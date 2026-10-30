#!/bin/bash
# Prepara la sesión de Claude: instala lo que usan los programas del proyecto.
# Anda en la nube y en la compu. Nunca corta la sesión: si algo falla, lo deja escrito
# ("INSTALACIÓN: ...") para que Claude se lo explique a Camila.
set -uo pipefail

cd "${CLAUDE_PROJECT_DIR:-.}"

PY=$(command -v python3 || command -v python || true)
if [ -z "$PY" ]; then
  echo "INSTALACIÓN: falta Python en esta compu (no se pudo instalar nada)."
  exit 0
fi

# Chromium (para PDFs e imágenes) viene preinstalado en la nube
if [ -n "${CLAUDE_ENV_FILE:-}" ] && [ -e /opt/pw-browsers/chromium ]; then
  echo 'export PATH="/opt/pw-browsers:$PATH"' >> "$CLAUDE_ENV_FILE"
fi

# pip va al Python del sistema (no hay carpeta propia para guardar una marca),
# así que se revisa si ya está todo importable y solo se instala si falta algo
listo() { "$PY" -c "import shapely, ezdxf, PIL, markdown, openpyxl" 2>/dev/null; }
if listo; then
  echo "INSTALACIÓN: lista (ya estaba todo)."
  exit 0
fi
"$PY" -m pip install --quiet -r requirements.txt >/dev/null 2>&1 \
  || "$PY" -m pip install --quiet --user -r requirements.txt >/dev/null 2>&1 \
  || "$PY" -m pip install --quiet --user --break-system-packages -r requirements.txt >/dev/null 2>&1
if listo; then
  echo "INSTALACIÓN: lista (se instaló todo recién)."
else
  echo "INSTALACIÓN: falló pip install -r requirements.txt. Probar a mano."
fi
exit 0
