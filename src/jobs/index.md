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
