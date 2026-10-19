# Evaluación EP1 — mi.gonzalezva

- Fuente: ZIP
 - SHA: 
- Revisión exclusivamente estática: sin pruebas de ejecución en este informe.

## Feedback por indicador

| IL | Peso | Estado | Evidencia y retroalimentación |
|---|---:|---|---|
| IE 1.1.1 — Variables y tipos | 10% | INDICIO | MartinIgnacioGonzalezVarela_FormaD/MartinIgnacioGonzalezVarela_FormaD/src/cl/duoc/mi/gonzalezva/Main.kt:8, MartinIgnacioGonzalezVarela_FormaD/MartinIgnacioGonzalezVarela_FormaD/src/cl/duoc/mi/gonzalezva/Service/SistemaBikeCity.kt:8, MartinIgnacioGonzalezVarela_FormaD/MartinIgnacioGonzalezVarela_FormaD/src/cl/duoc/migonzalezva/Model/EstadoSlot.kt:9 — Veo declaraciones de datos del dominio; revisar correspondencia de tipos y mutabilidad. |
| IE 1.1.2 — Cálculos | 10% | INDICIO | MartinIgnacioGonzalezVarela_FormaD/MartinIgnacioGonzalezVarela_FormaD/src/cl/duoc/mi/gonzalezva/Service/SistemaBikeCity.kt:8, MartinIgnacioGonzalezVarela_FormaD/MartinIgnacioGonzalezVarela_FormaD/src/cl/duoc/migonzalezva/Model/Bicicleta.kt:15 — Hay expresiones aritméticas; contrastar resultados con la tarifa e impuestos del caso. |
| IE 1.1.3 — Condicionales | 10% | INDICIO | MartinIgnacioGonzalezVarela_FormaD/MartinIgnacioGonzalezVarela_FormaD/src/cl/duoc/mi/gonzalezva/Service/SistemaBikeCity.kt:57, MartinIgnacioGonzalezVarela_FormaD/MartinIgnacioGonzalezVarela_FormaD/src/cl/duoc/migonzalezva/Model/Bicicleta.kt:16 — Existen condiciones de flujo; verificar cobertura de escenarios límite. |
| IE 1.2.1 — Funciones y modularidad | 10% | INDICIO | MartinIgnacioGonzalezVarela_FormaD/MartinIgnacioGonzalezVarela_FormaD/src/cl/duoc/mi/gonzalezva/Main.kt:7, MartinIgnacioGonzalezVarela_FormaD/MartinIgnacioGonzalezVarela_FormaD/src/cl/duoc/mi/gonzalezva/Service/SistemaBikeCity.kt:14, MartinIgnacioGonzalezVarela_FormaD/MartinIgnacioGonzalezVarela_FormaD/src/cl/duoc/migonzalezva/Model/EstadoSlot.kt:7 — Existen funciones; evaluar responsabilidad única y separación de lógica. |
| IE 1.2.2 — Colecciones | 10% | INDICIO | MartinIgnacioGonzalezVarela_FormaD/MartinIgnacioGonzalezVarela_FormaD/src/cl/duoc/mi/gonzalezva/Service/SistemaBikeCity.kt:8 — Se declara una colección; comprobar que gestione las entidades del sistema. |
| IE 1.2.3 — Funciones de orden superior | 15% | INDICIO | MartinIgnacioGonzalezVarela_FormaD/MartinIgnacioGonzalezVarela_FormaD/src/cl/duoc/mi/gonzalezva/Service/SistemaBikeCity.kt:50 — Se observan operaciones de colección; revisar aplicación y corrección del resultado. |
| IE 1.2.4 — Salida por consola | 5% | INDICIO | MartinIgnacioGonzalezVarela_FormaD/MartinIgnacioGonzalezVarela_FormaD/src/cl/duoc/mi/gonzalezva/Main.kt:10, MartinIgnacioGonzalezVarela_FormaD/MartinIgnacioGonzalezVarela_FormaD/src/cl/duoc/mi/gonzalezva/Service/SistemaBikeCity.kt:19 — Existe salida de consola; revisar claridad y cobertura del informe. |
| IE 1.3.1 — Herencia | 10% | INDICIO | MartinIgnacioGonzalezVarela_FormaD/MartinIgnacioGonzalezVarela_FormaD/src/cl/duoc/mi/gonzalezva/exception/BikeCityExceptions.kt:3, MartinIgnacioGonzalezVarela_FormaD/MartinIgnacioGonzalezVarela_FormaD/src/cl/duoc/migonzalezva/Model/Bicicleta.kt:8 — Hay una clase base abierta o abstracta; verificar que tenga derivadas y reutilización. |
| IE 1.3.2 — Polimorfismo | 5% | INDICIO | MartinIgnacioGonzalezVarela_FormaD/MartinIgnacioGonzalezVarela_FormaD/src/cl/duoc/migonzalezva/Model/EstadoSlot.kt:7, MartinIgnacioGonzalezVarela_FormaD/MartinIgnacioGonzalezVarela_FormaD/src/cl/duoc/migonzalezva/Model/Bicicleta.kt:53 — Hay métodos sobrescritos; comprobar que cambien el comportamiento mediante polimorfismo. |
| IE 1.3.3 — Corrutinas | 10% | INDICIO | MartinIgnacioGonzalezVarela_FormaD/MartinIgnacioGonzalezVarela_FormaD/src/cl/duoc/mi/gonzalezva/Service/SistemaBikeCity.kt:14 — Existe una función suspend; verificar delay y conexión con el flujo principal. |
| IE 1.3.4 — Manejo de excepciones | 5% | INDICIO | MartinIgnacioGonzalezVarela_FormaD/MartinIgnacioGonzalezVarela_FormaD/src/cl/duoc/mi/gonzalezva/Main.kt:12 — Existe try-catch; verificar recuperación real de entradas inválidas. |

## Retroalimentación general
Se inspeccionaron 9 archivos Kotlin. Hay indicios en 11 de 11 indicadores. Fortalezas: revisar los indicadores con evidencia citada. Brechas prioritarias: verificar los no identificados y las reglas del caso. La revisión estática no confirma funcionamiento.

## Pendiente docente
No se ha validado funcionalidad, casos de negocio ni publicación en AVA. Los niveles 100/60/0 y nota definitiva necesitan decisión docente fundamentada.
