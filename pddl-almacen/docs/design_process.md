# Proceso de diseño del dominio `almacen-automatizado`

Documento de autoría: explica qué se modeló, por qué se eligieron esos predicados y acciones, cómo se llegó al esquema final de cada acción y en qué se diferencia el dominio de los que sirvieron de inspiración.

## 1. Escenario elegido

**Almacén automatizado con zonas restringidas.** Un robot montacargas recibe lotes de mercancía en la zona de recepción y debe dejarlos en estantes específicos. Antes de almacenar, cada lote debe pasar por inspección, y los pasillos de estantería están bloqueados: se abren con tarjetas de acceso que se recogen en seguridad. El flujo real es:

```
recepción → inspección (lote apoyado en la mesa) → pasillo restringido (tarjeta) → estante
```

Se eligió porque (a) combina movimiento, una dependencia de orden (inspeccionar antes de almacenar) y un recurso consumible (tarjetas de un solo uso), (b) el manipulador único del robot genera conflictos reales entre acciones, y (c) es fácil de explicar acción por acción en el video.

## 2. Dominios de inspiración y diferencias

| Dominio de inspiración | Qué se tomó | Qué es distinto en este dominio |
|---|---|---|
| **Air Cargo** | La idea de transportar objetos entre ubicaciones conectadas hacia un destino final. | En Air Cargo basta con cargar, volar y descargar. Aquí el movimiento está **condicionado por permisos**: dos zonas no se pueden pisar hasta desbloquearlas, y el desbloqueo consume un objeto (la tarjeta). Además, el lote debe cumplir un requisito de calidad (inspección) antes de llegar a su destino. Un solo robot sin capacidad de varios lotes, en lugar de aviones. |
| **Blocks World** | El manipulador exclusivo: `manos-libres` juega el papel de `handempty`, y `recoger` / `soltar` equivalen a `pick-up` / `put-down`. | No hay apilamiento ni torres. La restricción del manipulador se usa para algo distinto: **inspeccionar y tomar tarjetas exige tener las manos libres**, así que el robot debe soltar el lote en la mesa de inspección para poder inspeccionarlo, y eso ordena el plan. |

**Elementos que no existen en ninguno de los dos:**

1. **Zonas restringidas con tarjetas de un solo uso**: `desbloquear-zona` consume `tiene-tarjeta` y cada tarjeta abre una zona concreta (`tarjeta-de`). Se desbloquea desde una zona vecina, y existen dos acciones de movimiento distintas según la zona sea libre o restringida.
2. **Inspección obligatoria con requisito de postura**: solo en una zona con mesa de inspección, con el lote depositado y el robot con las manos libres.
3. **Estantes de capacidad 1 con destino asignado por lote** (`destino`), de modo que no basta con llegar a cualquier estante.

## 3. Predicados definidos (16) y por qué

| Grupo | Predicado | Para qué existe |
|---|---|---|
| Topología y acceso | `conectada ?a ?b` | Define por dónde puede moverse el robot (estático). |
| | `zona-libre ?z` | Marca zonas sin restricción; `mover` solo entra a estas (estático). |
| | `zona-desbloqueada ?z` | Estado dinámico: una zona restringida ya abierta; `mover-restringida` lo exige. |
| | `zona-inspeccion ?z` | Solo ahí se puede inspeccionar (estático). |
| | `tarjeta-de ?t ?z` | Qué zona abre cada tarjeta (estático). |
| Estantes | `estante-en ?e ?z` | Ubicación fija del estante (estático). |
| | `estante-vacio ?e` | Capacidad 1: se ocupa al almacenar. |
| | `destino ?l ?e` | Estante asignado a cada lote (estático). |
| Robot | `robot-en ?r ?z` | Posición del robot. |
| | `manos-libres ?r` | El manipulador está disponible. |
| | `cargando ?r ?l` | El robot lleva ese lote. |
| | `tiene-tarjeta ?r ?t` | El robot porta una tarjeta sin usar. |
| Lotes y tarjetas | `lote-en ?l ?z` | Lote depositado en una zona (no aplica mientras se carga). |
| | `lote-inspeccionado ?l` | Se usa un predicado positivo, no uno de "pendiente", porque no se emplean precondiciones negativas. |
| | `lote-almacenado ?l ?e` | Efecto final que usa la meta. |
| | `tarjeta-en ?t ?z` | Tarjeta disponible para recoger. |

Se usan **cinco tipos** (`zona`, `robot`, `lote`, `tarjeta`, `estante`) para que cada acción solo pueda aplicarse a objetos del tipo correcto y reducir el número de operadores instanciados (60 en este problema).

## 4. Acciones (8) y cómo se llegó al esquema final

| # | Acción | Precondiciones | Agrega | Elimina |
|---|---|---|---|---|
| 1 | `mover` | `robot-en`, `conectada`, `zona-libre` (destino) | `robot-en` destino | `robot-en` origen |
| 2 | `mover-restringida` | `robot-en`, `conectada`, `zona-desbloqueada` (destino) | `robot-en` destino | `robot-en` origen |
| 3 | `tomar-tarjeta` | `robot-en`, `tarjeta-en`, `manos-libres` | `tiene-tarjeta` | `tarjeta-en` |
| 4 | `desbloquear-zona` | `robot-en`, `conectada`, `tiene-tarjeta`, `tarjeta-de` | `zona-desbloqueada` | **`tiene-tarjeta`** |
| 5 | `recoger` | `robot-en`, `lote-en`, `manos-libres` | `cargando` | `lote-en`, `manos-libres` |
| 6 | `soltar` | `robot-en`, `cargando` | `lote-en`, `manos-libres` | `cargando` |
| 7 | `inspeccionar-lote` | `robot-en`, `zona-inspeccion`, `lote-en`, **`manos-libres`** | `lote-inspeccionado` | — |
| 8 | `almacenar` | `robot-en`, `cargando`, `estante-en`, `estante-vacio`, `destino`, **`lote-inspeccionado`** | `lote-almacenado`, `manos-libres` | `cargando`, `estante-vacio` |

### Decisiones de modelado y alternativas descartadas

- **Dos acciones de movimiento (`mover` y `mover-restringida`) en lugar de una con precondición negativa o disyuntiva.** Con una sola acción habría que escribir "la zona es libre **o** está desbloqueada", y la disyunción no es STRIPS. Dos acciones lo resuelven sin salir del subconjunto básico.
- **El lote cargado no tiene una ubicación propia mientras se transporta.** Solo existen `lote-en` (depositado) y `cargando` (en las horquillas). Así `mover` sirve igual con o sin carga, en vez de duplicar el movimiento (`mover` y `mover-con-lote`) como se haría en Air Cargo.
- **Tarjetas de un solo uso** (`desbloquear-zona` elimina `tiene-tarjeta`). Se consideró que la tarjeta fuera permanente, pero entonces la restricción solo agregaría un viaje a seguridad. Consumirla hace que cada zona cueste una acción de desbloqueo y obliga a recoger una tarjeta por zona.
- **Desbloquear desde una zona vecina** (`conectada ?de ?z`) en lugar de desde cualquier lugar: así el pasillo B solo puede abrirse estando ya dentro del pasillo A, y el orden de las zonas importa.
- **`tomar-tarjeta` e `inspeccionar-lote` exigen `manos-libres`.** Sin esa precondición el robot podría inspeccionar con el lote en las horquillas y desaparecería la acción de soltar en la mesa.
- **Sin precondiciones negativas ni efectos condicionales**, para que el dominio funcione en planificadores STRIPS sencillos.
- **Tipos explícitos para tarjeta y estante**, aunque podrían ser constantes, para que la gramática de cada acción deje claro qué objeto recibe cada parámetro.

## 5. Problema `turno-manana`

- **Objetos:** 6 zonas, 1 robot, 2 lotes (`lote-herramientas`, `lote-quimicos`), 2 tarjetas, 2 estantes.
- **Mapa:**

```
[recepcion]--[inspeccion]--[centro]--[seguridad]
                              |
                         [pasillo-a]*--[pasillo-b]*      (* restringido)
```

- **Estado inicial:** ambos lotes sin inspeccionar en `recepcion`; el robot en `centro` con las manos libres; las dos tarjetas en `seguridad`; `estante-a1` (pasillo A) y `estante-b1` (pasillo B) vacíos.
- **Meta:** `(lote-almacenado lote-herramientas estante-a1)` y `(lote-almacenado lote-quimicos estante-b1)`.
- **Por qué no es trivial:** hay que ir por las tarjetas a un extremo del mapa, llevar cada lote a una zona de inspección, volver a recogerlo después de inspeccionarlo, y abrir los pasillos en orden (A desde el centro, B desde A). El robot lleva un solo lote a la vez, así que los lotes se reparten en viajes distintos.

## 6. Resultados

El problema se resolvió con dos planificadores distintos:

| Planificador | Longitud del plan | Observación | Archivo |
|---|---|---|---|
| BFWS (editor.planning.domains) | **31 pasos** | Plan válido; la búsqueda no garantiza optimalidad. | `plan/plan.txt` |
| BFS propio (`tools/solve.py`) | **28 pasos** | Óptimo para costos unitarios; 4 325 estados visitados, ≈ 0.03 s. | `plan/plan_optimo_28.txt` |

- 28 pasos es la longitud mínima, y ambos planes están muy por encima del mínimo exigido (5 pasos).
- La diferencia de 3 pasos se debe a que BFWS entra a `pasillo-a` solo para desbloquear `pasillo-b` y sale sin dejar nada, y a que procesa un lote por vez con un viaje de ida y vuelta a `recepcion` por cada uno. El plan óptimo lleva ambos lotes a la mesa de inspección antes de ir a los estantes.
- Ambos planes se verificaron con `tools/validate_plan.py`: liga cada acción a su esquema, comprueba tipos y precondiciones (estáticas incluidas) y confirma la meta. La traza del plan de 31 pasos, que es el que se explica en el video, está en `plan/plan_trace.md`.
- **Ablaciones** (`tools/ablaciones.py`): se quita una regla propia y se resuelve de nuevo con el BFS óptimo para medir su efecto.

| Variante | Pasos del plan óptimo |
|---|---|
| Dominio completo | 28 |
| Sin exigir inspección para almacenar | 22 |
| Sin zonas restringidas (pasillos libres) | 22 |
| Sin ambas reglas | 16 |

Cada regla propia aporta 6 pasos al plan, y juntas aportan 12, así que ambas condicionan el plan.

## 7. Limitaciones conocidas

- No se modelan tiempo, batería ni costos distintos por acción.
- Una zona desbloqueada queda abierta para siempre; en un almacén real se volvería a cerrar.
- Un lote puede esperar en la mesa de inspección el tiempo que sea; el modelo no tiene tiempos ni prioridades.
- Un solo robot: las acciones son estrictamente secuenciales.
- Posibles extensiones: segundo robot, capacidad de dos lotes, lotes refrigerados que requieran un estante frío, o tarjetas con caducidad.
