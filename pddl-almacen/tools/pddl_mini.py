import itertools
import re
from collections import deque


def _sexpr(text):
    text = re.sub(r";.*", "", text).lower()
    pila = [[]]
    for tok in re.findall(r"\(|\)|[^\s()]+", text):
        if tok == "(":
            pila.append([])
        elif tok == ")":
            x = pila.pop()
            pila[-1].append(x)
        else:
            pila[-1].append(tok)
    return pila[0][0]


def _tipada(lst):
    salida, nombres, i = [], [], 0
    while i < len(lst):
        if lst[i] == "-":
            salida += [(n, lst[i + 1]) for n in nombres]
            nombres, i = [], i + 2
        else:
            nombres.append(lst[i])
            i += 1
    return salida + [(n, "object") for n in nombres]


def _conjuncion(expr):
    if expr[0] == "and":
        return expr[1:]
    return [expr]


class Dominio:
    def __init__(self, ruta):
        d = _sexpr(open(ruta, encoding="utf-8").read())
        self.nombre = d[1][1]
        self.padre = {"object": None}
        self.predicados = {}
        self.acciones = {}
        for sec in d[2:]:
            if sec[0] == ":types":
                for t, p in _tipada(sec[1:]):
                    self.padre[t] = p
            elif sec[0] == ":predicates":
                for p in sec[1:]:
                    self.predicados[p[0]] = [t for _, t in _tipada(p[1:])]
            elif sec[0] == ":action":
                self._accion(sec)
        self.estaticos = set(self.predicados) - {
            e[0] if e[0] != "not" else e[1][0]
            for a in self.acciones.values()
            for e in a["efectos"]
        }

    def _accion(self, sec):
        nombre, props = sec[1], {sec[i]: sec[i + 1] for i in range(2, len(sec), 2)}
        pre = _conjuncion(props[":precondition"])
        efe = _conjuncion(props[":effect"])
        if any(p[0] == "not" for p in pre):
            raise ValueError("precondiciones negativas no soportadas")
        self.acciones[nombre] = {
            "params": _tipada(props[":parameters"]),
            "pre": [tuple(p) for p in pre],
            "efectos": [e if e[0] != "not" else ("not", tuple(e[1])) for e in efe],
        }

    def es_tipo(self, tipo, objetivo):
        while tipo is not None:
            if tipo == objetivo:
                return True
            tipo = self.padre.get(tipo)
        return False


class Problema:
    def __init__(self, ruta):
        p = _sexpr(open(ruta, encoding="utf-8").read())
        self.nombre = p[1][1]
        self.objetos, self.init, self.meta = [], set(), []
        for sec in p[2:]:
            if sec[0] == ":objects":
                self.objetos = _tipada(sec[1:])
            elif sec[0] == ":init":
                self.init = {tuple(a) for a in sec[1:]}
            elif sec[0] == ":goal":
                self.meta = [tuple(a) for a in _conjuncion(sec[1])]


def sustituir(atomo, ligas):
    return (atomo[0],) + tuple(ligas.get(x, x) for x in atomo[1:])


def separar_efectos(efectos, ligas):
    agrega, elimina = set(), set()
    for e in efectos:
        if e[0] == "not":
            elimina.add(sustituir(e[1], ligas))
        else:
            agrega.add(sustituir(e, ligas))
    return agrega, elimina


def instanciar(dom, prob):
    ops = []
    for nombre, a in dom.acciones.items():
        dominios = [[o for o, t in prob.objetos if dom.es_tipo(t, tp)]
                    for _, tp in a["params"]]
        for combo in itertools.product(*dominios):
            ligas = {v: o for (v, _), o in zip(a["params"], combo)}
            pre = [sustituir(p, ligas) for p in a["pre"]]
            if any(p[0] in dom.estaticos and p not in prob.init for p in pre):
                continue
            agrega, elimina = separar_efectos(a["efectos"], ligas)
            ops.append({
                "nombre": "(" + " ".join((nombre,) + combo) + ")",
                "pre": frozenset(p for p in pre if p[0] not in dom.estaticos),
                "agrega": frozenset(agrega),
                "elimina": frozenset(elimina),
            })
    return ops


def bfs(dom, prob):
    ops = instanciar(dom, prob)
    inicio = frozenset(a for a in prob.init if a[0] not in dom.estaticos)
    meta = frozenset(prob.meta)
    padres = {inicio: None}
    cola = deque([inicio])
    while cola:
        s = cola.popleft()
        if meta <= s:
            plan = []
            while padres[s] is not None:
                s, nombre = padres[s]
                plan.append(nombre)
            return plan[::-1], len(padres), len(ops)
        for op in ops:
            if op["pre"] <= s:
                t = (s - op["elimina"]) | op["agrega"]
                if t not in padres:
                    padres[t] = (s, op["nombre"])
                    cola.append(t)
    return None, len(padres), len(ops)
