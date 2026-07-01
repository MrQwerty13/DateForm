#!/usr/bin/env bash

set -e

cd "$(dirname "$0")"

PID_FILE="app.pid"

if [ ! -f "$PID_FILE" ]; then
    echo "No PID file found. app.py may not be running."
    exit 0
fi

PID="$(cat "$PID_FILE")"

if ! kill -0 "$PID" 2>/dev/null; then
    echo "Process with PID $PID is not running."
    rm -f "$PID_FILE"
    exit 0
fi

echo "Stopping app.py with PID $PID..."

kill "$PID"

sleep 2

if kill -0 "$PID" 2>/dev/null; then
    echo "Process did not stop gracefully, forcing stop..."
    kill -9 "$PID"
fi

rm -f "$PID_FILE"

echo "app.py stopped."