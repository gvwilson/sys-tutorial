> This legacy material will be revised heavily.
> Please see the `README.md` in the root directory of <[%config repo %]>
> for a partial list of topics the tutorial will cover.

<!-- ---------------------------------------------------------------- -->
[% section_start class="aside" title="What This Is" %]

-   Notes and working examples that instructors can use to perform a lesson
    -   Do *not* expect novices with no prior Python or Unix experience to be able to learn from them
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
    -   They learned Python in an intensive 16-week data science bootcamp program
        and are comfortable working with Unix command-line tools,
        writing data analysis programs in Python,
	and downloading data from the web to use in those programs
    -   Ning wants to build real-time dashboards for people in the Ministry,
        but doesn't understand how to do that
	without exposing confidential data or opening the Ministry up to attack
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
        -   `*` and `?` wildcards; shell variable with `$` expansion; `for` loop;
            shell scripts with numbered arguments; the `PATH` variable; `$(…)` expansion
    -   Git commands and workflow covered in [this Software Carpentry lesson][sc_git]
        -   `git config` to set username, email address, and editor; `git init`;
            `git status`; `git checkout`; `git add`; `git diff` (current state and history);
            `git commit`; `git log`; `git merge`; `git remote`; `.gitignore`
        -   Git vs. GitHub; local and remote repositories; authentication with SSH keys;
            branching; merging; conflicts; pull requests; code review
    -   Python for command-line scripting
        -   variables; numbers and strings; lists; dictionaries; `for` and `while` loops;
	    `if`/`else`; `with`; defining and calling functions; `sys.argv`, `sys.stdin`,
	    and `sys.stdout`; simple regular expressions; reading JSON data;
	    reading CSV files using [Pandas][pandas] or [Polars][polars]
        -   `pip install` (but not virtual environments); `ruff` for linting;
	    `pytest` (but not mock objects); writing docstrings
-   Learning outcomes
    1.  Create a virtual environment and explain what this actually does.
    1.  Create `requirements.txt` file for [`pip`][pip] and explain version pinning.
    1.  Explain what a filesystem is (disk partitions, inodes, symbolic links)
        and use `df`, `ln`, similar commands to explore with them.
    1.  Use Python in place of shell scripts:
        1.  Operate on files matching glob patterns.
        1.  Create/delete directories.
        1.  Explain how Unix permissions work and read/modify them.
	1.  Explain how file hashing works and how to use it in programs.
    1.  Describe the HTTP request/response cycle and the format of HTTP requests and responses.
    1.  Write scripts to fetch data programmatically from HTTP servers.
    1.  Create digital certificates to enable HTTPS.
    1.  Create and use authentication tokens for API access.
    1.  Manage processes using `ps`, `kill`, and related commands.
-   TODO:
    -   what to teach about Docker and why?
    -   what to teach about continuous integration, using what system?
    -   what to teach about batch jobs, using what system?
    -   what to teach about cron jobs (if anything)?
    -   what if anything to teach about networking, firewalls, certificates, etc.?

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="What We're Going to Do" %]

1.  Show how the basic components of the web work.
1.  Build a simple application that serves up data from files and a database.
1.  Fix its safety issues one by one.
1.  Along the way, introduce ideas about processes, file systems, certificates, and related topics.

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Setup" %]

-   Download [the latest release]([% config "release" %])
-   Unzip the file in a temporary directory to create:
    -   `./src/*.*`: shell scripts and Python programs
    -   `./site/*.*`: the pages and data files used in the examples
    -   `./out/*.*`: expected output for examples

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Securing the Server" %]

-   Two components
    -   Give the server a [%g digital_certificate "digital certificate" %] so that it can establish its identity
    -   Have the client communicate with it via [%g https HTTPS %] (the encrypted version of HTTP)
-   Certificate has private and public components
    -   Answer questions with '.' to skip
    -   `-nodes` is short for "no DES" so there isn't an interactive password on the certificate

[% single "src/create_pem.sh" %]
[% single "site/server_first_cert.pem" %]

-   Modify file server to listen for secure connections on port 1443
    -   [%g wrap_object "Wrap" %] the server's [%g socket "socket" %] with a layer of security
    -   Everything else stays the same

[% single "src/file_server_secure.py" keep="main" %]

-   Run it like this

[% single "src/file_server_secure.sh" %]

-   Point browser at `https://localhost:1443/motto.txt`
    -   Must have *both* `https` *and* the port `1443`

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Securing the Client" %]

-   Try `requests.get("https://localhost:1443/test.txt")`

[% single "out/requests_secure_no_verify.out" %]

-   Fair enough: `requests` shouldn't trust self-signed certificates by default
-   Can tell it not to check at all by passing `verify=False` but turning off security is a bad idea
-   Try `requests.get("https://localhost:1443/test.txt", verify="cert.pem")`
    -   I.e., pass it the server's certificate

[% single "out/requests_secure_server_cert.out" %]

-   What we actually need is to sign the server's certificate with a certificate from some authority,
    then tell `requests` it can use the authority's certificate to check the server's certificate
    -   Seems roundabout, but it allows us to use a few hundred trusted certificates to check everyone else's
-   `import certifi` and `certifi.where()` to see the PEM file that `requests` uses by default

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Starting Over" %]

-   Pretend to be our own [%g certificate_authority "certificate authority" %] (CA)
-   Use our CA certificate to [%g digital_signature "sign" %] the server's certificate
    -   We can use the CA to sign any number of certificates

[% single "src/create_signed_cert.sh" %]

-   Run the server with the newly-created certificate

[% single "src/file_server_signed.sh" %]

-   Point `requests` at the CA certificate
    -   Which it then uses to check that the server's certificate is properly signed

[% single "src/requests_signed_cert.py" %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="This Is Hard" %]

-   It took a full day and help from three other people to get this working
-   And I'm still not sure what these commands used to sign the server certificate are for

[% single "src/extfile.txt" %]

-   Some of this difficulty is intrinsinc: security really is hard
-   Some is accidental complexity introduced by evolution over time

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Processes" %]

-   We've been running clients and servers interactively
-   How can we automate this?
    -   The heart of [%g deployment "deploying" %] applications
-   A [%g process "process" %] is a running instance of a program
    -   Code plus variables in memory plus open files plus some IDs
-   Tools to manage them were invented when most users only had a single terminal
-   Some repurposed, some replaced: result is unfortunately as messy as certificates

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Viewing Processes" %]

-   Use `ps -a -l` to see currently running processes in terminal
-   Or `ps -a -x` to see (almost) all processes running on computer
    -   `UID`: numeric ID of the user that the process belongs to
    -   `PID`: process's unique ID
    -   `PPID`: ID of the process's parent (i.e., the process that created it)
    -   `CMD`: the command the process is running

[% multi "src/ps_a_l.sh" "out/ps_a_l.out" %]

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

[% multi "src/catch_interrupt.py" "out/catch_interrupt.out" %]

-   `^C` shows where user typed Ctrl-C

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Background Processes" %]

-   Can run a process in the [%g process_background "background" %]
    -   Only difference is that it's not connected to the terminal

[% multi "src/show_timer.py" "src/show_timer.sh" "out/show_timer.out" %]

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

[% single "src/ctrl_z_background.sh" %]

-   Note that input and output are mixed together
-   One of our goals is to build something that will re-run something like this
    *and* show input and output in the order a user would see them
    *while also* labeling input and output correctly

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Killing Processes" %]

-   Use `kill` to send a signal to a process
    -   Not necessarily to stop it

[% single "src/kill_process.sh" %]

-   By default, `kill` sends `SIGTERM` (terminate process)
-   Variations:
    -   Give a process ID: `kill 1234`
    -   Send a different signal: `kill -s INT %1`

[% single "src/kill_int.sh" %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Redirection" %]

[% todo "Explain redirection of standard error (with diagrams)" %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Running Processes Together" %]

-   Want to run a client and server side by side and capture their output
-   First attempt: start the server, wait one second, and run the client
-   When the client finishes, stop the script and its children
    -   Shuts down the server and anything else that may have started

[% single "src/run_2_sleep.sh" %]

-   Use this for the first script and something similar for the second

[% single "src/run_2_left.sh" %]

-   Run it

[% multi "src/run_2_example.sh" "out/run_2_example.out" %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Partial Ordering" %]

-   There are *choose(x+y, x)* ways to interleave two sequences of length *x* and *y*
-   Which is *(x+y)!/x!y!*
-   So two programs that open a file, write a line, and close the file
    can be interleaved in 20 different ways
-   A [%g robustness "robust" %] application works in all 20 ways
    -   Because sleeping for one second is no guarantee
        that another process has run far enough to open a socket

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Listing Open Files" %]

-   Unix tries hard to make (almost) everything look like a file
    -   Read/write as [%g stream "stream" %] or in [%g block_device "blocks" %]
-   In particular, a socket makes a network connection look like a file
-   Use `lsof` to list open files
    -   Operating system keeps track of what "files" a process is interacting with
    -   So we can ask it

[% multi "src/run_lsof.sh" "out/run_lsof.out" %]

-   Which means we can start a process and wait until it opens a particular port

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="A Better Runner" %]

[% single "src/run_and_wait.sh" %]

-   There's a lot going on here
    -   Shell functions
    -   Using `shift` and `$!` to handle arguments
    -   Using `trap` to handle interrupts
    -   Using `printf` instead of `echo`
-   The most important part is the `while` loop
    -   `await_port_listen` function waits for someone to listen to a port
-   We can either learn a new language (shell scripting)
    or figure out how to do this in Python

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Introducing FastAPI" %]

[% single "src/bird_server_fastapi.py" %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="At a Lower Level" %]

[% double stem="socket_server" suffix="py out" %]

-   A [%g socket "socket" %] is a channel between two computers
    -   Makes network I/O look (sort of) like file I/O
-   Our server handles a single request by:
    -   Waiting for a connection
    -   Creating a `Handler` object
    -   Calling its `handle` method
-   And then it closes
-   It responds to requests with an HTTP "OK"

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Sending an HTTP Request" %]

[% double stem="socket_client" suffix="py out" %]

-   Connect to a local server
-   Send an HTTP request
    -   Verb: `GET`
    -   Path: `/motto.txt`
    -   HTTP version
    -   One header identifying the host (because a single address might be home to several)
-   Read data back
    -   First chunk of reply is standard HTTP response with lots of headers,
        including length (in bytes) of content
    -   Second chunk is content
-   You can see why we use `requests`, right?

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Secure Sockets" %]

[% double stem="https_client" suffix="py out" %]

-   There's a lot going on here (which is why we use `requests`)
-   Create a socket and wrap it with [%g tls_ssl "TLS/SSL" %] security
    -   Which GitHub requires
-   Like we said, this is why we use `requests`

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Appendices" %]

### Terms

[% glossary %]

### Acknowledgments

[% thanks %]

### Links

[% link_table %]

[% section_end %]
