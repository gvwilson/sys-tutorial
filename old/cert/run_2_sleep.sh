#!/usr/bin/env bash

# Save the process group ID of this script.
pgid=`ps -o pgid=$$`
echo "PGID $pgid"

# Trap a Ctrl-C SIGINT and kill everything running inside this script.
trap "pkill -TERM -g $pgid" INT

# Redirect server stderr to stdout and background the process.
$1 2>&1 &

# Wait one second.
sleep 1

# Redirect client stderr to stdout as well but run in foreground.
$2 2>&1

# Kill this script and its children (client and server) when client finishes.
pkill -TERM -g $pgid
