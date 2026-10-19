# Evaluación EP1 — enz.rojas

- Fuente: GitHub HEAD
 - SHA: d867b64d24d53278cc8fba8437de20cd9c8b7139
- Revisión exclusivamente estática: sin pruebas de ejecución en este informe.

## Feedback por indicador

| IL | Peso | Estado | Evidencia y retroalimentación |
|---|---:|---|---|
| IE 1.1.1 — Variables y tipos | 10% | INDICIO | evaluaciones/ep1/src/main/kotlin/Main.kt:4, evaluaciones/ep1/src/main/kotlin/SistemaBikeCity.kt:3, evaluaciones/ep1/src/main/kotlin/Modelo.kt:7 — Veo declaraciones de datos del dominio; revisar correspondencia de tipos y mutabilidad. |
| IE 1.1.2 — Cálculos | 10% | INDICIO | evaluaciones/ep1/src/main/kotlin/SistemaBikeCity.kt:6, evaluaciones/ep1/src/main/kotlin/Modelo.kt:19 — Hay expresiones aritméticas; contrastar resultados con la tarifa e impuestos del caso. |
| IE 1.1.3 — Condicionales | 10% | INDICIO | evaluaciones/ep1/src/main/kotlin/SistemaBikeCity.kt:13, evaluaciones/ep1/src/main/kotlin/Modelo.kt:20 — Existen condiciones de flujo; verificar cobertura de escenarios límite. |
| IE 1.2.1 — Funciones y modularidad | 10% | INDICIO | evaluaciones/ep1/src/main/kotlin/Main.kt:3, evaluaciones/ep1/src/main/kotlin/SistemaBikeCity.kt:10, evaluaciones/ep1/src/main/kotlin/Modelo.kt:25 — Existen funciones; evaluar responsabilidad única y separación de lógica. |
| IE 1.2.2 — Colecciones | 10% | INDICIO | evaluaciones/ep1/src/main/kotlin/SistemaBikeCity.kt:6 — Se declara una colección; comprobar que gestione las entidades del sistema. |
| IE 1.2.3 — Funciones de orden superior | 15% | INDICIO | evaluaciones/ep1/src/main/kotlin/SistemaBikeCity.kt:51 — Se observan operaciones de colección; revisar aplicación y corrección del resultado. |
| IE 1.2.4 — Salida por consola | 5% | INDICIO | evaluaciones/ep1/src/main/kotlin/Main.kt:6, evaluaciones/ep1/src/main/kotlin/SistemaBikeCity.kt:14 — Existe salida de consola; revisar claridad y cobertura del informe. |
| IE 1.3.1 — Herencia | 10% | INDICIO | evaluaciones/ep1/src/main/kotlin/Modelo.kt:12 — Hay una clase base abierta o abstracta; verificar que tenga derivadas y reutilización. |
| IE 1.3.2 — Polimorfismo | 5% | INDICIO | evaluaciones/ep1/src/main/kotlin/Modelo.kt:47 — Hay métodos sobrescritos; comprobar que cambien el comportamiento mediante polimorfismo. |
| IE 1.3.3 — Corrutinas | 10% | INDICIO | evaluaciones/ep1/src/main/kotlin/SistemaBikeCity.kt:10 — Existe una función suspend; verificar delay y conexión con el flujo principal. |
| IE 1.3.4 — Manejo de excepciones | 5% | INDICIO | evaluaciones/ep1/src/main/kotlin/Main.kt:9 — Existe try-catch; verificar recuperación real de entradas inválidas. |

## Retroalimentación general
Se inspeccionaron 3 archivos Kotlin. Hay indicios en 11 de 11 indicadores. Fortalezas: revisar los indicadores con evidencia citada. Brechas prioritarias: verificar los no identificados y las reglas del caso. La revisión estática no confirma funcionamiento.

## Pendiente docente
No se ha validado funcionalidad, casos de negocio ni publicación en AVA. Los niveles 100/60/0 y nota definitiva necesitan decisión docente fundamentada.
