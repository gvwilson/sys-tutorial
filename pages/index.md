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

[%inc "src/ps_a_l.sh" "out/ps_a_l.out" %]

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

[%inc src/catch_interrupt.py out/catch_interrupt.out %]

-   `^C` shows where user typed Ctrl-C

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Background Processes" %]

-   Can run a process in the [%g background_process "background" %]
    -   Only difference is that it's not connected to the terminal

[%inc src/show_timer.py src/show_timer.sh out/show_timer.out %]

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

[%inc src/ctrl_z_background.text %]

-   Note that input and output are mixed together

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Killing Processes" %]

-   Use `kill` to send a signal to a process
    -   Not necessarily to stop it

[%inc src/kill_process.text %]

-   By default, `kill` sends `SIGTERM` (terminate process)
-   Variations:
    -   Give a process ID: `kill 1234`
    -   Send a different signal: `kill -s INT %1`

[%inc src/kill_int.text %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Fork" %]

-   [%g fork_process "Fork" %] creates a duplicate of a process
    -   Creator is parent, gets process ID of child as return value
    -   Child gets 0 as return value (but has something else as its process ID)

[%inc src/fork.py out/fork.out %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Flushing I/O" %]

-   Example above works interactively
-   Run as `python fork.py > temp.out`, the "starting" line is duplicated
-   [% todo "explain I/O flushing" %]

[%inc src/flush.py out/flush.out %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Exec" %]

-   The `exec` family of functions in `os` execute a new program *inside the calling process*
    -   Replace existing program and start a new one
-   So `fork`/`exec` to run a program

[%inc src/fork_exec.py out/fork_exec.out %]

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

[%inc src/shell_var_outer.sh src/shell_var_inner.sh out/shell_var_outer.out %]

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

[%inc src/env_var_outer.sh src/env_var_inner.sh out/env_var_outer.out %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="exercise" %]

[% exercise %]
If a child process sets shell or environment variables,
are they visible in the parent once the child finishes executing?

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Environment Variables in Programs" %]

-   Environment variables are inherited by child process…
-   …so they are inherited by programs (not just shell scripts)

[%inc src/env_var_py.sh src/env_var_py.py out/env_var_py.out %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Inspecting Variables" %]

-   `set` on its own lists variables, functions, etc.
-   `env` shows all environment variables

[%inc src/show_env_vars.sh out/show_env_vars.out %]

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

[%inc src/show_path.sh out/show_path.out %]

-   Notice `/Users/tut/bin`
-   Common to have a `~/bin` directory with the user's own utilities

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Adding to the Search Path" %]

-   Shell variables (of both kinds) are just strings
-   So redefine the variable to the old value with a new directory at the front

[%inc src/change_path.sh out/change_path.out %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Startup Files" %]

-   Bash shell runs commands in `~/.bash_profile` for login shells
-   Bash shell runs commands in `~/.bashrc` for interactive shells
-   Yes, the terminology is confusing
-   Common to have `~/.bash_profile` [%g source_shell "source" %] `~/.bashrc`
    -   I.e., run those commands in the current shell

[%inc src/source_bashrc.sh %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Command Interpolation" %]

-   Can use <code>outer $(<em>inner</em>)</code> to run `inner` and use its output as arguments to `outer`
-   Long-winded way to count lines in some text files

[%inc src/interpolate.sh out/interpolate.out %]

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

[%inc src/show_virtual_env.sh out/show_virtual_env.out %]

-   Virtual environment is initially a minimal Python installation
-   Installing new packages puts them in the environment's directory

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Package Installation" %]

1.  Create a new virtual environment called `example`: `conda create -n example python=3.12`
2.  Activate that virtual environment: `conda activate example`
3.  Install the `faker` package: `pip install faker`

[%inc src/find_faker.sh out/find_faker.out %]

-   The script in `bin` loads the module and runs it

[%inc src/faker_bin.py %]

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
-   We will build something worth installing and then return to this problem

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Start with Something Simple" %]

[%inc src/get_remote.py out/get_remote.out %]

-   Use the [`requests`][requests] module to send an [%g http "HTTP" %] [%g http_request "request" %]
-   The URL identifies the file we want
    -   Though as we'll see, the server can interpret it differently
-   Response includes:
    -   [%g http_status_code "HTTP status code" %] such as 200 (OK) or 404 (Not Found)
    -   The text of the response

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="What Just Happened" %]

[% figure
   file="img/http_lifecycle.svg"
   title="Lifecycle of an HTTP request and response"
   alt="HTTP request/response lifecycle"
%]

-   Open a connection to the server
-   Send an [%g http_request "HTTP request" %] for the file we want
-   Server creates a [%g http_response "response" %] that includes the contents of the file
-   Sends it back
-   `requests` parses the response and creates a Python object for us

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Request Structure" %]

[%inc src/dump_structure.py out/dump_structure.out %]

-   First line is [%g http_method "method" %], URL, and protocol version
-   Every HTTP request can have [%g http_header "headers" %] with extra information
-   And optionally data being uploaded (which we will see later)
-   Yes, it's all just text

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Response Structure" %]

[%inc src/response_headers.py out/response_headers.out %]

-   Every HTTP response also has with extra information
    -   Does *not* include status code: that appears in the first line
-   Most important for now are:
    -   `Content-Length`: number of bytes in response data (i.e., how much to read)
    -   `Content-Type`: [%g mime_type "MIME type" %] of data (e.g., `text/plain`)
-   From now on we will only show interesting headers

<!-- ---------------------------------------------------------------- -->
[% section_break class="exercise" %]

[% exercise %]
Add header called `Studying` with the value `safety` to the `requests` script shown above.
Does it make a difference to the response?
Should it?

[% exercise %]
What is the difference between the `Content-Type` and the `Content-Encoding` headers?

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="When Things Go Wrong" %]

[%inc src/get_404.py out/get_404.out %]

-   The 404 status code tells us something went wrong
-   The 9 kilobyte response is an HTML page with an embedded image (the GitHub logo)
-   The page contains human-readable error messages
    -   But we have to know page format to pull them out

<!-- ---------------------------------------------------------------- -->
[% section_break class="exercise" %]

[% exercise %]
Look at [this list of HTTP status codes][http_status_codes].

1.  What is the difference between status code 403 and status code 404?

2.  What is status code 418 used for?

3.  Under what circumstances would you expect to get a response whose status code is 505?

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Getting JSON" %]

[%inc src/get_json.py out/get_json.out %]

-   Parsing data out of HTML is called [%g web_scraping "web scraping" %]
    -   Painful and error prone
-   Better to have the server return data as data
    -   Preferred format these days is [%g json "JSON" %]
    -   So common that `requests` has built-in support
-   There is no standard for representing tabular data as JSON
    -   A list with one list with column names + N lists of values
    -   A list with N dictionaries, all with the same keys
    -   A dictionary with column names and lists of values, all the same length

<!-- ---------------------------------------------------------------- -->
[% section_break class="exercise" %]

[% exercise %]
Write a `requests` script that gets the current location and crew roster
of [the International Space Station][iss_api].

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Local Web Server" %]

[%inc src/local_server.sh %]

-   Pushing files to GitHub so that we can use them is annoying
-   And we want to show how to make things *wrong* so that we can then make them *right*
-   Use Python's [`http.server`][py_http_server] module
    to run a [%g local_server "local server" %]
    -   Host name is [%g localhost "`localhost`" %]
    -   Uses [%g port "port" %] 8000 by default
    -   So URLs look like `http://localhost:8000/path/to/file`
-   `-d site` tells the server to use `site` as its root directory
-   Use this local server for the next few examples
    -   Build our own server later on to show how it works

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Talk to Local Server" %]

[%inc src/get_local.py out/get_local.out %]

-   [%g concurrency "Concurrent" %] systems are hard to debug
    -   Multiple streams of activity
    -   Order may change from run to run
-   Use `S` and `c` to show output from server and client respectively

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Our Own File Server" %]

[%inc src/file_server_unsafe.py keep=do_get %]

-   Our `RequestHandler` handles a single HTTP request
    -   More specifically, handles the `GET` method
-   Combine working directory with requested file path to get local path to file
-   Return that if it exists and is a file or raise an error

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Support Code" %]

-   Send content

[%inc src/file_server_unsafe.py keep=send_content %]

-   Handle errors

[%inc src/file_server_unsafe.py keep=error_page %]
[%inc src/file_server_unsafe.py keep=handle_error %]

-   Define our own exceptions so we're sure we're only catching what we expect

[%inc src/file_server_unsafe.py keep=exception %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Running Our File Server" %]

[%inc src/file_server_unsafe.py keep=main %]

-   And then get `motto.txt` as before

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Built-in Safety" %]

-   Modify `requests` script to take URL as command-line parameter

[%inc src/get_url.py %]

-   Add a sub-directory to `site` called `sandbox` with a file `example.txt`
-   Serve that sub-directory

[%inc src/file_server_sandbox.sh %]

-   Can get files from that directory

[%inc src/get_url_allowed.sh out/get_url_allowed_server.out out/get_url_allowed_client.out %]

-   But not from parent directory (which isn't part of sandbox)

[%inc src/get_url_disallowed.sh out/get_url_disallowed_server.out out/get_url_disallowed_client.out %]

-   But why not?
-   Looks like `requests` is stripping the leading `..` off the path
-   And if we try that URL in the browser, same thing happens
-   So we're safe, right?

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Introducing netcat" %]

-   [`netcat`][netcat] (often just `nc`) is a computer networking tool
-   Open a connection, send exactly what the user types, and show exactly what is sent in response

[%inc src/nc_localhost.sh src/nc_allowed.text out/nc_allowed.out %]

-   So far so good, but:

[%inc src/nc_disallowed.text out/nc_disallowed.out %]

-   We shouldn't be able to see files outside the sandbox
-   But if someone doesn't strip out the `..` characters, users can escape

<!-- ---------------------------------------------------------------- -->
[% section_break class="exercise" %]

[% exercise %]
The shortcut <code>~<em>username</em></code> means "the specified user's home directory" in the shell,
while `~` on its own means "the current user's home directory".
create a file called `test.txt` in your home directory
and then try to get `~/test.txt` using your browser,
`requests`,
and Telnet.
What happens with each and why?

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="A Safer File Server" %]

[%inc src/file_server_safe.py keep=handle_file %]

-   [%g resolve_path "Resolve" %] the constructed path
-   Check that it's below the current working directory (i.e., the sandbox)
-   Fail if not
    -   Using `ServerException` guarantees that all errors are handled the same way

<!-- ---------------------------------------------------------------- -->
[% section_break class="exercise" %]

[% exercise %]
[%g refactor "Refactor" %] the `do_GET` and `handle_file` methods in `RequestHandler`
so that all checks are in one place.
Does this make the code easier to understand overall?
Do you think making code easier to understand also makes it safer?

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Serving Data" %]

-   Rarely have JSON lying around as [%g static_file "static files" %]

[%inc src/birds_head.sh out/birds_head.out %]

-   Modify server to generate it dynamically
-   Main program

[%inc src/bird_server_whole.py keep=main %]

-   Create our own server class because we want to pass the dataframe in the constructor

[%inc src/bird_server_whole.py keep=server %]

-   `do_GET` converts the dataframe to JSON (will modify later to do more than this)

[%inc src/bird_server_whole.py keep=get %]

-   `send_content` [%g character_encoding "encodes" %] the JSON string as [%g utf_8 "UTF-8" %]
    and sets the MIME type to `application/json`

[%inc src/bird_server_whole.py keep=send %]

-   Can view in browser at `http://localhost:8000` or use `requests` to fetch as before

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Slicing Data" %]

-   URL can contain [%g query_parameter "query parameters" %]
-   Want `http://localhost:8000/?year=2021&species=rebnut` to select red-breasted nuthatches in 2021
-   Put slicing in a method of its own

[%inc src/bird_server_slice.py keep=get %]

-   Use `urlparse` and `parse_qs` from [`urllib.parse`][py_urllib_parse] to get query parameters
    -   (Key, list) dictionary
-   Then filter data as requested

[%inc src/bird_server_slice.py keep=filter %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="exercise" %]

[% exercise %]
Write a function that takes a URL as input
and returns a dictionary whose keys are the query parameters' names
and whose values are lists of their values.
Do you now see why you should use the library function to do this?

[% exercise %]
Modify the server so that clients can specify which columns they want returned
as a comma-separated list of names.
If the client asks for a column that doesn't exist, ignore it.

[% exercise %]
Modify your solution to the previous exercise so that
if the client asks for a column that doesn't exist
the server returns a status code 400 (Bad Request)
and a JSON blog with two keys:
`status_code` (set to 400)
and `error_message` (set to something informative).
Explain why the server should return JSON rather than HTML in the case of an error.

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="What's the Magic Word?" %]

-   Only allow access to data if client:
    -   [%g authentication "Authenticates" %] (i.e., establishes their identity)
    -   Is [%g authorization "authorized" %] (i.e., has the right to view the data)
-   Simplest possible is wrong in many ways: does the client know a password?

[%inc src/bird_client_password.py %]
[%inc src/bird_client_password_correct.sh out/bird_client_password_correct.out %]
[%inc src/bird_client_password_incorrect.sh out/bird_client_password_incorrect.out %]

-   First change to server: get the password on the command line and save it

[%inc src/bird_server_password.py keep=main %]
[%inc src/bird_server_password.py keep=server %]

-   Second change: add authorization to `do_GET`
    -   Once again use our own exception class to handle unhappy cases

[%inc src/bird_server_password.py keep=get %]

-   Add authorization that checks header value

[%inc src/bird_server_password.py keep=auth %]

-   Handle errors by constructing JSON

[%inc src/bird_server_password.py keep=error %]

-   It works but:
    -   One password for everyone
    -   Sent as [%g cleartext "cleartext" %] over an unencrypted connection

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Basic Authentication" %]

-   Modify `do_GET`

[%inc src/bird_server_basicauth.py keep=get %]

-   [Basic HTTP authentication][basic_http_auth]:
    -   Header called `"Authorization"`
    -   Value is <code>Basic <em>data</em></code>
    -   Data is [%g base64 "base-64 encoded" %] <code><em>username</em>:<em>password</em></code>
-   Most of the code is checking that everything is OK and responding properly if it's not
-   Test client

[%inc src/bird_client_basicauth.py %]
[%inc src/bird_client_basicauth_correct.sh %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Changing the Root Directory" %]

-   The `chroot` command
    -   Changes the process's idea of the [%g root_directory "root directory" %]
    -   Runs a command
-   But…

[%inc src/chroot_example.sh out/chroot_example.out %]

-   Need special permission (discussed below)
-   Everything needed to run `echo` and other commands needs to be in the new filesystem
-   Only isolates the filesystem

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="sudo" %]

-   Every machine has a [%g superuser "superuser" %] account called [%g root_user "root" %]
    -   Which has nothing to do with the root directory of the filesystem
-   Use `sudo` ("superuser do") to change identity temporarily

[%inc src/sudo_example.sh out/sudo_example.out %]

-   At least it's a different error message…
-   `sudo` is a way to give yourself permission to mess up everything on your computer
-   So another requirement for virtual environments:
    break them without breaking anything else

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Docker" %]

-   [Docker][docker] solves all of these problems
-   Define an [%g docker_image "image" %] with its own copy of the operating system, filesystem, etc.
-   Run it in a [%g docker_container "container" %] that is isolated from the rest of your computer

[%inc src/docker_image_ls.sh out/docker_image_ls.out %]
[%inc src/docker_container_ls.sh out/docker_container_ls.out %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Common Error Message" %]

-   Docker requires a [%g daemon "daemon" %] process to be running in the background to start images

[%inc src/docker_image_ls.sh out/docker_image_ls_err.out %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Running a Container" %]

[%inc src/docker_run_fresh.text %]

-   Ask Docker to run a container with `ubuntu:latest`
    -   I.e., latest stable version of Ubuntu Linux from [Docker Hub][docker_hub]
-   Docker can't find a [%g cache "cached" %] copy locally, so it downloads the image
-   Then runs it
-   But its default command is `/bin/bash` with no inputs, so it exits immediately.

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Re-running a Container" %]

[%inc src/docker_run_again.text %]

-   Doesn't need to download again
-   Runs the given command instead of the default `/bin/bash`

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="This Doesn't Work" %]

[%inc src/docker_run_error.text %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Pulling Images" %]

-   Don't have to run immediately

[%inc src/docker_pull.text %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="What Have We Got?" %]

[%inc src/os_release.text %]

-   Don't need `:latest` every time (defaults)

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Inside the Container" %]

[%inc src/docker_run_interactive.text %]

-   `-i`: interactive
-   `-t`: terminal (kind of)
    -   Combination often abbreviated `-it`
-   The hexadecimal number after `root@` is the container's unique ID

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Persistence" %]

[%inc src/docker_run_nonpersistent.text %]

-   Container starts fresh each time it runs
-   Notice that the container's ID changes each time it runs

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="What Is Running" %]

[%inc src/docker_container_ls_id.text %]

-   `docker container ls` on its own shows a wide table
-   Use [Go][golang] format strings to format output (no, really)

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Installing Software" %]

[%inc src/docker_install_python.text %]

-   `apt update` to update available package lists
-   `apt install` to install the desired package
    -   Installs lots of dependencies as well
-   Doesn't create `python` (note lack of output)
-   Creates `python3` instead
-   Version is most recent in the default repository
-   But *it isn't there the next time we run*

[%inc src/docker_install_python_nonpersistent.text %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Actually Installing Software" %]

-   Create a Dockerfile
    -   Usually called that and in a directory of its own
    -   Ours is `src/ubuntu_python3/Dockerfile`

[%inc src/ubuntu_python3/Dockerfile %]

-   Tell docker to build the image

[%inc src/ubuntu_python3_build.text %]

-   `CACHED` because we've run this several times while building this tutorial

[%inc src/ubuntu_python3_run.text %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Layers" %]

[%inc src/docker_image_history.text %]

-   Docker images are built in layers
-   Layers can be shared between images to reduce disk space

[%inc src/docker_system_df.text %]

-   First line (`Images`) shows actual disk space
    -   We'll see the original `df` command again…

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Choosing a Command" %]

-   Add `CMD` with a list of arguments to specify default command when image runs

[%inc src/python3_interpreter/Dockerfile %]

-   Build

[%inc src/python3_interpreter_build.text %]

-   Run

[%inc src/python3_interpreter_run.text %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Appendices" %]

### Terms

[% glossary %]

### Acknowledgments

[% thanks %]

### Links

[% link_table %]

### To Do

-   How can I find things on my system?
    -   `find | xargs` and alternatives
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
-   How can I check my network connection (ping, traceroute)?
-   What is an IP address?
-   How can I connect to another computer (ssh)?
-   What is a user group and why do I care?
-   How can I view the computer's system log and what will I find there?
-   What are alternatives to classic password authentication?

[% section_end %]
