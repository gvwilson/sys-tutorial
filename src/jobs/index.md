---
title: "Running Jobs"
tagline: "How to do work on demand."
---

-   Computers don't get bored, so get them to do boring things

## Watching a Command {: #jobs-watch}

-   The `watch` command runs a command periodically and displays result
    -   Hard to show output statically…

[%inc watch_date.text %]

-   `-n 5`: every five seconds
-   Less distracting to show without title (`-t`)

[%inc watch_date_no_title.text %]

-   More useful to show differences with `-d`
-   Each successive update highlights the difference from the previous one
    -   Again, hard to show statically
-   Also use to use `-g` to exit when the command's output changes
-   E.g., `watch -n 1 -g netstat` will exit within one second of network activity

## Watching Files {: #jobs-fswatch}

-   Use `fswatch` (file system watch)

[%inc fswatch_example.text %]

-   `-l 1`: latency of one second (i.e., how often to report)
-   `-x Created -x Removed`: what events to watch for
-   `/tmp`: look for any changes in this directory
-   Get one line per change
    -   Common to pipe the output of `fswatch` to something that parses these lines and acts on them
-   [%fixme "why does removing the file generate a 'Created' record?" %]

## And Then There's `cron` {: #jobs-cron}

-   `cron` runs jobs at specified times
-   Which sounds simple, but its interface is complex even by Unix standards
    -   And differences between different machines make life even harder
-   Most research programmers won't ever need it
-   If you do, consult [crontab.guru][crontab-guru]

## Git Hooks {: #jobs-githooks}

-   Git stores repository data in `.git`
-   Contains a directory called `hooks`
-   Git automatically runs programs it finds there at particular times
    -   E.g., if there is a program called `pre-commit`, Git runs it before each commit takes place
-   What happens next depends on the program's exit [%g exit_status "exit status" %]
    -   0: no problems
    -   anything else: an error code of some sort

[%inc pre_commit_always_fail.text %]

-   More useful to check the files or something else

[%inc pre_commit_ruff.text %]

-   Use [ruff][ruff] to [%g lint "lint" %] the project's Python code
-   Exit with whatever exit status it returned
    -   `$?` is the exit status of the most recently run process in the shell

## Managing These Examples {: .aside}

-   Want to include the examples shown above in this repository and re-run them automatically
-   But nesting Git repositories is tricky
-   And re-running these commands *and* capturing all their output is also hard
