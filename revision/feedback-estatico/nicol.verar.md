# Evaluación EP1 — nicol.verar

- Fuente: ZIP
 - SHA: 
- Revisión exclusivamente estática: sin pruebas de ejecución en este informe.

## Feedback por indicador

| IL | Peso | Estado | Evidencia y retroalimentación |
|---|---:|---|---|
| IE 1.1.1 — Variables y tipos | 10% | INDICIO | sadas/Nicolas_Vera/src/main/kotlin/Bicicleta.kt:15, sadas/Nicolas_Vera/src/main/kotlin/BikeCitySistema.kt:4, sadas/Nicolas_Vera/src/main/kotlin/Main.kt:4 — Veo declaraciones de datos del dominio; revisar correspondencia de tipos y mutabilidad. |
| IE 1.1.2 — Cálculos | 10% | INDICIO | sadas/Nicolas_Vera/src/main/kotlin/Bicicleta.kt:39, sadas/Nicolas_Vera/src/main/kotlin/BikeCitySistema.kt:7, sadas/Nicolas_Vera/src/main/kotlin/Main.kt:8 — Hay expresiones aritméticas; contrastar resultados con la tarifa e impuestos del caso. |
| IE 1.1.3 — Condicionales | 10% | INDICIO | sadas/Nicolas_Vera/src/main/kotlin/Bicicleta.kt:55, sadas/Nicolas_Vera/src/main/kotlin/BikeCitySistema.kt:22, sadas/Nicolas_Vera/src/main/kotlin/Main.kt:15 — Existen condiciones de flujo; verificar cobertura de escenarios límite. |
| IE 1.2.1 — Funciones y modularidad | 10% | INDICIO | sadas/Nicolas_Vera/src/main/kotlin/Bicicleta.kt:24, sadas/Nicolas_Vera/src/main/kotlin/BikeCitySistema.kt:15, sadas/Nicolas_Vera/src/main/kotlin/Main.kt:3 — Existen funciones; evaluar responsabilidad única y separación de lógica. |
| IE 1.2.2 — Colecciones | 10% | INDICIO | sadas/Nicolas_Vera/src/main/kotlin/BikeCitySistema.kt:9 — Se declara una colección; comprobar que gestione las entidades del sistema. |
| IE 1.2.3 — Funciones de orden superior | 15% | INDICIO | sadas/Nicolas_Vera/src/main/kotlin/BikeCitySistema.kt:78, sadas/Nicolas_Vera/src/main/kotlin/Main.kt:118 — Se observan operaciones de colección; revisar aplicación y corrección del resultado. |
| IE 1.2.4 — Salida por consola | 5% | INDICIO | sadas/Nicolas_Vera/src/main/kotlin/BikeCitySistema.kt:33, sadas/Nicolas_Vera/src/main/kotlin/Main.kt:7 — Existe salida de consola; revisar claridad y cobertura del informe. |
| IE 1.3.1 — Herencia | 10% | INDICIO | sadas/Nicolas_Vera/src/main/kotlin/Bicicleta.kt:14 — Hay una clase base abierta o abstracta; verificar que tenga derivadas y reutilización. |
| IE 1.3.2 — Polimorfismo | 5% | INDICIO | sadas/Nicolas_Vera/src/main/kotlin/Bicicleta.kt:52 — Hay métodos sobrescritos; comprobar que cambien el comportamiento mediante polimorfismo. |
| IE 1.3.3 — Corrutinas | 10% | INDICIO | sadas/Nicolas_Vera/src/main/kotlin/BikeCitySistema.kt:21, sadas/Nicolas_Vera/src/main/kotlin/Main.kt:47 — Existe una función suspend; verificar delay y conexión con el flujo principal. |
| IE 1.3.4 — Manejo de excepciones | 5% | INDICIO | sadas/Nicolas_Vera/src/main/kotlin/Main.kt:48 — Existe try-catch; verificar recuperación real de entradas inválidas. |

## Retroalimentación general
Se inspeccionaron 6 archivos Kotlin. Hay indicios en 11 de 11 indicadores. Fortalezas: revisar los indicadores con evidencia citada. Brechas prioritarias: verificar los no identificados y las reglas del caso. La revisión estática no confirma funcionamiento.

## Pendiente docente
No se ha validado funcionalidad, casos de negocio ni publicación en AVA. Los niveles 100/60/0 y nota definitiva necesitan decisión docente fundamentada.
