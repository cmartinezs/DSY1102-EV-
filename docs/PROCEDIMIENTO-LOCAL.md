# Procedimiento local de evaluación — DSY1105 EP1

1. Leer la rúbrica y pauta por formas, además del comprobante de cada estudiante en `entregas/<id>/`.
2. Si hay URL GitHub, resolver rama por defecto y HEAD actual; registrar URL, SHA, fecha y commit declarado en comprobante, cuando exista.
3. Buscar código de evaluación en `evaluaciones/ev1`, `evaluaciones/ep1`, `ev1`, `ep1`, `eval1`, `Ev1_Forma*` o proyectos identificables por contenido. **Nunca** puntuar un laboratorio distinto.
4. Si el repositorio no es accesible, no contiene código EP1 o su ruta no es verificable, recurrir al comprimido original. Registrar razón de selección.
5. Confirmar forma D (BikeCity), E (PetCare) o F (GymSmart) mediante contenido. Anotar `NO VERIFICABLE` cuando proceda.
6. Compilar y ejecutar en contenedor/VM **sin red, secretos ni credenciales**; no ejecutar código estudiantil dentro de la sesión SSH autenticada del docente. Registrar comando y logs.
7. Aplicar únicamente los 11 indicadores de rúbrica con niveles 100%, 60% o 0% del peso, basados en evidencia concreta (ruta/línea/comportamiento).
8. Completar `revision/<id>/evaluacion.md` con trazabilidad, las 9 pruebas por forma, rúbrica y observaciones. No generar notas definitivas ante bloqueo de fuente o evidencia esencial.
9. Procesar **uno a uno**; iniciar con ab.puente, cla.jaime, enz.rojas. Persistir avances antes del siguiente.
10. Consolidar resultados únicamente después de revisar consistencia. Publicación al alumnado requiere aprobación docente.

## Operación

```bash
python3 scripts/recuperar_fuentes.py --student ab.puente
python3 scripts/recuperar_fuentes.py --all
```

La copia queda en `.work/fuentes/<id>/repo` y la metadata en `.work/manifest/<id>.json`, ignoradas por Git. El script no elimina carpetas existentes: si un checkout ya existe, utiliza `git fetch` y un checkout limpio de HEAD mediante directorio temporal. Si una ejecución falla, deja el error en el manifiesto y continúa con otros estudiantes.

**Divergencia documentada:** la pauta original pide corregir el commit declarado; la instrucción docente posterior pide HEAD actual. Para una evaluación histórica y justa, conservar ambos SHA y señalar cambios posteriores a la fecha original. No asignar cero por fallos de infraestructura.
