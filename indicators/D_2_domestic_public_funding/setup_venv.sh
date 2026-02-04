#!/usr/bin/env bash
set -e

# --- config ---
VENV_DIR=".venv"
PYTHON_BIN="python3"
REQ_FILE="requirements.txt"
SCRIPTS=(
  "querymaker_descargar_glosas.py"
  "querymaker_todos_los_programas_estatales.py"
)

# --- crear venv ---
if [ ! -d "$VENV_DIR" ]; then
  echo ">> creando venv en $VENV_DIR"
  $PYTHON_BIN -m venv "$VENV_DIR"
fi

VENV_PY="$(pwd)/$VENV_DIR/bin/python"

if [ ! -x "$VENV_PY" ]; then
  echo "error en la creacion de venv (dir: $VENV_PY) "
  exit 1
fi

# --- instalar requirements ---
if [ -f "$REQ_FILE" ]; then
  echo ">> instalando requirements.txt"
  "$VENV_PY" -m pip install -r "$REQ_FILE"
else
  echo " no hay requirements.txt, saltandando este paso"
fi

# --- arreglar shebangs ---
for f in "${SCRIPTS[@]}"; do
  if [ ! -f "$f" ]; then
    echo "archivo no existente : $f"
    continue
  fi

  # borrar shebang viejo
  sed -i '1{/^#!/d}' "$f"

  # poner shebang correcto
  sed -i "1i #!$VENV_PY" "$f"

  chmod +x "$f"
  echo ">> shebang listo en $f"
done

echo "archivos modificados: ./querymaker_descargar_glosas.py o ./querymaker_todos_los_programas_estatales.py"

