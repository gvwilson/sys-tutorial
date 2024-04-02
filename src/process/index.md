---
title: "Processes"
syllabus:
- FIXME
---

## Operating System vs. Shell

-   OS is…
-   Shell is…
-   Many different shells

## Program vs. Process

-   A program is…
-   A [%g process "process" %] is a running instance of a program
    -   Code plus variables in memory plus open files plus some IDs
-   Tools to manage them were invented when most users only had a single terminal

## Viewing Processes

-   Use `ps -a -l` to see currently running processes in terminal
    -   `UID`: numeric ID of the user that the process belongs to
    -   `PID`: process's unique ID
    -   `PPID`: ID of the process's parent (i.e., the process that created it)
    -   `CMD`: the command the process is running

[%inc ps_a_l.sh %]
[%inc ps_a_l.out %]

-   Use `ps -a -x` to see (almost) all processes running on computer
    -   `ps -a -x | wc` tells me there are 655 processes running on my laptop right now

## Parent and Child Processes

-   Every process is created by another process
    -   Except the first
-   Refer to [%g child_process "child process" %] and [%g parent_process "parent process" %]
-   `echo $$` shows [%g process_id "process ID" %] of current process
    -   `$$` shortcut because it's used so often
-   `echo $PPID` (parent process ID) to get parent
-   `pstree $$` to see [%g process_tree "process tree" %]

## Signals

-   Can send a [%g signal "signal" %] to a process
    -   Something extraordinary happened, please deal with it immediately

[% table slug="process_signals" tbl="signals.tbl" caption="Signals" %]

-   Create a [%g callback_function "callback function" %] to act as a [%g signal_handler "signal handler" %]

[%inc catch_interrupt.py %]
[%inc catch_interrupt.out %]

-   `^C` shows where user typed Ctrl-C

## Background Processes

-   Can run a process in the [%g background_process "background" %]
    -   Only difference is that it's not connected to the terminal

[%inc show_timer.py %]
[%inc show_timer.sh %]
[%inc show_timer.out %]

-   `&` at end of command to run `show_timer.py` means "run in the background"
-   So `ls` command executes immediately
-   But `show_timer.py` keeps running until it finishes
    -   Or needs keyboard input
-   Can also start process and then [%g suspend_process "suspend" %] it with Ctrl-Z
    -   Sends `SIGSTOP` instead of `SIGINT`
-   Use `jobs` to see all suspended processes
-   Then <code>bg %<em>num</em></code> to resume in the background
-   Or <code>fg %<em>num</em></code> to [%g foreground_process "foreground" %] the process
    to [%g resume_process "resume" %] its execution

[%inc ctrl_z_background.text %]

-   Note that input and output are mixed together

## Killing Processes

-   Use `kill` to send a signal to a process
    -   Not necessarily to stop it

[%inc kill_process.text %]

-   By default, `kill` sends `SIGTERM` (terminate process)
-   Variations:
    -   Give a process ID: `kill 1234`
    -   Send a different signal: `kill -s INT %1`

[%inc kill_int.text %]

## Fork

-   [%g fork_process "Fork" %] creates a duplicate of a process
    -   Creator is parent, gets process ID of child as return value
    -   Child gets 0 as return value (but has something else as its process ID)

[%inc fork.py %]
[%inc fork.out %]

## Flushing I/O

-   Example above works interactively
-   Run as `python fork.py > temp.out`, the "starting" line is duplicated
-   [%fixme "explain I/O flushing" %]

[%inc flush.py %]
[%inc flush.out %]

## Exec

-   The `exec` family of functions in `os` execute a new program *inside the calling process*
    -   Replace existing program and start a new one
-   So `fork`/`exec` to run a program

[%inc fork_exec.py %]
[%inc fork_exec.out %]

## Exercises

1.  What does the `top` command do?
    What does `top -o cpu` do?

1.  What does the `pgrep` command do?

1.  What are the differences between `os.execl`, `os.execlp`, and `os.execv`?
    When and why would you use each?
