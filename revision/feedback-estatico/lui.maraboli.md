# Evaluación EP1 — lui.maraboli

- Fuente: GitHub HEAD
 - SHA: 8869301982ea829715b896bae0ecf0da6e5661bb
- Revisión exclusivamente estática: sin pruebas de ejecución en este informe.

## Feedback por indicador

| IL | Peso | Estado | Evidencia y retroalimentación |
|---|---:|---|---|
| IE 1.1.1 — Variables y tipos | 10% | INDICIO | Desafio Max/src/main/kotlin/cl/duoc/dsy1105/DesafioMax/Main.kt:4, Laboratorio 1/src/main/kotlin/cl/duoc/dsy1105/lab/LaboratorioKotlin.kt:12, Ejercicios Faciles/src/main/kotlin/cl/duoc/dsy1105/ejercicios/Ejercicios Faciles.kt:11 — Veo declaraciones de datos del dominio; revisar correspondencia de tipos y mutabilidad. |
| IE 1.1.2 — Cálculos | 10% | INDICIO | Desafio Max/src/main/kotlin/cl/duoc/dsy1105/DesafioMax/Main.kt:25, Ejercicios Faciles/src/main/kotlin/cl/duoc/dsy1105/ejercicios/Ejercicios Faciles.kt:20, petcare/src/main/kotlin/cl/duoc/dsy1105/PetCare/Main.kt:12 — Hay expresiones aritméticas; contrastar resultados con la tarifa e impuestos del caso. |
| IE 1.1.3 — Condicionales | 10% | INDICIO | Desafio Max/src/main/kotlin/cl/duoc/dsy1105/DesafioMax/Main.kt:13, Laboratorio 1/src/main/kotlin/cl/duoc/dsy1105/lab/LaboratorioKotlin.kt:4, Ejercicios Faciles/src/main/kotlin/cl/duoc/dsy1105/ejercicios/Ejercicios Faciles.kt:45 — Existen condiciones de flujo; verificar cobertura de escenarios límite. |
| IE 1.2.1 — Funciones y modularidad | 10% | INDICIO | Desafio Max/src/main/kotlin/cl/duoc/dsy1105/DesafioMax/Main.kt:12, Laboratorio 1/src/main/kotlin/cl/duoc/dsy1105/lab/LaboratorioKotlin.kt:3, Ejercicios Faciles/src/main/kotlin/cl/duoc/dsy1105/ejercicios/Ejercicios Faciles.kt:3 — Existen funciones; evaluar responsabilidad única y separación de lógica. |
| IE 1.2.2 — Colecciones | 10% | INDICIO | Desafio Max/src/main/kotlin/cl/duoc/dsy1105/DesafioMax/Main.kt:45, Ejercicios Faciles/src/main/kotlin/cl/duoc/dsy1105/ejercicios/Ejercicios Faciles.kt:141, petcare/src/main/kotlin/cl/duoc/dsy1105/PetCare/SistemaPetCare.kt:6 — Se declara una colección; comprobar que gestione las entidades del sistema. |
| IE 1.2.3 — Funciones de orden superior | 15% | INDICIO | Desafio Max/src/main/kotlin/cl/duoc/dsy1105/DesafioMax/Main.kt:107, Ejercicios Faciles/src/main/kotlin/cl/duoc/dsy1105/ejercicios/Ejercicios Faciles.kt:205, petcare/src/main/kotlin/cl/duoc/dsy1105/PetCare/SistemaPetCare.kt:32 — Se observan operaciones de colección; revisar aplicación y corrección del resultado. |
| IE 1.2.4 — Salida por consola | 5% | INDICIO | Desafio Max/src/main/kotlin/cl/duoc/dsy1105/DesafioMax/Main.kt:56, Laboratorio 1/src/main/kotlin/cl/duoc/dsy1105/lab/LaboratorioKotlin.kt:17, Ejercicios Faciles/src/main/kotlin/cl/duoc/dsy1105/ejercicios/Ejercicios Faciles.kt:4 — Existe salida de consola; revisar claridad y cobertura del informe. |
| IE 1.3.1 — Herencia | 10% | INDICIO | petcare/src/main/kotlin/cl/duoc/dsy1105/PetCare/Modelo.kt:15, Laboratorio 3/src/main/kotlin/cl/duoc/dsy1105/lab03/Main.kt:4, src/main/kotlin/cl/duoc/dsy1105/petcare/Modelo.kt:15 — Hay una clase base abierta o abstracta; verificar que tenga derivadas y reutilización. |
| IE 1.3.2 — Polimorfismo | 5% | INDICIO | petcare/src/main/kotlin/cl/duoc/dsy1105/PetCare/Modelo.kt:38, src/main/kotlin/cl/duoc/dsy1105/petcare/Modelo.kt:38 — Hay métodos sobrescritos; comprobar que cambien el comportamiento mediante polimorfismo. |
| IE 1.3.3 — Corrutinas | 10% | INDICIO | petcare/src/main/kotlin/cl/duoc/dsy1105/PetCare/SistemaPetCare.kt:26, src/main/kotlin/cl/duoc/dsy1105/petcare/SistemaPetCare.kt:26 — Existe una función suspend; verificar delay y conexión con el flujo principal. |
| IE 1.3.4 — Manejo de excepciones | 5% | NO IDENTIFICADO | No se identificó try-catch. Requiere inspección antes de poner 0. |

## Retroalimentación general
Se inspeccionaron 13 archivos Kotlin. Hay indicios en 10 de 11 indicadores. Fortalezas: revisar los indicadores con evidencia citada. Brechas prioritarias: verificar los no identificados y las reglas del caso. La revisión estática no confirma funcionamiento.

## Pendiente docente
No se ha validado funcionalidad, casos de negocio ni publicación en AVA. Los niveles 100/60/0 y nota definitiva necesitan decisión docente fundamentada.
