#!/bin/sh
set -eu

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 \"Vault Display Name\" 13-char-author-code"
  exit 1
fi

NAME="$1"
AUTHOR="$2"

case "$AUTHOR" in
  ??????*) ;;
  *) echo "Author code must be exactly 13 lowercase ASCII/dash characters."; exit 1 ;;
esac
if [ "${#AUTHOR}" -ne 13 ]; then
  echo "Author code must be exactly 13 characters."
  exit 1
fi

if ! printf "%s" "$AUTHOR" | grep -Eq '^[a-z-]{13}$'; then
  echo "Author code must contain only lowercase a-z and '-'."
  exit 1
fi

if [ -f ".vault.yaml" ] && ! grep -q "UNINITIALIZED" ".vault.yaml"; then
  echo ".vault.yaml already appears initialized. Refusing to overwrite."
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
EOF

echo "Initialized vault UID: ${TS}${AUTHOR}"
