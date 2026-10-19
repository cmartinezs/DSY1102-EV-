# Evaluación EP1 — mr.soto

- Fuente: GitHub HEAD
 - SHA: ec6f02f113b9ff8ea4867098a34dae8a418efe54
- Revisión exclusivamente estática: sin pruebas de ejecución en este informe.

## Feedback por indicador

| IL | Peso | Estado | Evidencia y retroalimentación |
|---|---:|---|---|
| IE 1.1.1 — Variables y tipos | 10% | INDICIO | evaluaciones/src/main/kotlin/Equipo.kt:2, evaluaciones/src/main/kotlin/Main.kt:8, evaluaciones/src/main/kotlin/Usuario.kt:2 — Veo declaraciones de datos del dominio; revisar correspondencia de tipos y mutabilidad. |
| IE 1.1.2 — Cálculos | 10% | INDICIO | evaluaciones/src/main/kotlin/Main.kt:19, evaluaciones/src/main/kotlin/Validacion.kt:13 — Hay expresiones aritméticas; contrastar resultados con la tarifa e impuestos del caso. |
| IE 1.1.3 — Condicionales | 10% | INDICIO | evaluaciones/src/main/kotlin/Main.kt:24, evaluaciones/src/main/kotlin/Usuario.kt:8, evaluaciones/src/main/kotlin/Datos.kt:3 — Existen condiciones de flujo; verificar cobertura de escenarios límite. |
| IE 1.2.1 — Funciones y modularidad | 10% | INDICIO | evaluaciones/src/main/kotlin/Equipo.kt:6, evaluaciones/src/main/kotlin/Main.kt:3, evaluaciones/src/main/kotlin/Usuario.kt:6 — Existen funciones; evaluar responsabilidad única y separación de lógica. |
| IE 1.2.2 — Colecciones | 10% | INDICIO | evaluaciones/src/main/kotlin/Main.kt:46, evaluaciones/src/main/kotlin/Usuario.kt:16 — Se declara una colección; comprobar que gestione las entidades del sistema. |
| IE 1.2.3 — Funciones de orden superior | 15% | INDICIO | evaluaciones/src/main/kotlin/Main.kt:56, evaluaciones/src/main/kotlin/Usuario.kt:18 — Se observan operaciones de colección; revisar aplicación y corrección del resultado. |
| IE 1.2.4 — Salida por consola | 5% | INDICIO | evaluaciones/src/main/kotlin/Equipo.kt:7, evaluaciones/src/main/kotlin/Main.kt:5, evaluaciones/src/main/kotlin/Usuario.kt:9 — Existe salida de consola; revisar claridad y cobertura del informe. |
| IE 1.3.1 — Herencia | 10% | INDICIO | evaluaciones/src/main/kotlin/Equipo.kt:1 — Hay una clase base abierta o abstracta; verificar que tenga derivadas y reutilización. |
| IE 1.3.2 — Polimorfismo | 5% | INDICIO | evaluaciones/src/main/kotlin/Equipo.kt:17 — Hay métodos sobrescritos; comprobar que cambien el comportamiento mediante polimorfismo. |
| IE 1.3.3 — Corrutinas | 10% | NO IDENTIFICADO | No se detectó implementación completa de suspend y delay. Requiere inspección antes de poner 0. |
| IE 1.3.4 — Manejo de excepciones | 5% | INDICIO | evaluaciones/src/main/kotlin/Validacion.kt:3 — Existe try-catch; verificar recuperación real de entradas inválidas. |

## Retroalimentación general
Se inspeccionaron 6 archivos Kotlin. Hay indicios en 10 de 11 indicadores. Fortalezas: revisar los indicadores con evidencia citada. Brechas prioritarias: verificar los no identificados y las reglas del caso. La revisión estática no confirma funcionamiento.

## Pendiente docente
No se ha validado funcionalidad, casos de negocio ni publicación en AVA. Los niveles 100/60/0 y nota definitiva necesitan decisión docente fundamentada.
