#!/usr/bin/env bash

# Save the process group ID of this script.
pgid=`ps -o pgid= $$`

# Trap a Ctrl-C SIGINT and kill everything running inside this script.
trap "pkill -TERM -g $pgid" INT

# 1. Redirect server stderr to stdout.
# 2. Prefix each line with 'server'.
# 3. Background the process.
($1 2>&1 | while read server; do echo 'S: ' ${server}; done) &

# Wait.
sleep 1

# 1. Redirect client stderr to stdout.
# 2. Prefix each line with 'client'.
$2 2>&1 | while read client; do echo 'c: ' ${client}; done

# Kill this script and its children (client and server) when client finishes.
pkill -TERM -g $pgid
