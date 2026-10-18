#!/usr/bin/env python3
"""Recupera repositorios de estudiantes sin alterar entregas originales.
Requiere git y Python 3.10+. Los resultados se guardan en .work/ (gitignored).
"""
from __future__ import annotations
import argparse
import json
import re
import subprocess
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
ENTREGAS = ROOT / "entregas"
WORK = ROOT / ".work"
GITHUB = re.compile(r"https?://github\.com/[\w.-]+/[\w.-]+(?:\.git)?(?:/[^\s<>]*)?", re.I)

def run(*args: str, cwd: Path | None = None) -> str:
    p = subprocess.run(args, cwd=cwd, text=True, capture_output=True, timeout=45,
                       stdin=subprocess.DEVNULL,
                       env={**os.environ, "GIT_TERMINAL_PROMPT": "0", "GCM_INTERACTIVE": "never"})
    if p.returncode:
        raise RuntimeError(f"{' '.join(args)}: {p.stderr.strip() or p.stdout.strip()}")
    return p.stdout.strip()

def repositories(txt: str) -> list[str]:
    urls = []
    for raw in GITHUB.findall(txt):
        path = urlparse(raw.rstrip(').,;')).path.strip('/').split('/')
        if len(path) < 2:
            continue
        repo = path[1].removesuffix('.git')
        value = f"https://github.com/{path[0]}/{repo}.git"
        if value not in urls:
            urls.append(value)
    return urls

def evaluate(student: Path) -> dict:
    ident = student.name
    out = {"student": ident, "checked_at": datetime.now(timezone.utc).isoformat(),
           "status": "NO_GITHUB_URL", "declared_urls": [], "local_archives": [],
           "source": None, "head_sha": None, "default_branch": None,
           "candidate_paths": [], "error": None}
    for file in student.iterdir():
        if file.suffix.lower() in {".zip", ".7z", ".rar"}:
            out["local_archives"].append(str(file.relative_to(ROOT)))
        if file.suffix.lower() == ".txt":
            out["declared_urls"].extend(repositories(file.read_text(encoding="utf-8", errors="replace")))
    out["declared_urls"] = list(dict.fromkeys(out["declared_urls"]))
    if not out["declared_urls"]:
        return out
    url = out["declared_urls"][0]
    # Prioriza SSH para no solicitar credenciales interactivas de GitHub.
    url = re.sub(r"^https://github\\.com/", "git@github.com:", url)
    dest = WORK / "fuentes" / ident / "repo"
    try:
        # --symref is needed to determine the remote default branch.
        sym = run("git", "ls-remote", "--symref", url, "HEAD")
        m = re.search(r"ref:\s+refs/heads/([^\s]+)\s+HEAD", sym)
        if not m:
            raise RuntimeError("No se pudo determinar rama por defecto de HEAD")
        branch = m.group(1)
        sha = next((x.split()[0] for x in sym.splitlines() if x.endswith("\tHEAD") and not x.startswith("ref:")), None)
        if not sha:
            raise RuntimeError("No se encontró SHA para HEAD")
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            if not (dest / ".git").is_dir():
                raise RuntimeError(f"Destino existente sin .git: {dest}")
            existing = run("git", "-C", str(dest), "remote", "get-url", "origin")
            if existing != url:
                raise RuntimeError(f"Remote origin inesperado: {existing}")
            run("git", "-C", str(dest), "fetch", "--depth=1", "origin", sha)
        else:
            run("git", "clone", "--no-checkout", "--depth=1", "--single-branch", "--branch", branch, url, str(dest))
            run("git", "-C", str(dest), "fetch", "--depth=1", "origin", sha)
        run("git", "-C", str(dest), "checkout", "--force", "--detach", sha)
        paths = run("git", "-C", str(dest), "ls-files").splitlines()
        candidates = [p for p in paths if re.search(r"(^|/)(evaluaciones?/)?(ev1|ep1|eval1|ev1_forma[^/]*)($|/)", p, re.I)]
        out.update(status="FETCHED", source=url, head_sha=sha, default_branch=branch,
                   candidate_paths=candidates[:250])
    except Exception as exc:
        out.update(status="BLOCKED_GITHUB", source=url, error=str(exc))
    return out

def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--student")
    group.add_argument("--all", action="store_true")
    args = parser.parse_args()
    students = sorted(p for p in ENTREGAS.iterdir() if p.is_dir())
    if args.student:
        students = [p for p in students if p.name == args.student]
        if not students:
            parser.error("Estudiante no encontrado")
    (WORK / "manifest").mkdir(parents=True, exist_ok=True)
    for student in students:
        result = evaluate(student)
        destination = WORK / "manifest" / f"{student.name}.json"
        tmp = destination.with_suffix(".tmp")
        tmp.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        tmp.replace(destination)
        print(f"{student.name}: {result['status']} ({len(result['candidate_paths'])} rutas candidatas)")

if __name__ == "__main__":
    main()
