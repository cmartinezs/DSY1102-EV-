# Pauta de correccion — Evaluacion Parcial 1 (DSY1105)

Documento de trabajo para aplicar la pauta a las entregas individuales. Se elaboro a partir de `Evaluación Parcial 1_Estudiante_DSY1105.pdf`; no asigna calificaciones ni sustituye una decision docente.

## Alcance de la evaluacion

- Asignatura: **DSY1105 — Desarrollo de Aplicaciones Móviles**.
- Modalidad: ejecucion practica, individual, aplicacion funcional de consola en Kotlin.
- Caso de negocio: se entrega el dia de la evaluacion. Cada solucion se revisa contra los requisitos de ese caso, ademas de los indicadores de esta pauta.
- Entrega declarada: proyecto comprimido y cargado en AVA antes de terminar la evaluacion.
- Regla administrativa del enunciado: la ausencia de entrega en AVA genera nota 1.0. Esta condicion debe verificarse por separado; la sola presencia de un archivo en `entregas/` no demuestra una entrega valida en AVA.

## Regla de puntuacion

La pauta detallada presenta tres categorias por indicador:

| Nivel aplicable | Factor del peso | Uso |
| --- | ---: | --- |
| Muy buen desempeño | 100% | Cumple completamente el indicador y la evidencia funciona en el caso entregado. |
| Desempeño aceptable | 60% | Cumple lo esencial, pero presenta las omisiones o errores descritos en el indicador. |
| Desempeño no logrado | 0% | No implementa el indicador o la evidencia es incorrecta/no funcional. |

> El PDF tambien define descriptores generales de 80% (buen desempeño) y 30% (desempeño incipiente), pero la tabla de indicadores solo provee columnas y descriptores especificos para 100%, 60% y 0%. Por consistencia y trazabilidad, **no interpolar 80% ni 30%** sin una instruccion explicita de la docencia.

Formula: `puntaje final (%) = Σ (peso del indicador × factor del nivel)`.

Ejemplo: en un indicador de 10%, nivel aceptable = `10 × 0,60 = 6,0` puntos porcentuales.

## Preparacion de la revision

1. Identificar al estudiante y el archivo de entrega. Registrar si el comprimido puede abrirse y si contiene codigo fuente.
2. Localizar el punto de entrada y ejecutar o compilar la aplicacion cuando el entorno lo permita.
3. Contrastar la solucion con el caso de negocio asignado. Si ese caso no esta disponible, marcar esa parte como `NO VERIFICABLE`; no inferir requisitos.
4. Para cada indicador, registrar ruta, clase, funcion y una evidencia concreta (o la ausencia de ella).
5. Otorgar exclusivamente 100%, 60% o 0%, calcular el subtotal y dejar una observacion breve, verificable y respetuosa.

## Lista de evidencias minimas del enunciado

- Aplicacion de consola funcional que procesa informacion y determina resultados segun multiples condiciones.
- Variables y tipos de datos pertinentes; operadores aritmeticos, condicionales y logicos.
- Clase base `open`, al menos dos clases hijas, y un metodo sobrescrito con `override` que evidencie polimorfismo.
- `List` de objetos del caso y operaciones de orden superior (`filter`, `map`, `sumOf` u otras pertinentes).
- Funcion `suspend` con `delay`, invocada coherentemente desde el flujo principal (por ejemplo, mediante `runBlocking`).
- `sealed class` para estados de la operacion asincrona y expresion `when` para gestionarlos.
- Manejo de entradas/datos invalidos con `try-catch` (el ejemplo del PDF es un precio negativo), sin que la aplicacion falle.
- Codigo modular, legible y con comentarios en secciones clave.

## Rubrica analitica (100%)

La tabla de ponderaciones del PDF suma 100% con los 11 indicadores siguientes. Por ello, el uso de `sealed class`/`when` se registra como requisito obligatorio y evidencia contextual, pero **no recibe un puntaje independiente**: el documento no le asigna una fila ni ponderacion propia. Si la docencia define como evaluarlo, debe quedar consignado antes de calificar.

| ID | Indicador y evidencia a revisar | 100% — muy buen desempeño | 60% — desempeño aceptable | 0% — no logrado | Peso |
| --- | --- | --- | --- | --- | ---: |
| IE 1.1.1 | Declara variables y selecciona tipos Kotlin pertinentes (`Int`, `Double`, `String`, `val`/`var`) para informacion numerica y textual del problema. | Tipos correctos y pertinentes para los requisitos del problema, incluida la mutabilidad necesaria. | La mayoria de los tipos son correctos, pero hay algun error significativo (p. ej., `Int` para un precio). | No declara variables adecuadamente, o los tipos son completamente incorrectos. | 10% |
| IE 1.1.2 | Aplica operadores aritmeticos para los calculos requeridos por el caso. | Todos los calculos requeridos son correctos, con logica clara y tipo de dato apropiado. | Realiza los calculos, pero el resultado es incorrecto por un error logico. | No implementa los calculos solicitados. | 10% |
| IE 1.1.3 | Implementa condicionales `if/else` o `when` para controlar el flujo segun datos procesados. | Condicionales efectivos, robustos y que cubren los casos necesarios. | Implementa condicionales, pero son incompletos o no cubren todos los casos necesarios. | No utiliza estructuras condicionales. | 10% |
| IE 1.2.1 | Estructura el codigo en funciones modulares y reutilizables. | Funciones con logica especifica encapsulada; nombres descriptivos, responsabilidad unica, buena comprension y mantenimiento. | Hay funciones claras, pero la logica esta mezclada y no respeta completamente la responsabilidad unica. | No usa funciones para estructurar el codigo. | 10% |
| IE 1.2.2 | Usa una coleccion `List` o `Map` para almacenar y gestionar datos del caso. | Coleccion creada y gestionada correctamente dentro del flujo del programa. | Coleccion funcional, pero con manejo ineficiente o errores menores. | No utiliza una coleccion para gestionar los datos. | 10% |
| IE 1.2.3 | Aplica funciones de orden superior (`filter`, `map`, `sumOf`, etc.) para consultar o transformar la coleccion. | Uso idiomatico y eficiente para analizar o transformar datos de forma concisa. | Usa funciones de orden superior, pero recurre a ciclos `for` en operaciones que deberian resolverse de forma funcional. | No implementa funciones de orden superior. | 15% |
| IE 1.2.4 | Recorre la coleccion y muestra resultados en consola. | Resultados claros, ordenados y faciles de leer; simulan adecuadamente la capa de presentacion. | La visualizacion funciona, pero es incompleta o desordenada. | No muestra resultados de las operaciones. | 5% |
| IE 1.3.1 | Implementa jerarquia de clases con herencia. | Clase base `open` y clases hijas; aplica principios de reutilizacion y extension del comportamiento. | Implementa herencia, pero con errores conceptuales graves (p. ej., clase base no `open` o parametros mal delegados). | No utiliza clases ni herencia. | 10% |
| IE 1.3.2 | Aplica polimorfismo mediante sobrescritura de metodos. | Metodo sobrescrito con `override` en clase derivada; evidencia modificacion del comportamiento heredado mediante instancias polimorficas. | Hay sobrescritura, pero con errores de sintaxis o sin marcar correctamente el metodo base como `open`. | No implementa sobrescritura de metodos. | 5% |
| IE 1.3.3 | Implementa una tarea asincrona simple con corrutinas (`suspend fun`, `delay`). | Funcion `suspend` con `delay`, ejecutada desde `runBlocking` e integrada coherentemente en el flujo. | Incluye la funcion `suspend` y `delay`, pero la ejecucion desde `main` es incorrecta o no funciona como se espera. | No implementa tarea asincrona. | 10% |
| IE 1.3.4 | Implementa manejo basico de excepciones con `try-catch`. | Bloque `try-catch` robusto para excepciones posibles, evita que la aplicacion falle y permite continuar ante errores controlados. | Usa `try-catch`, pero no captura la excepcion correctamente o no maneja el error de forma adecuada. | No implementa manejo de errores. | 5% |

## Registro por estudiante (copiar esta seccion)

### Estudiante: `[nombre o identificador]`

- Archivo revisado: `[ruta]`
- Estado del archivo: `[abrible / corrupto / sin codigo / otro]`
- Caso de negocio disponible: `[si / no — NO VERIFICABLE]`
- Ejecucion o compilacion: `[resultado y comando/entorno usado]`
- Entrega AVA verificada por docencia: `[si / no / pendiente]`

| ID | Peso | Nivel (100/60/0) | Puntaje | Evidencia verificable | Observacion de retroalimentacion |
| --- | ---: | ---: | ---: | --- | --- |
| IE 1.1.1 | 10% |  |  |  |  |
| IE 1.1.2 | 10% |  |  |  |  |
| IE 1.1.3 | 10% |  |  |  |  |
| IE 1.2.1 | 10% |  |  |  |  |
| IE 1.2.2 | 10% |  |  |  |  |
| IE 1.2.3 | 15% |  |  |  |  |
| IE 1.2.4 | 5% |  |  |  |  |
| IE 1.3.1 | 10% |  |  |  |  |
| IE 1.3.2 | 5% |  |  |  |  |
| IE 1.3.3 | 10% |  |  |  |  |
| IE 1.3.4 | 5% |  |  |  |  |
| **Total** | **100%** |  | **/ 100** |  |  |

**Retroalimentacion global:** `[fortalezas, brechas prioritarias y siguiente mejora concreta]`

## Descriptores generales del PDF (referencia)

| Nivel | Factor | Descripcion general |
| --- | ---: | --- |
| Muy buen desempeño | 100% | Logro destacado de todos los aspectos evaluados en el indicador. |
| Buen desempeño | 80% | Alto desempeño, con pequeñas omisiones, dificultades o errores. |
| Desempeño aceptable | 60% | Logro de elementos basicos, con omisiones, dificultades o errores. |
| Desempeño incipiente | 30% | Omisiones, dificultades o errores importantes que no evidencian los elementos basicos. |
| Desempeño no logrado | 0% | Ausencia de evidencia o desempeno incorrecto. |
