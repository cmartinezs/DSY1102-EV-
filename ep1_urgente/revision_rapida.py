#!/usr/bin/env python3
"""Precorrección estática de DSY1105 EP1. No asigna notas."""
import argparse,csv,json,re,zipfile
from pathlib import Path
from collections import Counter
IDS=['IE 1.1.1','IE 1.1.2','IE 1.1.3','IE 1.2.1','IE 1.2.2','IE 1.2.3','IE 1.2.4','IE 1.3.1','IE 1.3.2','IE 1.3.3','IE 1.3.4']
WEIGHTS=[10,10,10,10,10,15,5,10,5,10,5]
CUES=[r'\b(val|var)\b',r'(?<![\w])(?:\+|\*|/|-)(?!>)',r'\b(if|when)\b',r'\bfun\s+\w+',r'\b(?:mutableListOf|listOf|List\s*\(|mutableMapOf|mapOf)\b',r'\b(?:filter|map|sumOf|find|groupBy|count|sortedBy)\s*\{',r'\b(?:print|println)\s*\(',r'\b(?:open|abstract)\s+class\b',r'\boverride\s+fun\b',r'\bsuspend\s+fun\b',r'\btry\s*\{']
REPO_PATH=re.compile(r'(^|/)(?:evaluaciones?/)?(?:ev1|ep1|eval1|ev1_forma[^/]*)(?:/|$)',re.I)
REJECT=re.compile(r'(^|/)(?:labs?|desafios?|ejercicios?|build|\.gradle|\.git|out|test)(?:/|$)',re.I)
def detect_form(s):
    s=s.lower()
    scores={'D':sum(s.count(w) for w in ('bikecity','bicicleta','slot')),'E':sum(s.count(w) for w in ('petcare','paciente','veterinaria','box')),'F':sum(s.count(w) for w in ('gymsmart','gimnasio','puesto','entrenamiento'))}
    k=max(scores,key=scores.get)
    return k if scores[k]>=2 and scores[k]>sorted(scores.values())[-2] else 'NO_VERIFICABLE'
def extract_zip(src,dst):
    try:
        with zipfile.ZipFile(src) as z:
            total=0
            for item in z.infolist():
                if item.is_dir():continue
                p=Path(item.filename)
                if p.is_absolute() or '..' in p.parts or item.file_size>15_000_000:continue
                total+=item.file_size
                if total>80_000_000:break
                if p.suffix.lower() in ('.kt','.kts','.gradle','.md','.txt','.properties'):
                    target=dst/p;target.parent.mkdir(parents=True,exist_ok=True)
                    with z.open(item) as inp:target.write_bytes(inp.read())
        return True
    except (OSError,zipfile.BadZipFile,RuntimeError):return False
def sources(base):
    allkt=[p for p in base.rglob('*.kt') if not REJECT.search(p.relative_to(base).as_posix())]
    prioritized=[p for p in allkt if REPO_PATH.search(p.relative_to(base).as_posix())]
    if prioritized:return prioritized,'EV1'
    if not allkt:return [],'SIN_KOTLIN'
    parent=Path(Counter(str(p.parent) for p in allkt).most_common(1)[0][0])
    return [p for p in allkt if p.parent==parent],'RUTA_ALTERNATIVA_REVISAR'
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--root',default='.')
    args=ap.parse_args()
    root=Path(args.root).resolve();out=root/'.work'/'revision-rapida';out.mkdir(parents=True,exist_ok=True)
    fields=['id','fuente','sha','forma','compilacion','alertas','nota_propuesta_100','estado_docente']+[f'{k}_nivel' for k in IDS]
    rows=[]
    for folder in sorted(p for p in (root/'entregas').iterdir() if p.is_dir()):
        ident=folder.name;manifest=root/'.work'/'manifest'/f'{ident}.json'
        meta=json.loads(manifest.read_text()) if manifest.is_file() else {}
        repo=root/'.work'/'fuentes'/ident/'repo'
        warnings=[];source=None;kind='NO_RECUPERADA'
        if meta.get('status')=='FETCHED' and repo.is_dir():
            source=repo;kind='GitHub HEAD'
        else:
            archives=list(folder.glob('*.zip'))+list(folder.glob('*.7z'))
            for archive in archives:
                if archive.suffix.lower()=='.7z':
                    warnings.append('7Z_REQUIERE_EXTRACCION');continue
                dst=out/'extraidos'/ident
                if extract_zip(archive,dst):source=dst;kind='ZIP';warnings.append('ZIP_RESPALDO');break
                warnings.append('ZIP_NO_EXTRAIBLE')
            if source is None:warnings.append('FUENTE_NO_RECUPERADA')
        record=dict(id=ident,fuente=kind,sha=meta.get('head_sha') or '',forma='NO_VERIFICABLE',compilacion='NO_EJECUTADA',alertas='',nota_propuesta_100='',estado_docente='BLOQUEADO' if source is None else 'REVISAR')
        if source:
            files,selection=sources(source)
            if selection!='EV1':warnings.append(selection)
            modular=[p for p in files if p.name.lower() not in ('prueba.kt','todo.kt')]
            if modular:files=modular
            contents=[(p.relative_to(source).as_posix(),p.read_text(encoding='utf-8',errors='replace')) for p in files]
            joined='\n'.join(code for _,code in contents);record['forma']=detect_form(joined)
            if record['forma']=='NO_VERIFICABLE':warnings.append('FORMA_NO_VERIFICABLE')
            evidence=[]
            for pat in CUES:
                matches=[]
                for filename,code in contents:
                    m=re.search(pat,code,re.I)
                    if m:matches.append(f'{filename}:{code[:m.start()].count(chr(10))+1}')
                evidence.append('; '.join(matches[:3]) or 'NO DETECTADO')
            doc=[f'# {ident} — revisión estática',f'Fuente: {kind}; SHA: {record["sha"]}; forma: {record["forma"]}',f'Selección: {selection}','','| Indicador | Peso | Evidencia sintáctica | Nivel |','|---|---:|---|---|']
            for ind,weight,ev in zip(IDS,WEIGHTS,evidence):
                doc.append(f'| {ind} | {weight} | {ev} | PENDIENTE |')
            doc.extend(['','**La evidencia sintáctica no confirma funcionamiento. No hay notas asignadas.**'])
            (out/f'{ident}.md').write_text('\n'.join(doc)+'\n',encoding='utf-8')
        record['alertas']=';'.join(warnings)
        for ind in IDS:record[f'{ind}_nivel']=''
        rows.append(record)
    with (out/'matriz_para_calificar.csv').open('w',newline='',encoding='utf-8-sig') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
    print(f'Procesados {len(rows)} alumnos; fuentes localizadas {sum(r["fuente"]!="NO_RECUPERADA" for r in rows)}')
    print(out/'matriz_para_calificar.csv')
if __name__=='__main__':main()
