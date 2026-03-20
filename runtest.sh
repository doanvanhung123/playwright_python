#!/bin/bash

# ===== DEFAULT VALUES =====
BROWSER="chromium"
WORKERS=1
ENV="dev"
MARKER=""

# ===== PARSE ARGUMENTS =====
while [[ "$#" -gt 0 ]]; do
  case $1 in
    --browser) BROWSER="$2"; shift ;;
    --workers) WORKERS="$2"; shift ;;
    --env) ENV="$2"; shift ;;
    -m) MARKER="$2"; shift ;;
  esac
  shift
done

# ===== EXPORT ENV =====
export BROWSER=$BROWSER
export TEST_ENV=$ENV

echo "===== RUN CONFIG ====="
echo "Browser: $BROWSER"
echo "Workers: $WORKERS"
echo "Env: $ENV"
echo "Marker: $MARKER"

# ===== RUN TEST =====
if [ -z "$MARKER" ]; then
  python -m pytest -n $WORKERS --alluredir=allure-results
else
  python -m pytest -n $WORKERS -m "$MARKER" --alluredir=allure-results
fi

# # ===== OPEN REPORT =====
# allure serve allure-results