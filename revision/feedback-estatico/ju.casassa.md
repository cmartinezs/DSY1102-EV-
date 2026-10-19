# Evaluación EP1 — ju.casassa

- Fuente: GitHub HEAD
 - SHA: 0155497664cab3b19bff63cfb52e36c037aeac90
- Revisión exclusivamente estática: sin pruebas de ejecución en este informe.

## Feedback por indicador

| IL | Peso | Estado | Evidencia y retroalimentación |
|---|---:|---|---|
| IE 1.1.1 — Variables y tipos | 10% | INDICIO | Examenes/AplicacionesMovilesParcial1/PetCare/src/main/kotlin/Main.kt:11, Examenes/AplicacionesMovilesParcial1/PetCare/src/main/kotlin/modelos/Veterinaria.kt:4, Examenes/AplicacionesMovilesParcial1/PetCare/src/main/kotlin/modelos/Box.kt:4 — Veo declaraciones de datos del dominio; revisar correspondencia de tipos y mutabilidad. |
| IE 1.1.2 — Cálculos | 10% | INDICIO | Examenes/AplicacionesMovilesParcial1/PetCare/src/main/kotlin/Main.kt:137, Examenes/AplicacionesMovilesParcial1/PetCare/src/main/kotlin/modelos/Tarifa.kt:12 — Hay expresiones aritméticas; contrastar resultados con la tarifa e impuestos del caso. |
| IE 1.1.3 — Condicionales | 10% | INDICIO | Examenes/AplicacionesMovilesParcial1/PetCare/src/main/kotlin/Main.kt:56, Examenes/AplicacionesMovilesParcial1/PetCare/src/main/kotlin/modelos/Veterinaria.kt:15, Examenes/AplicacionesMovilesParcial1/PetCare/src/main/kotlin/modelos/Tarifa.kt:8 — Existen condiciones de flujo; verificar cobertura de escenarios límite. |
| IE 1.2.1 — Funciones y modularidad | 10% | INDICIO | Examenes/AplicacionesMovilesParcial1/PetCare/src/main/kotlin/Main.kt:7, Examenes/AplicacionesMovilesParcial1/PetCare/src/main/kotlin/modelos/Veterinaria.kt:12, Examenes/AplicacionesMovilesParcial1/PetCare/src/main/kotlin/modelos/Tarifa.kt:7 — Existen funciones; evaluar responsabilidad única y separación de lógica. |
| IE 1.2.2 — Colecciones | 10% | INDICIO | Examenes/AplicacionesMovilesParcial1/PetCare/src/main/kotlin/Main.kt:36, Examenes/AplicacionesMovilesParcial1/PetCare/src/main/kotlin/modelos/Veterinaria.kt:4 — Se declara una colección; comprobar que gestione las entidades del sistema. |
| IE 1.2.3 — Funciones de orden superior | 15% | NO IDENTIFICADO | No se identificaron funciones de orden superior. Requiere inspección antes de poner 0. |
| IE 1.2.4 — Salida por consola | 5% | INDICIO | Examenes/AplicacionesMovilesParcial1/PetCare/src/main/kotlin/Main.kt:8 — Existe salida de consola; revisar claridad y cobertura del informe. |
| IE 1.3.1 — Herencia | 10% | NO IDENTIFICADO | No se identificó clase base abierta o abstracta. Requiere inspección antes de poner 0. |
| IE 1.3.2 — Polimorfismo | 5% | NO IDENTIFICADO | No se identificó sobrescritura de métodos. Requiere inspección antes de poner 0. |
| IE 1.3.3 — Corrutinas | 10% | NO IDENTIFICADO | No se detectó implementación completa de suspend y delay. Requiere inspección antes de poner 0. |
| IE 1.3.4 — Manejo de excepciones | 5% | NO IDENTIFICADO | No se identificó try-catch. Requiere inspección antes de poner 0. |

## Retroalimentación general
Se inspeccionaron 8 archivos Kotlin. Hay indicios en 6 de 11 indicadores. Fortalezas: revisar los indicadores con evidencia citada. Brechas prioritarias: verificar los no identificados y las reglas del caso. La revisión estática no confirma funcionamiento.

## Pendiente docente
No se ha validado funcionalidad, casos de negocio ni publicación en AVA. Los niveles 100/60/0 y nota definitiva necesitan decisión docente fundamentada.
