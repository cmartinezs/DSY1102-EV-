# Evaluación EP1 — cla.jaime

- Fuente: GitHub HEAD
 - SHA: 2d1057df2b99acedea32da20477ec36ccb7d0ffe
- Revisión exclusivamente estática: sin pruebas de ejecución en este informe.

## Feedback por indicador

| IL | Peso | Estado | Evidencia y retroalimentación |
|---|---:|---|---|
| IE 1.1.1 — Variables y tipos | 10% | INDICIO | Ev1_FormaE/Pet-Care/src/main/kotlin/PetCare.kt:3, Ev1_FormaE/Pet-Care/src/main/kotlin/main.kt:2, Ev1_FormaE/Pet-Care/src/main/kotlin/Ticket.kt:2 — Veo declaraciones de datos del dominio; revisar correspondencia de tipos y mutabilidad. |
| IE 1.1.2 — Cálculos | 10% | INDICIO | Ev1_FormaE/Pet-Care/src/main/kotlin/PetCare.kt:125, Ev1_FormaE/Pet-Care/src/main/kotlin/main.kt:8, Ev1_FormaE/Pet-Care/src/main/kotlin/Box.kt:10 — Hay expresiones aritméticas; contrastar resultados con la tarifa e impuestos del caso. |
| IE 1.1.3 — Condicionales | 10% | INDICIO | Ev1_FormaE/Pet-Care/src/main/kotlin/PetCare.kt:20, Ev1_FormaE/Pet-Care/src/main/kotlin/Box.kt:12, Ev1_FormaE/Pet-Care/src/main/kotlin/Exotico.kt:16 — Existen condiciones de flujo; verificar cobertura de escenarios límite. |
| IE 1.2.1 — Funciones y modularidad | 10% | INDICIO | Ev1_FormaE/Pet-Care/src/main/kotlin/PetCare.kt:16, Ev1_FormaE/Pet-Care/src/main/kotlin/main.kt:1, Ev1_FormaE/Pet-Care/src/main/kotlin/Ticket.kt:9 — Existen funciones; evaluar responsabilidad única y separación de lógica. |
| IE 1.2.2 — Colecciones | 10% | NO IDENTIFICADO | No se identificó colección List/Map. Requiere inspección antes de poner 0. |
| IE 1.2.3 — Funciones de orden superior | 15% | NO IDENTIFICADO | No se identificaron funciones de orden superior. Requiere inspección antes de poner 0. |
| IE 1.2.4 — Salida por consola | 5% | INDICIO | Ev1_FormaE/Pet-Care/src/main/kotlin/PetCare.kt:42, Ev1_FormaE/Pet-Care/src/main/kotlin/main.kt:54, Ev1_FormaE/Pet-Care/src/main/kotlin/Ticket.kt:10 — Existe salida de consola; revisar claridad y cobertura del informe. |
| IE 1.3.1 — Herencia | 10% | INDICIO | Ev1_FormaE/Pet-Care/src/main/kotlin/Paciente.kt:1 — Hay una clase base abierta o abstracta; verificar que tenga derivadas y reutilización. |
| IE 1.3.2 — Polimorfismo | 5% | INDICIO | Ev1_FormaE/Pet-Care/src/main/kotlin/Exotico.kt:10, Ev1_FormaE/Pet-Care/src/main/kotlin/Felino.kt:7, Ev1_FormaE/Pet-Care/src/main/kotlin/Canino.kt:8 — Hay métodos sobrescritos; comprobar que cambien el comportamiento mediante polimorfismo. |
| IE 1.3.3 — Corrutinas | 10% | NO IDENTIFICADO | No se detectó implementación completa de suspend y delay. Requiere inspección antes de poner 0. |
| IE 1.3.4 — Manejo de excepciones | 5% | NO IDENTIFICADO | No se identificó try-catch. Requiere inspección antes de poner 0. |

## Retroalimentación general
Se inspeccionaron 8 archivos Kotlin. Hay indicios en 7 de 11 indicadores. Fortalezas: revisar los indicadores con evidencia citada. Brechas prioritarias: verificar los no identificados y las reglas del caso. La revisión estática no confirma funcionamiento.

## Pendiente docente
No se ha validado funcionalidad, casos de negocio ni publicación en AVA. Los niveles 100/60/0 y nota definitiva necesitan decisión docente fundamentada.
