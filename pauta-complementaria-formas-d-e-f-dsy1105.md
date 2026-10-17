# Pauta complementaria por forma — Evaluación Parcial 1 DSY1105

Esta pauta se usa junto con la [rúbrica central](pauta-rubrica-evaluacion-parcial-1-dsy1105.md). Convierte los requisitos de negocio particulares de cada forma en evidencia comprobable para la revisión de una entrega.

No añade indicadores ni ponderación: la calificación se conserva exclusivamente en los 11 indicadores y 100% de la rúbrica central. Cada resultado de esta pauta se anota como evidencia en la fila central correspondiente.

## Uso y límites

1. Primero identifica la forma mediante el enunciado incluido, el nombre explícito del proyecto o la terminología consistente del código. No la deduzcas solo del nombre del archivo de entrega.
2. Ejecuta las comprobaciones aplicables y registra `C` (cumple), `P` (parcial/no verificable) o `N` (no cumple), junto con la ruta y el comportamiento observado.
3. Una entrega que no compile no permite evidenciar los indicadores, conforme a los tres enunciados. Conserva el error de compilación como evidencia; no inventes una ejecución.
4. Las reglas de integridad académica, supervisión y entrega en AVA son decisiones docentes externas. Este repositorio no permite probarlas; regístralas como `PENDIENTE DOCENCIA` si no existe evidencia institucional.

## Controles transversales (todas las formas)

| Control | Evidencia esperada | Indicador central relacionado |
| --- | --- | --- |
| Kotlin/Gradle | Kotlin 1.9 o superior, `build.gradle.kts`, `settings.gradle.kts` y dependencia `kotlinx-coroutines-core` declarada. | IE 1.3.3 |
| Organización | Más de un archivo `.kt`, responsabilidades separadas, PascalCase para clases y camelCase para funciones/propiedades. | IE 1.2.1 |
| Comentarios | Comentarios en la lógica no evidente (tarifas, transiciones o validaciones). | IE 1.2.1 |
| Modelo OO | Clase base `open`, al menos dos hijas y un comportamiento sobrescrito con `override`. | IE 1.3.1, IE 1.3.2 |
| Estados | `sealed class` y `when` que considere los cuatro estados de la forma. La rúbrica central no le entrega peso propio: usar como evidencia contextual. | Contextual |
| Colecciones e informes | Colecciones para entidades/historial y operaciones funcionales para las consultas; salida de consola legible. | IE 1.2.2, IE 1.2.3, IE 1.2.4 |
| Robustez | Errores controlados, mensajes descriptivos y continuidad de la sesión, sin traza técnica para el usuario. | IE 1.3.4 |

## Ambigüedad común que requiere decisión docente

Los tres enunciados exigen que el resultado de una tarifa no sea negativo ni igual a cero, pero a la vez declaran un tipo cuyo cobro es `$0` bajo un umbral de minutos (BiciMontaña, Felino o Fuerza). No establecen si ese `$0` debe emitirse como ticket válido, informarse como caso especial o rechazarse como tarifa inválida.

Por ello, al corregir ese escenario:

- verifica que la regla del umbral exista y que la aplicación no falle;
- registra la decisión implementada y el mensaje mostrado;
- **no castigues una de las dos interpretaciones** hasta que la docencia defina el comportamiento esperado;
- no asignes decimales, redondeos ni una tolerancia temporal que el enunciado no especifica.

## Forma D — BikeCity: Sistema de Arriendo de Bicicletas

Fuente: `DSY1105_EP1_Instrucciones_Alumno_Forma_D.docx`.

### Reglas de negocio a verificar

| Área | Requisito específico |
| --- | --- |
| Capacidad | Sistema `BikeCity`, 10 slots; total recaudado y recaudación por tipo de bicicleta. |
| Dominio | Bicicleta con código inmutable de dos letras, dos dígitos y dos letras; marca, modelo, fecha/hora de ingreso y tipo de cliente. |
| Tipos | `BiciCiudad` ($800/h), `BiciMontana` ($1.500/h) y `BiciElectrica` ($2.200/h). |
| Reglas de tipo | Ciudad: abonado recibe 20% de descuento al calcular el arriendo. Montaña: menos de 20 min cobra $0. Eléctrica: larga autonomía suma 30%; el detalle informa si aplica. |
| Orden de tarifa | Primero regla propia/tipo y tiempo; luego IVA 19%; finalmente cliente discapacitado descuenta 50% sobre el monto con IVA. |
| Clientes válidos | `turista`, `abonado`, `discapacitado`; cualquier otro es inválido. |
| Slots | `Libre`, `Arrendada` (con bicicleta), `EnProceso` (con motivo) y `EnMantención` (con motivo). |
| Entrada asíncrona | Primer slot libre → `EnProceso` (“registrando entrada”) → espera de 3 s → `Arrendada` con bicicleta. |
| Salida asíncrona | Localiza código → `EnProceso` (“calculando tarifa”) → espera de 6,5 s → ticket, historial, recaudación, slot libre. |

### Comprobaciones de escenario

| ID | Prueba y evidencia observada | Resultado | Relación central |
| --- | --- | --- | --- |
| D-01 | Registrar `BC12CD`, Trek FX3, abonado; demostrar tarifa ciudad y descuento 20% antes del IVA. | C / P / N | IE 1.1.1, IE 1.1.2, IE 1.1.3, IE 1.3.1 |
| D-02 | Registrar `BC99ZA`, Giant Escape, turista; demostrar tarifa ciudad sin descuento. | C / P / N | IE 1.1.2, IE 1.3.1 |
| D-03 | Registrar/salir `BM22TO` con 18 min; comprobar regla bajo 20 min y anotar el tratamiento del conflicto de tarifa $0. | C / P / N | IE 1.1.2, IE 1.3.4 |
| D-04 | Registrar/salir `BE44RG`, larga autonomía y cliente discapacitado; comprobar recargo 30%, IVA y descuento 50% en ese orden. | C / P / N | IE 1.1.2, IE 1.1.3, IE 1.3.1 |
| D-05 | Registrar/salir `BE77RG`, no larga autonomía, turista; el detalle debe declararlo y no aplicar recargo/descuento. | C / P / N | IE 1.1.3, IE 1.2.4 |
| D-06 | Intentar registrar `123ABC`, salida de código inexistente y entrada sin slots libres; cada caso muestra mensaje claro y permite continuar. | C / P / N | IE 1.3.4 |
| D-07 | Observar las transiciones de slot en entrada/salida, los cuatro estados y los `delay` de 3 s/6,5 s. | C / P / N | IE 1.1.3, IE 1.3.3 |
| D-08 | Revisar consultas: slots libres; historial de abonados; ingreso promedio; códigos finalizados; bicicleta con mayor tiempo. | C / P / N | IE 1.2.2, IE 1.2.3, IE 1.2.4 |
| D-09 | Revisar cierre: por ticket tipo, código, tiempo y monto; total, cantidad, promedio, tipo con más ingresos y slots libres. | C / P / N | IE 1.2.3, IE 1.2.4 |

## Forma E — PetCare: Sistema de Gestión de Boxes Veterinarios

Fuente: `DSY1105_EP1_Instrucciones_Alumno_Forma_E.docx`.

### Reglas de negocio a verificar

| Área | Requisito específico |
| --- | --- |
| Capacidad | Sistema `PetCare`, 10 boxes; total recaudado y recaudación por tipo de paciente. |
| Dominio | Paciente con código de atención inmutable de dos letras, dos dígitos y dos letras; nombre, especie, fecha/hora y tipo de dueño. |
| Tipos | `Canino` ($12.000/h), `Felino` ($9.000/h) y `Exótico` ($20.000/h). |
| Reglas de tipo | Canino: dueño con convenio recibe 20% de descuento. Felino: menos de 20 min cobra $0. Exótico: animal silvestre suma 30%; el detalle informa si aplica. |
| Orden de tarifa | Primero regla propia/tipo y tiempo; luego IVA 19%; finalmente dueño municipal descuenta 50% sobre el monto con IVA. |
| Dueños válidos | `particular`, `convenio`, `municipal`; cualquier otro es inválido. |
| Boxes | `Libre`, `EnAtencion` (con paciente), `EnProceso` (con motivo) y `FueraDeServicio` (con motivo). |
| Entrada asíncrona | Primer box libre → `EnProceso` (“registrando entrada”) → espera de 3 s → `EnAtencion` con paciente. |
| Salida asíncrona | Localiza código → `EnProceso` (“calculando tarifa”) → espera de 6,5 s → ticket, historial, recaudación, box libre. |

### Comprobaciones de escenario

| ID | Prueba y evidencia observada | Resultado | Relación central |
| --- | --- | --- | --- |
| E-01 | Registrar `CA12CD`, Max/Golden Retriever, convenio; demostrar tarifa canino y descuento 20% antes del IVA. | C / P / N | IE 1.1.1, IE 1.1.2, IE 1.1.3, IE 1.3.1 |
| E-02 | Registrar `CA99ZA`, Luna/Labrador, particular; demostrar tarifa canino sin descuento. | C / P / N | IE 1.1.2, IE 1.3.1 |
| E-03 | Registrar/salir `FE22TO` con 18 min; comprobar regla bajo 20 min y anotar el tratamiento del conflicto de tarifa $0. | C / P / N | IE 1.1.2, IE 1.3.4 |
| E-04 | Registrar/salir `EX44RG`, silvestre y municipal; comprobar recargo 30%, IVA y descuento 50% en ese orden. | C / P / N | IE 1.1.2, IE 1.1.3, IE 1.3.1 |
| E-05 | Registrar/salir `EX77RG`, no silvestre y particular; el detalle debe declararlo y no aplicar recargo/descuento. | C / P / N | IE 1.1.3, IE 1.2.4 |
| E-06 | Intentar registrar `123ABC`, salida de código inexistente y entrada sin boxes libres; cada caso muestra mensaje claro y permite continuar. | C / P / N | IE 1.3.4 |
| E-07 | Observar las transiciones de box en entrada/salida, los cuatro estados y los `delay` de 3 s/6,5 s. | C / P / N | IE 1.1.3, IE 1.3.3 |
| E-08 | Revisar consultas: boxes libres; historial de clientes convenio; ingreso promedio; códigos finalizados; paciente con mayor tiempo. | C / P / N | IE 1.2.2, IE 1.2.3, IE 1.2.4 |
| E-09 | Revisar cierre: por ticket tipo, código, tiempo y monto; total, cantidad, promedio, tipo con más ingresos y boxes libres. | C / P / N | IE 1.2.3, IE 1.2.4 |

## Forma F — GymSmart: Sistema de Gestión de Equipos de Gimnasio

Fuente: `DSY1105_EP1_Instrucciones_Alumno_Forma_F.docx`.

### Reglas de negocio a verificar

| Área | Requisito específico |
| --- | --- |
| Capacidad | Sistema `GymSmart`, 10 puestos; total recaudado y recaudación por tipo de equipo. |
| Dominio | Equipo con código inmutable de dos letras, dos dígitos y dos letras; nombre/máquina, fecha/hora y tipo de usuario. |
| Tipos | `Cardio` ($1.000/h), `Fuerza` ($1.500/h) y `Funcional` ($2.500/h). |
| Reglas de tipo | Cardio: socio recibe 20% de descuento. Fuerza: menos de 15 min cobra $0. Funcional: sesión con entrenador suma 30%; el detalle informa si aplica. |
| Orden de tarifa | Primero regla propia/tipo y tiempo; luego IVA 19%; finalmente usuario `tercera_edad` descuenta 50% sobre el monto con IVA. |
| Usuarios válidos | `visitante`, `socio`, `tercera_edad`; cualquier otro es inválido. |
| Puestos | `Libre`, `EnUso` (con equipo), `EnProceso` (con motivo) y `EnMantención` (con motivo). |
| Entrada asíncrona | Primer puesto libre → `EnProceso` (“registrando entrada”) → espera de 3 s → `EnUso` con equipo. |
| Salida asíncrona | Localiza código → `EnProceso` (“calculando tarifa”) → espera de 6,5 s → ticket, historial, recaudación, puesto libre. |

### Comprobaciones de escenario

| ID | Prueba y evidencia observada | Resultado | Relación central |
| --- | --- | --- | --- |
| F-01 | Registrar `CA12CD`, Cinta Technogym, socio; demostrar tarifa cardio y descuento 20% antes del IVA. | C / P / N | IE 1.1.1, IE 1.1.2, IE 1.1.3, IE 1.3.1 |
| F-02 | Registrar `CA99ZA`, Bicicleta Spinning, visitante; demostrar tarifa cardio sin descuento. | C / P / N | IE 1.1.2, IE 1.3.1 |
| F-03 | Registrar/salir `FU22TO` con 12 min; comprobar regla bajo 15 min y anotar el tratamiento del conflicto de tarifa $0. | C / P / N | IE 1.1.2, IE 1.3.4 |
| F-04 | Registrar/salir `FN44RG`, con entrenador y `tercera_edad`; comprobar recargo 30%, IVA y descuento 50% en ese orden. | C / P / N | IE 1.1.2, IE 1.1.3, IE 1.3.1 |
| F-05 | Registrar/salir `FN77RG`, sin entrenador y visitante; el detalle debe declararlo y no aplicar recargo/descuento. | C / P / N | IE 1.1.3, IE 1.2.4 |
| F-06 | Intentar registrar `123ABC`, salida de código inexistente y entrada sin puestos libres; cada caso muestra mensaje claro y permite continuar. | C / P / N | IE 1.3.4 |
| F-07 | Observar las transiciones de puesto en entrada/salida, los cuatro estados y los `delay` de 3 s/6,5 s. | C / P / N | IE 1.1.3, IE 1.3.3 |
| F-08 | Revisar consultas: puestos libres; historial de socios; ingreso promedio; códigos finalizados; equipo con mayor tiempo. | C / P / N | IE 1.2.2, IE 1.2.3, IE 1.2.4 |
| F-09 | Revisar cierre: por ticket tipo, código, tiempo y monto; total, cantidad, promedio, tipo con más ingresos y puestos libres. | C / P / N | IE 1.2.3, IE 1.2.4 |

## Ficha de aplicación por estudiante

### Estudiante: `[nombre o identificador]` — Forma: `[D / E / F]`

- Archivo y ruta: `[ruta]`
- Forma identificada por: `[enunciado / nombre del proyecto / terminología del código]`
- Compilación/ejecución: `[comando, entorno y resultado]`
- Decisión aplicada al caso de tarifa $0: `[pendiente docencia / ticket válido / error controlado]`
- Controles externos (AVA, identidad, integridad académica): `[pendiente docencia / evidencia institucional]`

| Prueba | Resultado (C/P/N) | Ruta o salida observada | Vincular a fila central |
| --- | --- | --- | --- |
| `[D/E/F]-01` |  |  |  |
| `[D/E/F]-02` |  |  |  |
| `[D/E/F]-03` |  |  |  |
| `[D/E/F]-04` |  |  |  |
| `[D/E/F]-05` |  |  |  |
| `[D/E/F]-06` |  |  |  |
| `[D/E/F]-07` |  |  |  |
| `[D/E/F]-08` |  |  |  |
| `[D/E/F]-09` |  |  |  |

**Notas de evidencia y decisión docente:** `[texto]`
