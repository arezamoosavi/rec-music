#!/bin/sh

set -o errexit
set -o nounset

uvicorn web_app:app --host "0.0.0.0" --port $PORT --reload --ws 'auto' \
--loop 'auto' --workers 4

exec "$@"