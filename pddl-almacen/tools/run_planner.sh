#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

echo "== Resolviendo con BFS (óptimo para costos unitarios) =="
python3 tools/solve.py

echo "== Validando el plan de BFWS (editor.planning.domains) =="
python3 tools/validate_plan.py

echo "== Validando el plan óptimo de BFS =="
python3 tools/validate_plan.py plan/plan_optimo_28.txt

echo "== Ablaciones =="
python3 tools/ablaciones.py
