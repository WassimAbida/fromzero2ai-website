#! /bin/bash
set -o errexit -o pipefail -o nounset
# shellcheck source=/dev/null
source ./venv/bin/activate
# shellcheck source=/dev/null
# shellcheck disable=SC2154
streamlit run fromzero2ai/app_engine/demo_app.py --server.port=8501 --server.address=0.0.0.0
