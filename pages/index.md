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

[% exercise %]
What does the `pgrep` command do?

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Parent and Child Processes" %]

-   Every process is created by another process
    -   Except the first
-   Refer to [%g child_process "child process" %] and [%g parent_process "parent process" %]
-   `echo $$` shows [%g process_id "process ID" %] of current process
    -   `$$` shortcut because it's used so often
-   `echo $PPID` (parent process ID) to get parent
-   `pstree $$` to see [%g process_tree "process tree" %]

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

-   Can run a process in the [%g background_process "background" %]
    -   Only difference is that it's not connected to the terminal

[% multi src/show_timer.py src/show_timer.sh out/show_timer.out %]

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
[% section_break class="topic" title="Fork" %]

-   [%g fork_process "Fork" %] creates a duplicate of a process
    -   Creator is parent, gets process ID of child as return value
    -   Child gets 0 as return value (but has something else as its process ID)

[% multi src/fork.py out/fork.out %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Flushing I/O" %]

-   Example above works interactively
-   Run as `python fork.py > temp.out`, the "starting" line is duplicated
-   [% todo "explain I/O flushing" %]

[% single src/flush.py %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Exec" %]

-   The `exec` family of functions in `os` execute a new program *inside the calling process*
    -   Replace existing program and start a new one
-   So `fork`/`exec` to run a program

[% multi src/fork_exec.py out/fork_exec.out %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="exercise" %]

[% exercise %]
What are the differences between `os.execl`, `os.execlp`, and `os.execv`?
When and why would you use each?

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Shell Variables" %]

-   The shell is a program and programs have variables
-   Create or change with <code><em>name</em>=<em>value</em></code>
-   [%g shell_var "Shell variable" %] stays in the process
-   Use <code>$<em>name</em></code> to get value
    -   Because people type file and directory names more often

[% multi src/shell_var_outer.sh src/shell_var_inner.sh out/shell_var_outer.out %]

-   Note: variables usually written in upper case to distinguish them from filenames
    -   So underscores as separators

<!-- ---------------------------------------------------------------- -->
[% section_break class="exercise" %]

[% exercise %]
What happens if you modify the scripts shown above
to use single quotes instead of double quotes?

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Environment Variables" %]

-   [%g env_var "Environment variable" %] is inherited by new processes
-   Use <code>export <em>name</em>=<em>value</em></code>

[% multi src/env_var_outer.sh src/env_var_inner.sh out/env_var_outer.out %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="exercise" %]

[% exercise %]
If a child process sets shell or environment variables,
are they visible in the parent once the child finishes executing?

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Environment Variables in Programs" %]

-   Environment variables are inherited by child process…
-   …so they are inherited by programs (not just shell scripts)

[% multi src/env_var_py.sh src/env_var_py.py out/env_var_py.out %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Inspecting Variables" %]

-   `set` on its own lists variables, functions, etc.
-   `env` shows all environment variables

[% multi src/show_env_vars.sh out/show_env_vars.out %]

-   Many tools create variables to manage configuration
    -   No guarantees that they don't collide with each other

<!-- ---------------------------------------------------------------- -->
[% section_break class="exercise" %]

[% exercise %]
The `os.environ` variable in Python's `os` module
is an easy way to get all of the process's environment variables.
Compare it to what `env` shows.
Are there differences?
If so, what are they and why do they exist?

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Important Environment Variables" %]

| Name     | Typical Value    | Purpose                           |
| -------- | ---------------- | --------------------------------- |
| `EDITOR` | `nano`           | default text editor               |
| `HOME`   | `/Users/tut`     | user's home directory             |
| `LANG`   | `en_CA.UTF-8`    | user's preferred (human) language |
| `PATH`   | see below        | search path for programs          |
| `PWD`    | `/Users/tut/sys` | present working directory         |
| `SHELL`  | `/bin/bash`      | user's default shell              |
| `TERM`   | `xterm-256color` | type of terminal                  |
| `TMPDIR` | `/var/tmp`       | storage for temporary files       |
| `USER`   | `tut`            | current user's name               |

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Search Path" %]

-   `PATH` holds a colon-separated list of directories
-   Shell looks in these *in order* to find commands
-   Looking at them all on one line is annoying, so use `tr` to split

[% multi src/show_path.sh out/show_path.out %]

-   Notice `/Users/tut/bin`
-   Common to have a `~/bin` directory with the user's own utilities

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Adding to the Search Path" %]

-   Shell variables (of both kinds) are just strings
-   So redefine the variable to the old value with a new directory at the front

[% multi src/change_path.sh out/change_path.out %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Startup Files" %]

-   Bash shell runs commands in `~/.bash_profile` for login shells
-   Bash shell runs commands in `~/.bashrc` for interactive shells
-   Yes, the terminology is confusing
-   Common to have `~/.bash_profile` [%g source_shell "source" %] `~/.bashrc`
    -   I.e., run those commands in the current shell

[% single src/source_bashrc.sh %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Command Interpolation" %]

-   Can use <code>outer $(<em>inner</em>)</code> to run `inner` and use its output as arguments to `outer`
-   Long-winded way to count lines in some text files

[% multi src/interpolate.sh out/interpolate.out %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="exercise" %]

[% exercise %]
Removing a directory from `PATH` is harder than adding one.
Write a shell script that:

1.  Splits `PATH` on colons to put one entry on each line.
2.  Uses `grep` to remove the undesired line.
3.  Uses `paste -s -d :` to recombine the lines.
4.  Uses command interpolation to assign the result back to `PATH`.

This exercise may remind you why complicated operations should be done in Python
rather than in the shell.

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Virtual Environments" %]

-   If two directories `A` and `B` contain a program `xyz` and `A` comes before `B`,
    `xyz` on its own will run `A/xyz` instead of `B/xyz`
-   This is how [%g virtual_env "virtual environments" %] work

[% multi src/show_virtual_env.sh out/show_virtual_env.out %]

-   Virtual environment is initially a minimal Python installation
-   Installing new packages puts them in the environment's directory

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Package Installation" %]

1.  Create a new virtual environment called `example`: `conda create -n example python=3.12`
2.  Activate that virtual environment: `conda activate example`
3.  Install the `faker` package: `pip install faker`

[% multi src/find_faker.sh out/find_faker.out %]

-   The script in `bin` loads the module and runs it

[% single src/faker_bin.py %]

-   The directory under `site-packages` has 642 Python files (as of version 24.3.0)
-   The `python` in the virtual environment' `bin` directory
    knows to look in that environment's `site-packages` directory

<!-- ---------------------------------------------------------------- -->
[% section_break class="exercise" %]

[% exercise %]
What is the `re.sub` call in the `faker` script doing and why?

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Limits of Virtual Environments" %]

-   `conda` and `python -m venv` work for Python
-   But what about Rust, JavaScript, and other languages?
-   In particular, what if you need an isolated environment for several languages at once?
-   And you want other people to be able to reproduce it?

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
-   How can I see what's using a computer's processor/memory/disk/network?
-   How are files and directories stored (i.e., what is an inode)?
-   How can I see how much disk space is in use (`df`, `du`)?
-   When is a file not a file?
-   How can I create a shortcut (link) for a file?
-   What is a port?
-   How can I tell which ports are being used and by which processes?
-   How can I run a job repeatedly (`cron` and `watch`)?
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
-   How does package installation work?
    -   For Unix and for Python and why they are different
-   How does authentication work?
-   What are alternatives to classic password authentication?

[% section_end %]
