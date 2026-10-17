# Evaluación EP1 — DSY1105

> **Aviso de nomenclatura:** el repositorio se llama `DSY1102-EV-`, pero las pautas y entregas actuales pertenecen a **DSY1105 — Desarrollo de Aplicaciones Móviles**. No mezclar evaluaciones de DSY1102 aquí sin separar previamente los cursos.

## Estado y fuente de verdad

- `entregas/<id>/`: comprobantes y adjuntos originales **inmutables**.
- `pauta-rubrica-evaluacion-parcial-1-dsy1105.md`: 11 indicadores (100/60/0), 100 puntos.
- `pauta-complementaria-formas-d-e-f-dsy1105.md`: pruebas por forma D/E/F, sin puntos adicionales.
- `instrucciones-evaluacion-por-alumno.md`: plantilla base; la política de selección posterior acordada con docencia está descrita en `docs/PROCEDIMIENTO-LOCAL.md`.
- `revision/<id>/`: informes y evidencia de cada estudiante.

**Política acordada:** ante un repositorio GitHub verificable, revisar su HEAD actual en la rama por defecto y buscar `evaluaciones/ev1`, `evaluaciones/ep1`, `ev1`, `ep1` y variantes. Registrar también el commit que figure en el comprobante; es evidencia histórica, no el código base de la revisión actual. Preferir el ZIP solo si GitHub no contiene la evaluación o es inaccesible. La evaluación no se completa por una mera inspección de carpetas.

## Ejecución local (WSL2)

```bash
git pull --ff-only
python3 scripts/recuperar_fuentes.py --student ab.puente
```

El script busca repositorios declarados en los comprobantes, resuelve su HEAD vía Git sin necesidad de `gh`, clona fuera del árbol versionado bajo `.work/` y produce trazabilidad. No compila, no califica y no sube resultados automáticamente. El código de estudiantes es **no confiable**; compilar/ejecutar en un entorno aislado sin credenciales.

**Privacidad:** este repositorio aparece como público y contiene entregas de estudiantes, nombres y posibles datos personales. Revisar su visibilidad antes de publicar notas, fichas o evidencias adicionales. Las calificaciones quedan fuera de Git por defecto.
