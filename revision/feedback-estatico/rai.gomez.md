# Evaluación EP1 — rai.gomez

- Fuente: GitHub HEAD
 - SHA: 785b10a43cb81d439c77ebe773de4f8e6e2d371b
- Revisión exclusivamente estática: sin pruebas de ejecución en este informe.

## Feedback por indicador

| IL | Peso | Estado | Evidencia y retroalimentación |
|---|---:|---|---|
| IE 1.1.1 — Variables y tipos | 10% | INDICIO | practica-kotlin/laboratorio-java-kotlin/src/cl/duoc/dsy11052/lab/LaboratorioKotlin.kt:16, src/main/kotlin/Main.kt:5, src/main/kotlin/SistemasBikeCity.kt:3 — Veo declaraciones de datos del dominio; revisar correspondencia de tipos y mutabilidad. |
| IE 1.1.2 — Cálculos | 10% | INDICIO | src/main/kotlin/SistemasBikeCity.kt:8, src/main/kotlin/Modelos.kt:26 — Hay expresiones aritméticas; contrastar resultados con la tarifa e impuestos del caso. |
| IE 1.1.3 — Condicionales | 10% | INDICIO | practica-kotlin/laboratorio-java-kotlin/src/cl/duoc/dsy11052/lab/LaboratorioKotlin.kt:5, src/main/kotlin/SistemasBikeCity.kt:18, src/main/kotlin/Modelos.kt:31 — Existen condiciones de flujo; verificar cobertura de escenarios límite. |
| IE 1.2.1 — Funciones y modularidad | 10% | INDICIO | practica-kotlin/laboratorio-java-kotlin/src/cl/duoc/dsy11052/lab/LaboratorioKotlin.kt:3, src/main/kotlin/Main.kt:3, src/main/kotlin/SistemasBikeCity.kt:12 — Existen funciones; evaluar responsabilidad única y separación de lógica. |
| IE 1.2.2 — Colecciones | 10% | INDICIO | src/main/kotlin/SistemasBikeCity.kt:9 — Se declara una colección; comprobar que gestione las entidades del sistema. |
| IE 1.2.3 — Funciones de orden superior | 15% | INDICIO | src/main/kotlin/SistemasBikeCity.kt:84 — Se observan operaciones de colección; revisar aplicación y corrección del resultado. |
| IE 1.2.4 — Salida por consola | 5% | INDICIO | practica-kotlin/laboratorio-java-kotlin/src/cl/duoc/dsy11052/lab/LaboratorioKotlin.kt:21, src/main/kotlin/Main.kt:4, src/main/kotlin/SistemasBikeCity.kt:19 — Existe salida de consola; revisar claridad y cobertura del informe. |
| IE 1.3.1 — Herencia | 10% | INDICIO | src/main/kotlin/Modelos.kt:16 — Hay una clase base abierta o abstracta; verificar que tenga derivadas y reutilización. |
| IE 1.3.2 — Polimorfismo | 5% | INDICIO | src/main/kotlin/Modelos.kt:50 — Hay métodos sobrescritos; comprobar que cambien el comportamiento mediante polimorfismo. |
| IE 1.3.3 — Corrutinas | 10% | INDICIO | src/main/kotlin/SistemasBikeCity.kt:17 — Existe una función suspend; verificar delay y conexión con el flujo principal. |
| IE 1.3.4 — Manejo de excepciones | 5% | NO IDENTIFICADO | No se identificó try-catch. Requiere inspección antes de poner 0. |

## Retroalimentación general
Se inspeccionaron 4 archivos Kotlin. Hay indicios en 10 de 11 indicadores. Fortalezas: revisar los indicadores con evidencia citada. Brechas prioritarias: verificar los no identificados y las reglas del caso. La revisión estática no confirma funcionamiento.

## Pendiente docente
No se ha validado funcionalidad, casos de negocio ni publicación en AVA. Los niveles 100/60/0 y nota definitiva necesitan decisión docente fundamentada.
