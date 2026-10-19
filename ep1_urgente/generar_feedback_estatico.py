#!/usr/bin/env python3
"""Prepara feedback estático por IL; no asigna notas automáticas."""
import csv, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CSV=ROOT/'.work/revision-rapida/matriz_para_calificar.csv'
OUT=ROOT/'revision/feedback-estatico'
IDS=['IE 1.1.1','IE 1.1.2','IE 1.1.3','IE 1.2.1','IE 1.2.2','IE 1.2.3','IE 1.2.4','IE 1.3.1','IE 1.3.2','IE 1.3.3','IE 1.3.4']
NAMES=['Variables y tipos','Cálculos','Condicionales','Funciones y modularidad','Colecciones','Funciones de orden superior','Salida por consola','Herencia','Polimorfismo','Corrutinas','Manejo de excepciones']
WEIGHTS=[10,10,10,10,10,15,5,10,5,10,5]
PAT=[r'\b(?:val|var)\s+\w+',r'\w+\s*[+*/-]\s*\w+',r'\b(?:if|when)\s*[(\{]',r'\bfun\s+\w+',r'\b(?:listOf|mutableListOf|List|mapOf|mutableMapOf)\b',r'\.\s*(?:filter|map|sumOf|find|groupBy|count|sortedBy)\b',r'\bprintln?\s*\(',r'\b(?:open|abstract)\s+class\b',r'\boverride\s+fun\b',r'\bsuspend\s+fun\b',r'\btry\s*\{']
FEEDBACK=[
'Veo declaraciones de datos del dominio; revisar correspondencia de tipos y mutabilidad.',
'Hay expresiones aritméticas; contrastar resultados con la tarifa e impuestos del caso.',
'Existen condiciones de flujo; verificar cobertura de escenarios límite.',
'Existen funciones; evaluar responsabilidad única y separación de lógica.',
'Se declara una colección; comprobar que gestione las entidades del sistema.',
'Se observan operaciones de colección; revisar aplicación y corrección del resultado.',
'Existe salida de consola; revisar claridad y cobertura del informe.',
'Hay una clase base abierta o abstracta; verificar que tenga derivadas y reutilización.',
'Hay métodos sobrescritos; comprobar que cambien el comportamiento mediante polimorfismo.',
'Existe una función suspend; verificar delay y conexión con el flujo principal.',
'Existe try-catch; verificar recuperación real de entradas inválidas.'
]
NO=[
'No se localizó declaración suficiente de variables y tipos.',
'No se identificaron expresiones de cálculo de forma inequívoca.',
'No se localizaron condiciones relevantes.',
'No se localizaron funciones Kotlin.',
'No se identificó colección List/Map.',
'No se identificaron funciones de orden superior.',
'No se encontró evidencia de salida por consola.',
'No se identificó clase base abierta o abstracta.',
'No se identificó sobrescritura de métodos.',
'No se detectó implementación completa de suspend y delay.',
'No se identificó try-catch.'
]
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 with CSV.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
 report=[]
 for row in rows:
  sid=row['id'];repo=ROOT/'.work/fuentes'/sid/'repo'
  zdir=ROOT/'.work/revision-rapida/extraidos'/sid
  base=repo if row.get('fuente')=='GitHub HEAD' and repo.exists() else zdir
  files=[]
  if base.exists():
   for p in base.rglob('*.kt'):
    rel=p.relative_to(base).as_posix()
    if any(x in '/'+rel.lower()+'/' for x in ('/.git/','/build/','/labs/','/laboratorios/','/desafios/')):continue
    files.append((rel,p.read_text(encoding='utf-8',errors='replace')))
   focused=[x for x in files if re.search(r'(^|/)(?:evaluaciones?/)?(?:ev1|ep1|eval1|ev1_forma[^/]*)/',x[0],re.I)]
   if focused:files=focused
   if len(files)>1:files=[x for x in files if not x[0].lower().endswith('/prueba.kt')]
  joined='\n'.join(code for _,code in files)
  rows_md=['# Evaluación EP1 — '+sid,'','- Fuente: '+row.get('fuente',''),' - SHA: '+row.get('sha',''),
       '- Revisión exclusivamente estática: sin pruebas de ejecución en este informe.','',
       '## Feedback por indicador','','| IL | Peso | Estado | Evidencia y retroalimentación |','|---|---:|---|---|']
  positives=0
  for i,il in enumerate(IDS):
   matches=[]
   for path,code in files:
    m=re.search(PAT[i],code)
    if m:matches.append(path+':'+str(code.count('\n',0,m.start())+1))
   valid=bool(matches)
   if i==9:valid=valid and bool(re.search(r'\bdelay\s*\(',joined))
   if valid:positives+=1
   status='INDICIO' if valid else ('NO IDENTIFICADO' if files else 'SIN FUENTE')
   detail=(', '.join(matches[:3])+' — '+FEEDBACK[i]) if valid else (NO[i]+' Requiere inspección antes de poner 0.' if files else 'Falta recuperar código; no calificar.')
   rows_md.append('| '+il+' — '+NAMES[i]+' | '+str(WEIGHTS[i])+'% | '+status+' | '+detail.replace('|','/')+' |')
  rows_md+=['','## Retroalimentación general',
      ('Se inspeccionaron '+str(len(files))+' archivos Kotlin. Hay indicios en '+str(positives)+' de 11 indicadores. '
      +'Fortalezas: revisar los indicadores con evidencia citada. Brechas prioritarias: verificar los no identificados y las reglas del caso. '
      +'La revisión estática no confirma funcionamiento.') if files else 'Sin fuente suficiente para retroalimentación de la solución.',
      '','## Pendiente docente','No se ha validado funcionalidad, casos de negocio ni publicación en AVA. '
      +'Los niveles 100/60/0 y nota definitiva necesitan decisión docente fundamentada.']
  (OUT/(sid+'.md')).write_text('\n'.join(rows_md)+'\n',encoding='utf-8')
  report.append({'id':sid,'fuente':row.get('fuente',''),'sha':row.get('sha',''),'archivos_kt':len(files),
                'indicadores_con_indicio':positives,'puntaje_validado':'','estado':'REVISAR' if files else 'SIN_FUENTE'})
 with (OUT/'consolidado.csv').open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(report[0]));w.writeheader();w.writerows(report)
 print('Fichas:',len(report),'Ubicación:',OUT)
if __name__=='__main__':main()
