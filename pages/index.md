<div class="row">
  <div class="col-4 center">
    <img src="@root/advent_05_356-resized.png" alt="cover art by Danielle Navarro" width="80%"/>
  </div>
  <div class="col-8">
    <p>
      Many think they know Unix.
      Few realize that what they know is just a shell.
      Beneath it lie mysteries both bewildering and wonderful:
      ports, processes, permissions,
      files that are not files,
      and components built atop other, older components
      that occasionally rise to the surface like ancient sea creatures believed long extinct.
    </p>
    <p>
      Like such creatures,
      Unix will outlive those who mock it.
      Welcome, then, to a world in which the strange will become familiar, and the familiar, strange.
      Welcome, thrice welcome, to Unix systems programming.
    </p>
    <p class="italic">
      "[% config "title" %]" is a <a href="[% config "author.site" %]">Third Bit</a> production.
    </p>
  </div>
</div>

<!-- ---------------------------------------------------------------- -->
[% section_start class="aside" title="What This Is" %]

-   Notes and working examples that instructors can use to perform a lesson
    -   Do *not* expect novices with no prior Unix experience to be able to learn from them on their own
-   Musical analogy
    -   This is the chord changes and melody
    -   We expect instructors to create an arrangement and/or improvise while delivering
-   Please see [the license](./license/) for terms of use,
    the [Code of Conduct](./conduct/) for community standards,
    and [these guidelines](./contributing/) for notes on contributing
-   [Greg Wilson][wilson_greg] is a programmer, author, and educator based in Toronto

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Scope" %]

-   [Intended audience][persona]
    -   Ning did a bachelor's degree in economics
        and now works as a data analyst for the Ministry of Health
    -   They are comfortable working with Unix command-line tools,
        writing data analysis programs in Python,
	and downloading data from the web manually
    -   Ning wants to understand what happens when they install a package
	or run a pipeline in the cloud
    -   Their work schedule is unpredictable and highly variable,
        so they need to be able to learn a bit at a time
-   Prerequisites
    -   Unix shell commands covered in [this Software Carpentry lesson][sc_shell]:
        -   `pwd`; `ls`; `cd`; `.` and `..`; `rm` and `rmdir`; `mkdir`; `touch`;
            `mv`; `cp`; `tree`; `cat`; `wc`; `head`; `tail`; `less`; `cut`; `echo`;
            `history`; `find`; `grep`; `zip`; `man`
        -   current working directory; absolute and relative paths; naming files;
            editing with `nano`
        -   standard input; standard output; standard error; redirection; pipes
        -   `*` and `?` wildcards; shell variable with `$` expansion; `for` loop
    -   Python for command-line scripting
        -   variables; numbers and strings; lists; dictionaries; `for` and `while` loops;
	    `if`/`else`; `with`; defining and calling functions; `sys.argv`, `sys.stdin`,
	    and `sys.stdout`; simple regular expressions; reading JSON data;
	    reading CSV files using [Pandas][pandas] or [Polars][polars]
        -   `pip install`
	-   `python -m venv` or `conda create`
-   Learning outcomes
    1.  Explain the difference between shell variables and environment variables
        and write shell scripts that use each.
    1.  Create a virtual environment and explain what this actually does.
    1.  Create `requirements.txt` file for [`pip`][pip] and explain version pinning.
    1.  Explain what a filesystem is (disk partitions, inodes, symbolic links)
        and use `df`, `ln`, similar commands to explore with them.
    1.  Explain what a process is and use commands like `ps` and `kill` to explore and manage them.
    1.  Explain what a job is and use commands like `jobs`, `bg`, and `fg` to manage them.
    1.  Explain what `cron` jobs are and how to create them.
    1.  Explain the difference between a container and a virtual machine.
    1.  Create and manage Docker images.
    1.  Explain what ports are and write Python code that uses sockets and HTTP.
    1.  Explain what certificates are and how they are used to support HTTPS.
    1.  Explain what key pairs are and how they are stored, and create and manage key pairs.
    1.  Explain what IP addresses are and how they are resolved.
    1.  Explain how traditional password authentication works and describe its weaknesses.

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Setup" %]

-   Download [the latest release]([% config "release" %])
-   Unzip the file in a temporary directory to create:
    -   `./site/*.*`: files and directories used in examples
    -   `./src/*.*`: shell scripts and Python programs
    -   `./out/*.*`: expected output for examples

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Operating System vs. Shell" %]

-   OS is…
-   Shell is…
-   Many different shells
-   [% todo "how to tell what shell you are using" %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Program vs. Process" %]

-   A program is…
-   A [%g process "process" %] is a running instance of a program
    -   Code plus variables in memory plus open files plus some IDs
-   Tools to manage them were invented when most users only had a single terminal

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Viewing Processes" %]

-   Use `ps -a -l` to see currently running processes in terminal
    -   `UID`: numeric ID of the user that the process belongs to
    -   `PID`: process's unique ID
    -   `PPID`: ID of the process's parent (i.e., the process that created it)
    -   `CMD`: the command the process is running

[% multi "src/ps_a_l.sh" "out/ps_a_l.out" %]

-   Use `ps -a -x` to see (almost) all processes running on computer
    -   `ps -a -x | wc` tells me there are 655 processes running on my laptop right now

<!-- ---------------------------------------------------------------- -->
[% section_break class="exercise" %]

[% exercise %]
What does the `top` command do?
What does `top -o cpu` do?

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Parent and Child Processes" %]

-   Every process is created by another process
    -   Except the first
-   Refer to [%g process_child "child process" %] and [%g process_parent "parent process" %]
-   `echo $$` shows [%g process_id "process ID" %] of current process
    -   `$$` shortcut because it's used so often
-   `echo $PPID` (parent process ID) to get parent
-   `pstree $$` to see [%g process_tree "process tree" %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Shell Variables vs. Environment Variables" %]

-   The shell is a program and programs have variables
-   [%g shell_var "Shell variable" %] stays in the process
-   [%g env_var "Environment variable" %] is inherited by new processes

[%multi src/shell_vs_env_outer.sh src/shell_vs_env_inner.sh out/shell_vs_env_outer.out %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="exercise" %]

[% exercise %]
If a child process sets shell or environment variables,
are they visible in the parent once the child finishes executing?

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Signals" %]

-   Can send a [%g signal "signal" %] to a process
    -   Something extraordinary happened, please deal with it immediately

| Number | Name      | Default Action    | Description |
| -----: | --------- | ----------------- | ----------- |
|      1 | `SIGHUP`  | terminate process | terminal line hangup |
|      2 | `SIGINT`  | terminate process | interrupt program |
|      3 | `SIGQUIT` | create core image | quit program |
|      4 | `SIGILL`  | create core image | illegal instruction |
|      8 | `SIGFPE`  | create core image | floating-point exception |
|      9 | `SIGKILL` | terminate process | kill program |
|     11 | `SIGSEGV` | create core image | segmentation violation |
|     12 | `SIGSYS`  | create core image | non-existent system call invoked |
|     14 | `SIGALRM` | terminate process | real-time timer expired |
|     15 | `SIGTERM` | terminate process | software termination signal |
|     17 | `SIGSTOP` | stop process      | stop (cannot be caught or ignored) |
|     24 | `SIGXCPU` | terminate process | CPU time limit exceeded |
|     25 | `SIGXFSZ` | terminate process | file size limit exceeded |

-   Create a [%g callback_function "callback function" %] to act as a [%g signal_handler "signal handler" %]

[% multi src/catch_interrupt.py out/catch_interrupt.out %]

-   `^C` shows where user typed Ctrl-C

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Background Processes" %]

-   Can run a process in the [%g process_background "background" %]
    -   Only difference is that it's not connected to the terminal

[% multi src/show_timer.py src/show_timer.sh out/show_timer.out %]

-   `&` at end of command to run `show_timer.py` means "run in the background"
-   So `ls` command executes immediately
-   But `show_timer.py` keeps running until it finishes
    -   Or needs keyboard input
-   Can also start process and then [%g process_suspend "suspend" %] it with Ctrl-Z
    -   Sends `SIGSTOP` instead of `SIGINT`
-   Use `jobs` to see all suspended processes
-   Then <code>bg %<em>num</em></code> to resume in the background
-   Or <code>fg %<em>num</em></code> to [%g process_foreground "foreground" %] the process
    to [%g process_resume "resume" %] its execution

[% single src/ctrl_z_background.text %]

-   Note that input and output are mixed together

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Killing Processes" %]

-   Use `kill` to send a signal to a process
    -   Not necessarily to stop it

[% single src/kill_process.text %]

-   By default, `kill` sends `SIGTERM` (terminate process)
-   Variations:
    -   Give a process ID: `kill 1234`
    -   Send a different signal: `kill -s INT %1`

[% single src/kill_int.text %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Where Do Processes Come From?" %]

-   [%g fork "Fork" %] creates a duplicate of a process
    -   Creator is parent, gets process ID of child as return value
    -   Child gets 0 as return value (but has something else as its process ID)

[% multi src/fork.py out/fork.out %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Flushing I/O" %]

-   Example above works interactively
-   Run as `python fork.py > temp.out`, the "starting" line is duplicated
-   [% todo "explain I/O flushing" %]

[% multi src/flush.py %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Appendices" %]

### Terms

[% glossary %]

### Acknowledgments

[% thanks %]

### Links

[% link_table %]

### To Do

-   What is Docker and why do I care?
    -   Introduce it early so people don't screw up their laptop
-   How can I find things on my system?
    -   `find | xargs` and alternatives
-   What is `sudo` and when should I use it?
-   How can I found out what kind of system I'm using (`uname`)
-   How do I see who has accounts on a machine?
-   How do I create a new account?
-   How do I delete an account?
-   How do I see who owns a file?
-   What does it actually mean to own a file?
-   What other kinds of permissions are there?
-   How can I specify what program to use to run a file?
-   How can I tell what kind of file a file is?
-   How can I see what processes are running on a computer (`ps`, `pgrep`, `top`)?
-   How can I see what's using a computer's processor/memory/disk/network?
-   How are files and directories stored (i.e., what is an inode)?
-   How can I see how much disk space is in use (`df`, `du`)?
-   When is a file not a file?
-   How can I create a shortcut (link) for a file?
-   What is a port?
-   How can I tell which ports are being used and by which processes?
-   How can I run a job repeatedly (`cron` and `watch`)?
-   How do new programs start (the fork/exec model)?
-   What does it mean to suspend, background, or foreground a process?
-   How can I interrupt a process (`kill`, `pkill`) and what kinds of interrupts are there?
-   What is a process group?
-   What are keys and how do I manage them?
-   What are certificates and how do I manage them?
-   How can I run a web server?
-   What other services might I want to run, when, and why?
-   How can I change my identity (sudo)?
-   How can I check my network connection (ping, traceroute)?
-   What is an IP address?
-   How can I connect to another computer (ssh)?
-   What is a user group and why do I care?
-   How can I view the computer's system log and what will I find there?
-   What are virtual environments and when would I use one?
-   How does package installation work?
    -   For Unix and for Python and why they are different
-   How does authentication work?
-   What are alternatives to classic password authentication?

[% section_end %]
