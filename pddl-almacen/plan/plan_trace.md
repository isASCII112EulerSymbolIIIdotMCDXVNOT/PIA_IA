# Traza de ejecución del plan (31 pasos)

## Paso 1: `(mover robot-1 centro seguridad)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 centro)`, `(conectada centro seguridad)`, `(zona-libre seguridad)`
- Agrega: `(robot-en robot-1 seguridad)`
- Elimina: `(robot-en robot-1 centro)`

## Paso 2: `(tomar-tarjeta robot-1 tarjeta-a seguridad)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 seguridad)`, `(tarjeta-en tarjeta-a seguridad)`, `(manos-libres robot-1)`
- Agrega: `(tiene-tarjeta robot-1 tarjeta-a)`
- Elimina: `(tarjeta-en tarjeta-a seguridad)`

## Paso 3: `(tomar-tarjeta robot-1 tarjeta-b seguridad)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 seguridad)`, `(tarjeta-en tarjeta-b seguridad)`, `(manos-libres robot-1)`
- Agrega: `(tiene-tarjeta robot-1 tarjeta-b)`
- Elimina: `(tarjeta-en tarjeta-b seguridad)`

## Paso 4: `(mover robot-1 seguridad centro)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 seguridad)`, `(conectada seguridad centro)`, `(zona-libre centro)`
- Agrega: `(robot-en robot-1 centro)`
- Elimina: `(robot-en robot-1 seguridad)`

## Paso 5: `(desbloquear-zona robot-1 tarjeta-a centro pasillo-a)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 centro)`, `(conectada centro pasillo-a)`, `(tiene-tarjeta robot-1 tarjeta-a)`, `(tarjeta-de tarjeta-a pasillo-a)`
- Agrega: `(zona-desbloqueada pasillo-a)`
- Elimina: `(tiene-tarjeta robot-1 tarjeta-a)`

## Paso 6: `(mover-restringida robot-1 centro pasillo-a)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 centro)`, `(conectada centro pasillo-a)`, `(zona-desbloqueada pasillo-a)`
- Agrega: `(robot-en robot-1 pasillo-a)`
- Elimina: `(robot-en robot-1 centro)`

## Paso 7: `(desbloquear-zona robot-1 tarjeta-b pasillo-a pasillo-b)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 pasillo-a)`, `(conectada pasillo-a pasillo-b)`, `(tiene-tarjeta robot-1 tarjeta-b)`, `(tarjeta-de tarjeta-b pasillo-b)`
- Agrega: `(zona-desbloqueada pasillo-b)`
- Elimina: `(tiene-tarjeta robot-1 tarjeta-b)`

## Paso 8: `(mover robot-1 pasillo-a centro)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 pasillo-a)`, `(conectada pasillo-a centro)`, `(zona-libre centro)`
- Agrega: `(robot-en robot-1 centro)`
- Elimina: `(robot-en robot-1 pasillo-a)`

## Paso 9: `(mover robot-1 centro inspeccion)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 centro)`, `(conectada centro inspeccion)`, `(zona-libre inspeccion)`
- Agrega: `(robot-en robot-1 inspeccion)`
- Elimina: `(robot-en robot-1 centro)`

## Paso 10: `(mover robot-1 inspeccion recepcion)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 inspeccion)`, `(conectada inspeccion recepcion)`, `(zona-libre recepcion)`
- Agrega: `(robot-en robot-1 recepcion)`
- Elimina: `(robot-en robot-1 inspeccion)`

## Paso 11: `(recoger robot-1 lote-quimicos recepcion)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 recepcion)`, `(lote-en lote-quimicos recepcion)`, `(manos-libres robot-1)`
- Agrega: `(cargando robot-1 lote-quimicos)`
- Elimina: `(lote-en lote-quimicos recepcion)`, `(manos-libres robot-1)`

## Paso 12: `(mover robot-1 recepcion inspeccion)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 recepcion)`, `(conectada recepcion inspeccion)`, `(zona-libre inspeccion)`
- Agrega: `(robot-en robot-1 inspeccion)`
- Elimina: `(robot-en robot-1 recepcion)`

## Paso 13: `(soltar robot-1 lote-quimicos inspeccion)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 inspeccion)`, `(cargando robot-1 lote-quimicos)`
- Agrega: `(lote-en lote-quimicos inspeccion)`, `(manos-libres robot-1)`
- Elimina: `(cargando robot-1 lote-quimicos)`

## Paso 14: `(inspeccionar-lote robot-1 lote-quimicos inspeccion)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 inspeccion)`, `(zona-inspeccion inspeccion)`, `(lote-en lote-quimicos inspeccion)`, `(manos-libres robot-1)`
- Agrega: `(lote-inspeccionado lote-quimicos)`
- Elimina: —

## Paso 15: `(recoger robot-1 lote-quimicos inspeccion)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 inspeccion)`, `(lote-en lote-quimicos inspeccion)`, `(manos-libres robot-1)`
- Agrega: `(cargando robot-1 lote-quimicos)`
- Elimina: `(lote-en lote-quimicos inspeccion)`, `(manos-libres robot-1)`

## Paso 16: `(mover robot-1 inspeccion centro)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 inspeccion)`, `(conectada inspeccion centro)`, `(zona-libre centro)`
- Agrega: `(robot-en robot-1 centro)`
- Elimina: `(robot-en robot-1 inspeccion)`

## Paso 17: `(mover-restringida robot-1 centro pasillo-a)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 centro)`, `(conectada centro pasillo-a)`, `(zona-desbloqueada pasillo-a)`
- Agrega: `(robot-en robot-1 pasillo-a)`
- Elimina: `(robot-en robot-1 centro)`

## Paso 18: `(mover-restringida robot-1 pasillo-a pasillo-b)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 pasillo-a)`, `(conectada pasillo-a pasillo-b)`, `(zona-desbloqueada pasillo-b)`
- Agrega: `(robot-en robot-1 pasillo-b)`
- Elimina: `(robot-en robot-1 pasillo-a)`

## Paso 19: `(almacenar robot-1 lote-quimicos estante-b1 pasillo-b)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 pasillo-b)`, `(cargando robot-1 lote-quimicos)`, `(estante-en estante-b1 pasillo-b)`, `(estante-vacio estante-b1)`, `(destino lote-quimicos estante-b1)`, `(lote-inspeccionado lote-quimicos)`
- Agrega: `(lote-almacenado lote-quimicos estante-b1)`, `(manos-libres robot-1)`
- Elimina: `(cargando robot-1 lote-quimicos)`, `(estante-vacio estante-b1)`

## Paso 20: `(mover-restringida robot-1 pasillo-b pasillo-a)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 pasillo-b)`, `(conectada pasillo-b pasillo-a)`, `(zona-desbloqueada pasillo-a)`
- Agrega: `(robot-en robot-1 pasillo-a)`
- Elimina: `(robot-en robot-1 pasillo-b)`

## Paso 21: `(mover robot-1 pasillo-a centro)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 pasillo-a)`, `(conectada pasillo-a centro)`, `(zona-libre centro)`
- Agrega: `(robot-en robot-1 centro)`
- Elimina: `(robot-en robot-1 pasillo-a)`

## Paso 22: `(mover robot-1 centro inspeccion)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 centro)`, `(conectada centro inspeccion)`, `(zona-libre inspeccion)`
- Agrega: `(robot-en robot-1 inspeccion)`
- Elimina: `(robot-en robot-1 centro)`

## Paso 23: `(mover robot-1 inspeccion recepcion)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 inspeccion)`, `(conectada inspeccion recepcion)`, `(zona-libre recepcion)`
- Agrega: `(robot-en robot-1 recepcion)`
- Elimina: `(robot-en robot-1 inspeccion)`

## Paso 24: `(recoger robot-1 lote-herramientas recepcion)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 recepcion)`, `(lote-en lote-herramientas recepcion)`, `(manos-libres robot-1)`
- Agrega: `(cargando robot-1 lote-herramientas)`
- Elimina: `(lote-en lote-herramientas recepcion)`, `(manos-libres robot-1)`

## Paso 25: `(mover robot-1 recepcion inspeccion)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 recepcion)`, `(conectada recepcion inspeccion)`, `(zona-libre inspeccion)`
- Agrega: `(robot-en robot-1 inspeccion)`
- Elimina: `(robot-en robot-1 recepcion)`

## Paso 26: `(soltar robot-1 lote-herramientas inspeccion)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 inspeccion)`, `(cargando robot-1 lote-herramientas)`
- Agrega: `(lote-en lote-herramientas inspeccion)`, `(manos-libres robot-1)`
- Elimina: `(cargando robot-1 lote-herramientas)`

## Paso 27: `(inspeccionar-lote robot-1 lote-herramientas inspeccion)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 inspeccion)`, `(zona-inspeccion inspeccion)`, `(lote-en lote-herramientas inspeccion)`, `(manos-libres robot-1)`
- Agrega: `(lote-inspeccionado lote-herramientas)`
- Elimina: —

## Paso 28: `(recoger robot-1 lote-herramientas inspeccion)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 inspeccion)`, `(lote-en lote-herramientas inspeccion)`, `(manos-libres robot-1)`
- Agrega: `(cargando robot-1 lote-herramientas)`
- Elimina: `(lote-en lote-herramientas inspeccion)`, `(manos-libres robot-1)`

## Paso 29: `(mover robot-1 inspeccion centro)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 inspeccion)`, `(conectada inspeccion centro)`, `(zona-libre centro)`
- Agrega: `(robot-en robot-1 centro)`
- Elimina: `(robot-en robot-1 inspeccion)`

## Paso 30: `(mover-restringida robot-1 centro pasillo-a)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 centro)`, `(conectada centro pasillo-a)`, `(zona-desbloqueada pasillo-a)`
- Agrega: `(robot-en robot-1 pasillo-a)`
- Elimina: `(robot-en robot-1 centro)`

## Paso 31: `(almacenar robot-1 lote-herramientas estante-a1 pasillo-a)`

- Precondiciones (todas verdaderas en el estado previo): `(robot-en robot-1 pasillo-a)`, `(cargando robot-1 lote-herramientas)`, `(estante-en estante-a1 pasillo-a)`, `(estante-vacio estante-a1)`, `(destino lote-herramientas estante-a1)`, `(lote-inspeccionado lote-herramientas)`
- Agrega: `(lote-almacenado lote-herramientas estante-a1)`, `(manos-libres robot-1)`
- Elimina: `(cargando robot-1 lote-herramientas)`, `(estante-vacio estante-a1)`

## Verificación de la meta

- `(lote-almacenado lote-herramientas estante-a1)`: ✔ se cumple
- `(lote-almacenado lote-quimicos estante-b1)`: ✔ se cumple
