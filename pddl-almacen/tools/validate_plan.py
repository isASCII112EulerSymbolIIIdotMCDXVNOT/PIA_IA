import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pddl_mini import Dominio, Problema, separar_efectos, sustituir

RAIZ = Path(__file__).resolve().parent.parent
PLAN = RAIZ / "plan" / "plan.txt"
TRAZA = RAIZ / "plan" / "plan_trace.md"


def fmt(atomo):
    return "`(" + " ".join(atomo) + ")`"


def main():
    ruta = Path(sys.argv[1]) if len(sys.argv) > 1 else PLAN
    dom = Dominio(RAIZ / "pddl" / "domain.pddl")
    prob = Problema(RAIZ / "pddl" / "problem.pddl")
    tipos = dict(prob.objetos)
    pasos = [l.strip() for l in ruta.read_text().splitlines() if l.strip().startswith("(")]
    estado = set(prob.init)
    ok = True
    lineas = [f"# Traza de ejecución del plan ({len(pasos)} pasos)\n"]

    for i, paso in enumerate(pasos, 1):
        nombre, *args = paso.strip("()").split()
        acc = dom.acciones.get(nombre)
        if acc is None or len(args) != len(acc["params"]):
            print(f"Paso {i}: acción inválida {paso}")
            ok = False
            continue
        for (v, tp), o in zip(acc["params"], args):
            if o not in tipos or not dom.es_tipo(tipos[o], tp):
                print(f"Paso {i} {paso}: {o} no es de tipo {tp}")
                ok = False
        ligas = {v: o for (v, _), o in zip(acc["params"], args)}
        pre = [sustituir(p, ligas) for p in acc["pre"]]
        faltan = [p for p in pre if p not in estado]
        if faltan:
            ok = False
            print(f"Paso {i} {paso}: precondiciones NO satisfechas: {faltan}")
        agrega, elimina = separar_efectos(acc["efectos"], ligas)
        lineas.append(f"## Paso {i}: `{paso}`\n")
        lineas.append("- Precondiciones (todas verdaderas en el estado previo): "
                      + ", ".join(fmt(p) for p in pre))
        lineas.append("- Agrega: " + (", ".join(fmt(p) for p in sorted(agrega)) or "—"))
        lineas.append("- Elimina: " + (", ".join(fmt(p) for p in sorted(elimina)) or "—"))
        lineas.append("")
        estado = (estado - elimina) | agrega

    lineas.append("## Verificación de la meta\n")
    meta_ok = True
    for g in prob.meta:
        cumple = g in estado
        meta_ok &= cumple
        lineas.append(f"- {fmt(g)}: {'✔ se cumple' if cumple else '✘ NO se cumple'}")

    if ok and meta_ok:
        print(f"PLAN VÁLIDO ({ruta.name}): {len(pasos)} pasos, todas las precondiciones se cumplen y la meta se alcanza.")
        if ruta == PLAN:
            TRAZA.write_text("\n".join(lineas) + "\n", encoding="utf-8")
            print(f"Traza escrita en {TRAZA.relative_to(RAIZ)}")
    else:
        print(f"PLAN INVÁLIDO ({ruta.name})")
        sys.exit(1)


if __name__ == "__main__":
    main()
