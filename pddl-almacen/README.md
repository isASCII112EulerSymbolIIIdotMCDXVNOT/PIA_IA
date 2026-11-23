# Proyecto final PDDL: Almacén automatizado con zonas restringidas

Dominio y problema PDDL propios que modelan un robot montacargas que recibe lotes, los inspecciona y los almacena en estantes ubicados en pasillos que solo se abren con tarjetas de acceso de un solo uso.

## Estructura

```
pddl-almacen/
├── README.md
├── pddl/
│   ├── domain.pddl
│   └── problem.pddl
├── plan/
│   ├── plan.txt
│   ├── plan_trace.md
│   └── plan_optimo_28.txt
├── docs/
│   └── design_process.md
└── tools/
    ├── pddl_mini.py
    ├── solve.py
    ├── validate_plan.py
    ├── ablaciones.py
    └── run_planner.sh
```

| Archivo | Contenido |
|---|---|
| `pddl/domain.pddl` | 16 predicados y 8 acciones |
| `pddl/problem.pddl` | 6 zonas, 2 lotes, 2 tarjetas, 1 robot y 2 estantes |
| `plan/plan.txt` | Plan de 31 pasos encontrado por BFWS en editor.planning.domains |
| `plan/plan_trace.md` | Traza del plan de 31 pasos: precondiciones, efectos y meta de cada paso |
| `plan/plan_optimo_28.txt` | Plan óptimo de 28 pasos encontrado con un BFS propio |
| `docs/design_process.md` | Proceso de diseño, originalidad y resultados |
| `tools/` | Scripts de Python para resolver, validar y medir el efecto de cada regla |

## Cómo ejecutarlo

Para resolver el problema, copiar `pddl/domain.pddl` y `pddl/problem.pddl` en [editor.planning.domains](https://editor.planning.domains) y ejecutar un planificador desde el menú Solver. Con BFWS el plan tiene 31 pasos.

Para verificar los planes y repetir los experimentos (solo requiere Python 3, sin dependencias):

```bash
bash tools/run_planner.sh
```

## Resumen

| Requisito | Cumplimiento |
|---|---|
| Predicados (mín. 4) | 16 |
| Acciones (mín. 3) | 8, cada una con precondiciones, lista de agregar y lista de eliminar |
| Plan (mín. 5 pasos) | 31 pasos con BFWS; 28 pasos con un BFS óptimo |
| Originalidad y proceso de diseño | `docs/design_process.md` |

## Video

[Pegar aquí el enlace no listado del video, o indicar que se entregó en Teams]
