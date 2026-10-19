# Evaluación EP1 — ab.puente

- Fuente: GitHub HEAD
 - SHA: 8aaac1a2c55fc4c45b2e6e1aa3ba9d20f9563fe0
- Revisión exclusivamente estática: sin pruebas de ejecución en este informe.

## Feedback por indicador

| IL | Peso | Estado | Evidencia y retroalimentación |
|---|---:|---|---|
| IE 1.1.1 — Variables y tipos | 10% | INDICIO | evaluaciones/ep1/Bicicletas.kt:4, evaluaciones/ep1/Main.kt:4, evaluaciones/ep1/Slot.kt:1 — Veo declaraciones de datos del dominio; revisar correspondencia de tipos y mutabilidad. |
| IE 1.1.2 — Cálculos | 10% | INDICIO | evaluaciones/ep1/Bicicletas.kt:17, evaluaciones/ep1/Main.kt:22, evaluaciones/ep1/Estados.kt:11 — Hay expresiones aritméticas; contrastar resultados con la tarifa e impuestos del caso. |
| IE 1.1.3 — Condicionales | 10% | INDICIO | evaluaciones/ep1/Bicicletas.kt:15, evaluaciones/ep1/Main.kt:16, evaluaciones/ep1/Estados.kt:21 — Existen condiciones de flujo; verificar cobertura de escenarios límite. |
| IE 1.2.1 — Funciones y modularidad | 10% | INDICIO | evaluaciones/ep1/Bicicletas.kt:10, evaluaciones/ep1/Main.kt:3, evaluaciones/ep1/Slot.kt:11 — Existen funciones; evaluar responsabilidad única y separación de lógica. |
| IE 1.2.2 — Colecciones | 10% | INDICIO | evaluaciones/ep1/Estados.kt:11 — Se declara una colección; comprobar que gestione las entidades del sistema. |
| IE 1.2.3 — Funciones de orden superior | 15% | INDICIO | evaluaciones/ep1/Estados.kt:20 — Se observan operaciones de colección; revisar aplicación y corrección del resultado. |
| IE 1.2.4 — Salida por consola | 5% | INDICIO | evaluaciones/ep1/Main.kt:7, evaluaciones/ep1/Estados.kt:22 — Existe salida de consola; revisar claridad y cobertura del informe. |
| IE 1.3.1 — Herencia | 10% | INDICIO | evaluaciones/ep1/Bicicletas.kt:3 — Hay una clase base abierta o abstracta; verificar que tenga derivadas y reutilización. |
| IE 1.3.2 — Polimorfismo | 5% | INDICIO | evaluaciones/ep1/Bicicletas.kt:34 — Hay métodos sobrescritos; comprobar que cambien el comportamiento mediante polimorfismo. |
| IE 1.3.3 — Corrutinas | 10% | NO IDENTIFICADO | No se detectó implementación completa de suspend y delay. Requiere inspección antes de poner 0. |
| IE 1.3.4 — Manejo de excepciones | 5% | NO IDENTIFICADO | No se identificó try-catch. Requiere inspección antes de poner 0. |

## Retroalimentación general
Se inspeccionaron 5 archivos Kotlin. Hay indicios en 9 de 11 indicadores. Fortalezas: revisar los indicadores con evidencia citada. Brechas prioritarias: verificar los no identificados y las reglas del caso. La revisión estática no confirma funcionamiento.

## Pendiente docente
No se ha validado funcionalidad, casos de negocio ni publicación en AVA. Los niveles 100/60/0 y nota definitiva necesitan decisión docente fundamentada.
