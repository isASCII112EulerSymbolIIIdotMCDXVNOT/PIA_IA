import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pddl_mini import Dominio, Problema, bfs

RAIZ = Path(__file__).resolve().parent.parent


def main():
    dom = Dominio(RAIZ / "pddl" / "domain.pddl")
    prob = Problema(RAIZ / "pddl" / "problem.pddl")
    t0 = time.time()
    plan, estados, ops = bfs(dom, prob)
    dt = time.time() - t0
    if plan is None:
        print("Sin solución")
        sys.exit(1)
    (RAIZ / "plan" / "plan_optimo_28.txt").write_text("\n".join(plan) + "\n", encoding="utf-8")
    print(f"Plan de {len(plan)} pasos (óptimo, BFS) | {ops} operadores instanciados | "
          f"{estados} estados visitados | {dt:.2f} s")


if __name__ == "__main__":
    main()
