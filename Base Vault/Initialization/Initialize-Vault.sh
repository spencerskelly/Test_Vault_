#!/bin/sh
set -eu

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 \"Vault Display Name\" 13-char-author-code"
  exit 1
fi

NAME="$1"
AUTHOR="$2"

if [ "${#AUTHOR}" -ne 13 ] || ! printf "%s" "$AUTHOR" | grep -Eq '^[a-z-]{13}$'; then
  echo "Author code must be exactly 13 lowercase ASCII letters/dashes."
  exit 1
fi

if [ ! -f ".vault.yaml" ]; then
  echo ".vault.yaml is missing. Start from a generated MDSE base vault."
  exit 1
fi
if ! grep -q "UNINITIALIZED" ".vault.yaml"; then
  echo ".vault.yaml already appears initialized. Refusing to overwrite."
  exit 1
fi

RELEASE=$(python3 - <<'PY'
import re
text=open(".vault.yaml", encoding="utf-8").read()
m=re.search(r"(?m)^mdse_release:\\s*[\"']?([^\"'#\\r\\n]+)", text)
print(m.group(1).strip() if m else "")
PY
)
if [ -z "$RELEASE" ]; then
  echo ".vault.yaml has no mdse_release. Refusing to initialize an unpaired base."
  exit 1
fi

TS=$(python3 - <<'PY'
from datetime import datetime, timezone
now=datetime.now(timezone.utc)
print(now.strftime("%Y%m%d%H%M%S")+f"{now.microsecond//1000:03d}")
PY
)

cat > .vault.yaml <<EOF
vault_uid: ${TS}${AUTHOR}
name: ${NAME}
default_branch: main
mdse_release: "${RELEASE}"
EOF

echo "Initialized vault UID: ${TS}${AUTHOR}"
echo "Preserved MDSE release: ${RELEASE}"
