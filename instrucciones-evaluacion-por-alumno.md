# Instrucciones para evaluar una entrega individual — EP1 DSY1105

Esta guía define el procedimiento repetible para revisar **un estudiante a la vez**. Debe usarse junto con:

- [Rúbrica central](pauta-rubrica-evaluacion-parcial-1-dsy1105.md): única fuente de los 11 indicadores, pesos y niveles de calificación.
- [Pauta complementaria por forma](pauta-complementaria-formas-d-e-f-dsy1105.md): pruebas de negocio para las formas D, E y F. No añade puntaje.

No se debe inferir evidencia a partir del nombre de un archivo, de una carpeta o de un repositorio. Registrar siempre la ruta, el archivo, la clase/función o la salida de consola que sustenta cada conclusión.

## Estructura de trabajo

Cada estudiante dispone de una carpeta en `entregas/`:

```text
entregas/<identificador>/
  <identificador>_intento_<fecha>.txt     # comprobante de entrega
  <archivo-entregado>.zip | .7z           # si existe
```

Mantener los artefactos originales sin modificar. Para la revisión, crear el registro en:

```text
revision/<identificador>/
  evaluacion.md
  fuente/                                  # copia o extracción de trabajo, si procede
```

No usar la existencia de una carpeta local como prueba de que la entrega se subió correctamente a AVA. La validación de AVA, identidad e integridad académica corresponde a docencia y se registra como `PENDIENTE DOCENCIA` cuando no haya evidencia institucional.

## Flujo de evaluación

### 1. Abrir y registrar la entrega

1. Seleccionar una sola carpeta `entregas/<identificador>/`.
2. Anotar el identificador, todos los archivos originales y sus tipos.
3. Leer el comprobante `.txt`. Puede contener el nombre, fecha, enlace a repositorio o SHA de commit declarado.
4. Verificar que el comprimido, si existe, pueda listarse y abrirse. Si está corrupto, vacío o no contiene código fuente, registrarlo con el mensaje concreto.
5. Si la entrega se declara en GitHub, usar como fuente el **commit declarado en el comprobante**. Si se revisa el HEAD actual, dejar explícito que es una revisión posterior y no sustituye la evidencia de la entrega original.

Resultado mínimo a registrar:

- ruta del comprobante y del archivo fuente;
- estado del archivo: `abrible`, `corrupto`, `sin código` u otro descriptivo;
- fuente exacta revisada: archivo local o URL + SHA;
- estado de AVA: `verificado por docencia`, `no entregado según docencia` o `PENDIENTE DOCENCIA`.

### 2. Identificar la forma del caso

Determinar si corresponde a la forma D, E o F a partir del enunciado incluido, el nombre explícito del proyecto o la terminología coherente del código:

| Forma | Sistema | Unidad de capacidad |
| --- | --- | --- |
| D | BikeCity | slots de bicicletas |
| E | PetCare | boxes veterinarios |
| F | GymSmart | puestos de gimnasio |

Si no hay evidencia suficiente, escribir `FORMA NO VERIFICABLE`. No deducirla solo desde el nombre del archivo comprimido. Una vez identificada, aplicar únicamente las pruebas `D-01…D-09`, `E-01…E-09` o `F-01…F-09` correspondientes en la pauta complementaria.

### 3. Inspeccionar el código antes de puntuar

Comprobar y registrar, como mínimo:

- punto de entrada y estructura Kotlin/Gradle disponible;
- variables y tipos para datos numéricos y textuales;
- cálculos de tarifas, impuestos, descuentos y recargos requeridos por la forma;
- condicionales para reglas y casos inválidos;
- funciones con responsabilidades separadas;
- colección de entidades/historial y operaciones de orden superior;
- clase base `open`, dos clases hijas y algún `override` efectivo;
- corrutina con `suspend`, `delay` y llamada coherente desde el flujo principal;
- `sealed class` y `when` para estados como evidencia contextual;
- `try-catch` y continuidad de la aplicación ante entradas inválidas;
- salida de consola legible, con consultas e informe de cierre aplicables.

El uso de `sealed class` y `when` es obligatorio en el enunciado, pero no tiene indicador ni peso independiente: vincularlo como evidencia contextual de los indicadores relacionados, sin inventar una fila nueva.

### 4. Compilar y ejecutar

1. Usar el mecanismo de construcción que realmente incluya la entrega (por ejemplo, Gradle si se proporcionan sus archivos de configuración).
2. Registrar el comando, entorno y resultado exacto.
3. Si compila, ejecutar las pruebas de escenario de la forma identificada, capturando la salida o describiendo el comportamiento observado.
4. Si no compila, conservar el error verificable. No inventar una ejecución ni otorgar evidencia funcional no demostrada.

La ambigüedad de una tarifa `$0` bajo el umbral debe tratarse tal como indica la pauta complementaria: comprobar que la regla exista y no produzca una caída, describir el comportamiento, y no penalizar una interpretación razonable hasta que docencia defina el criterio.

### 5. Calificar con la rúbrica central

Para cada indicador, seleccionar **solo uno** de estos niveles:

| Nivel | Factor | Cálculo |
| --- | ---: | --- |
| Muy buen desempeño | 100% | peso × 1,00 |
| Desempeño aceptable | 60% | peso × 0,60 |
| No logrado | 0% | peso × 0,00 |

No interpolar 80% ni 30%: aunque aparecen como descriptores generales del PDF, no están definidos en las filas de indicadores. El total es la suma de los 11 puntajes ponderados de la rúbrica central y debe quedar sobre 100.

Para cada fila, incluir una evidencia verificable (ruta + clase/función, prueba de escenario o salida) y una observación breve de retroalimentación. Las pruebas de la pauta complementaria se anotan como apoyo de evidencia; no crean puntos adicionales.

### 6. Cerrar el registro

Crear `revision/<identificador>/evaluacion.md` con la siguiente plantilla. No alterar los originales de `entregas/`.

```md
# Evaluación EP1 — <identificador>

## Trazabilidad de la entrega

- Comprobante: `entregas/<identificador>/<archivo>.txt`
- Archivo fuente: `<ruta o URL + SHA declarado>`
- Estado del archivo: `<abrible / corrupto / sin código / otro>`
- Forma identificada: `<D / E / F / NO VERIFICABLE>`
- Evidencia para identificar la forma: `<ruta y descripción>`
- Compilación/ejecución: `<comando, entorno y resultado>`
- Entrega AVA, identidad e integridad: `<verificado por docencia / PENDIENTE DOCENCIA>`
- Tratamiento observado de tarifa $0 (si aplica): `<descripción o pendiente docencia>`

## Pruebas de negocio

| Prueba | Resultado (C/P/N) | Evidencia observada | Indicadores relacionados |
| --- | --- | --- | --- |
| `<D/E/F>-01` |  |  |  |
| `<D/E/F>-02` |  |  |  |
| `<D/E/F>-03` |  |  |  |
| `<D/E/F>-04` |  |  |  |
| `<D/E/F>-05` |  |  |  |
| `<D/E/F>-06` |  |  |  |
| `<D/E/F>-07` |  |  |  |
| `<D/E/F>-08` |  |  |  |
| `<D/E/F>-09` |  |  |  |

## Rúbrica central

| ID | Peso | Nivel (100/60/0) | Puntaje | Evidencia verificable | Retroalimentación |
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

## Retroalimentación global

`<fortalezas, brechas prioritarias y una siguiente mejora concreta>`

## Aspectos pendientes de decisión docente

`<AVA, identidad, integridad, interpretación de tarifa $0 u otros>`
```

## Criterio de cierre por estudiante

La evaluación queda lista para revisión docente cuando el registro contiene la fuente exacta, forma identificada o marcada como no verificable, resultado de compilación/ejecución, las 11 filas puntuadas con evidencia y el total calculado. Si falta una de esas condiciones, indicar claramente `INCOMPLETA` y explicar qué evidencia falta; no completar los vacíos por suposición.
