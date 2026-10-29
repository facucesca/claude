#!/bin/bash
# Prepara la sesión de Claude en la nube: instala lo que usan los programas del proyecto.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-.}"

# pip va al Python del sistema (no hay carpeta propia para guardar una marca),
# así que se revisa si ya está todo importable y solo se instala si falta algo
if ! python3 -c "import shapely, ezdxf, PIL, markdown, openpyxl" 2>/dev/null; then
  pip install --quiet -r requirements.txt
fi

# Chromium (para PDFs e imágenes) viene preinstalado en /opt/pw-browsers
if [ -n "${CLAUDE_ENV_FILE:-}" ] && [ -e /opt/pw-browsers/chromium ]; then
  echo 'export PATH="/opt/pw-browsers:$PATH"' >> "$CLAUDE_ENV_FILE"
fi
