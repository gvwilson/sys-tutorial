# assume first arg is a set of TCP ports
# followed by one command per server listening to the port
# followed by client commands
# bash run_and_wait.sh "8000" "server 8000" "client"

PORTS="$1"
shift

CHILDREN=

await_port_free() {
    PORTNUM=$1
    while lsof -n -iTCP:${PORTNUM} ; do
        sleep 0.5
        printf "*"
    done
    printf "\nport $PORTNUM free\n"
}

await_port_listen() {
    PORTNUM=$1
    while ! lsof -n -iTCP:${PORTNUM}|grep -qw LISTEN ; do
        sleep 0.5
        printf "*"
    done
    printf "\nport $PORTNUM in LISTEN state\n"
}

on_exit(){
    # disable trap
    trap - exit int
    # gently kill every child
    kill -INT $CHILDREN &>/dev/null
    sleep 1
    # thorough cleanup
    pkill -TERM -g 0
}

# exiting or ^C runs on_exit
trap on_exit exit int

# server commands

for PORT in $PORTS; do
    await_port_free $PORT

    CMD="$1"
    shift
    $CMD &
    CHILDREN="$CHILDREN $!"

    await_port_listen $PORT
done

# client commands

for CMD in "$@"; do
    $CMD &
    CHILDREN="$CHILDREN $!"
done

# wait until any child process exits
while true; do
    for CHILD in $CHILDREN; do
        if ! kill -0 $CHILD &>/dev/null; then
            exit # to on_exit
        fi
    done
    sleep 0.5
done
