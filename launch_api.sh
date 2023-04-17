#! /bin/bash
set -o errexit -o pipefail -o nounset
# shellcheck source=/dev/null
source ./venv/bin/activate
# shellcheck source=/dev/null
# shellcheck disable=SC2154
# PYTHON_ENV="${long_env}" python -m "$PROJECT_NAME" run

python -m uvicorn fromzero2ai.api_engine.main:app --host 0.0.0.0 --port ${CONTAINER_PORT}
