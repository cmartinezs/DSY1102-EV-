# Evaluación EP1 — cr.menesesn

- Fuente: GitHub HEAD
 - SHA: e286de3a3c6f1e40486637f5a6c8dab5fd0e7d98
- Revisión exclusivamente estática: sin pruebas de ejecución en este informe.

## Feedback por indicador

| IL | Peso | Estado | Evidencia y retroalimentación |
|---|---:|---|---|
| IE 1.1.1 — Variables y tipos | 10% | INDICIO | src/main/kotlin/Bicicletas.kt:10, src/main/kotlin/Main.kt:5, src/main/kotlin/BikeCity.kt:1 — Veo declaraciones de datos del dominio; revisar correspondencia de tipos y mutabilidad. |
| IE 1.1.2 — Cálculos | 10% | INDICIO | src/main/kotlin/Bicicletas.kt:16, src/main/kotlin/Main.kt:39, src/main/kotlin/BikeCity.kt:2 — Hay expresiones aritméticas; contrastar resultados con la tarifa e impuestos del caso. |
| IE 1.1.3 — Condicionales | 10% | INDICIO | src/main/kotlin/Bicicletas.kt:17, src/main/kotlin/BikeCity.kt:9 — Existen condiciones de flujo; verificar cobertura de escenarios límite. |
| IE 1.2.1 — Funciones y modularidad | 10% | INDICIO | src/main/kotlin/Bicicletas.kt:24, src/main/kotlin/Main.kt:3, src/main/kotlin/BikeCity.kt:6 — Existen funciones; evaluar responsabilidad única y separación de lógica. |
| IE 1.2.2 — Colecciones | 10% | INDICIO | src/main/kotlin/BikeCity.kt:3 — Se declara una colección; comprobar que gestione las entidades del sistema. |
| IE 1.2.3 — Funciones de orden superior | 15% | INDICIO | src/main/kotlin/Main.kt:46, src/main/kotlin/BikeCity.kt:86 — Se observan operaciones de colección; revisar aplicación y corrección del resultado. |
| IE 1.2.4 — Salida por consola | 5% | INDICIO | src/main/kotlin/Main.kt:4, src/main/kotlin/BikeCity.kt:32 — Existe salida de consola; revisar claridad y cobertura del informe. |
| IE 1.3.1 — Herencia | 10% | INDICIO | src/main/kotlin/Bicicletas.kt:9 — Hay una clase base abierta o abstracta; verificar que tenga derivadas y reutilización. |
| IE 1.3.2 — Polimorfismo | 5% | INDICIO | src/main/kotlin/Bicicletas.kt:39 — Hay métodos sobrescritos; comprobar que cambien el comportamiento mediante polimorfismo. |
| IE 1.3.3 — Corrutinas | 10% | NO IDENTIFICADO | No se detectó implementación completa de suspend y delay. Requiere inspección antes de poner 0. |
| IE 1.3.4 — Manejo de excepciones | 5% | INDICIO | src/main/kotlin/Main.kt:9, src/main/kotlin/BikeCity.kt:68 — Existe try-catch; verificar recuperación real de entradas inválidas. |

## Retroalimentación general
Se inspeccionaron 5 archivos Kotlin. Hay indicios en 10 de 11 indicadores. Fortalezas: revisar los indicadores con evidencia citada. Brechas prioritarias: verificar los no identificados y las reglas del caso. La revisión estática no confirma funcionamiento.

## Pendiente docente
No se ha validado funcionalidad, casos de negocio ni publicación en AVA. Los niveles 100/60/0 y nota definitiva necesitan decisión docente fundamentada.
