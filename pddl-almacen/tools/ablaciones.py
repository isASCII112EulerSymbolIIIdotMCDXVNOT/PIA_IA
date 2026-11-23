import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pddl_mini import Dominio, Problema, bfs

RAIZ = Path(__file__).resolve().parent.parent
DOM = (RAIZ / "pddl" / "domain.pddl").read_text(encoding="utf-8")
PROB = (RAIZ / "pddl" / "problem.pddl").read_text(encoding="utf-8")

SIN_INSPECCION = DOM.replace("(destino ?l ?e)\n                       (lote-inspeccionado ?l))",
                             "(destino ?l ?e))")
SIN_TARJETAS = PROB.replace("(zona-inspeccion inspeccion)",
                            "(zona-inspeccion inspeccion)\n    (zona-libre pasillo-a)\n    (zona-libre pasillo-b)")

VARIANTES = [
    ("Dominio completo (referencia)", DOM, PROB),
    ("Sin exigir inspección para almacenar", SIN_INSPECCION, PROB),
    ("Sin zonas restringidas (pasillos libres)", DOM, SIN_TARJETAS),
    ("Sin inspección y sin zonas restringidas", SIN_INSPECCION, SIN_TARJETAS),
]


def resolver(dom_txt, prob_txt):
    with tempfile.TemporaryDirectory() as d:
        (Path(d) / "d.pddl").write_text(dom_txt, encoding="utf-8")
        (Path(d) / "p.pddl").write_text(prob_txt, encoding="utf-8")
        plan, _, _ = bfs(Dominio(Path(d) / "d.pddl"), Problema(Path(d) / "p.pddl"))
    return plan


def main():
    assert SIN_INSPECCION != DOM and SIN_TARJETAS != PROB, "la variante no modificó el texto"
    print("| Variante | Pasos del plan óptimo |\n|---|---|")
    for nombre, d, p in VARIANTES:
        plan = resolver(d, p)
        print(f"| {nombre} | {len(plan) if plan else 'sin solución'} |")


if __name__ == "__main__":
    main()
