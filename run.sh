#!/usr/bin/env bash

set -e

cd "$(dirname "$0")"

LOG_FILE="app.log"
PID_FILE="app.pid"

if [ -f "$PID_FILE" ] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null; then
    echo "app.py is already running with PID $(cat "$PID_FILE")"
    exit 0
fi

if [ -d ".venv" ]; then
    source ".venv/bin/activate"
fi

nohup python app.py > "$LOG_FILE" 2>&1 &

echo $! > "$PID_FILE"

echo "app.py started in background"
echo "PID: $(cat "$PID_FILE")"
echo "Logs: $LOG_FILE"