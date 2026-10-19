# Evaluación EP1 — ca.pinillag

- Fuente: GitHub HEAD
 - SHA: 28d788bcd15491c51dfc2915aae716fe1a9df5d0
- Revisión exclusivamente estática: sin pruebas de ejecución en este informe.

## Feedback por indicador

| IL | Peso | Estado | Evidencia y retroalimentación |
|---|---:|---|---|
| IE 1.1.1 — Variables y tipos | 10% | INDICIO | src/Main.kt:11, src/model/EstadoSlot.kt:6, src/model/Bicicleta.kt:6 — Veo declaraciones de datos del dominio; revisar correspondencia de tipos y mutabilidad. |
| IE 1.1.2 — Cálculos | 10% | INDICIO | src/Main.kt:16, src/model/Bicicleta.kt:30, src/service/BikeCityService.kt:8 — Hay expresiones aritméticas; contrastar resultados con la tarifa e impuestos del caso. |
| IE 1.1.3 — Condicionales | 10% | INDICIO | src/Main.kt:59, src/model/Bicicleta.kt:27, src/service/BikeCityService.kt:39 — Existen condiciones de flujo; verificar cobertura de escenarios límite. |
| IE 1.2.1 — Funciones y modularidad | 10% | INDICIO | src/Main.kt:6, src/model/Bicicleta.kt:12, src/service/BikeCityService.kt:26 — Existen funciones; evaluar responsabilidad única y separación de lógica. |
| IE 1.2.2 — Colecciones | 10% | INDICIO | src/service/BikeCityService.kt:8 — Se declara una colección; comprobar que gestione las entidades del sistema. |
| IE 1.2.3 — Funciones de orden superior | 15% | INDICIO | src/Main.kt:48, src/service/BikeCityService.kt:47 — Se observan operaciones de colección; revisar aplicación y corrección del resultado. |
| IE 1.2.4 — Salida por consola | 5% | INDICIO | src/Main.kt:8, src/service/BikeCityService.kt:52 — Existe salida de consola; revisar claridad y cobertura del informe. |
| IE 1.3.1 — Herencia | 10% | INDICIO | src/model/Bicicleta.kt:5 — Hay una clase base abierta o abstracta; verificar que tenga derivadas y reutilización. |
| IE 1.3.2 — Polimorfismo | 5% | INDICIO | src/model/Bicicleta.kt:25 — Hay métodos sobrescritos; comprobar que cambien el comportamiento mediante polimorfismo. |
| IE 1.3.3 — Corrutinas | 10% | INDICIO | src/service/BikeCityService.kt:38 — Existe una función suspend; verificar delay y conexión con el flujo principal. |
| IE 1.3.4 — Manejo de excepciones | 5% | NO IDENTIFICADO | No se identificó try-catch. Requiere inspección antes de poner 0. |

## Retroalimentación general
Se inspeccionaron 6 archivos Kotlin. Hay indicios en 10 de 11 indicadores. Fortalezas: revisar los indicadores con evidencia citada. Brechas prioritarias: verificar los no identificados y las reglas del caso. La revisión estática no confirma funcionamiento.

## Pendiente docente
No se ha validado funcionalidad, casos de negocio ni publicación en AVA. Los niveles 100/60/0 y nota definitiva necesitan decisión docente fundamentada.
