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
[% section_break class="aside" title="Start with Something Simple" %]

[% multi "src/get_remote.py" "out/get_remote.out" %]

-   Use the [`requests`][requests] module (needs to be installed)
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

[% multi "src/dump_structure.py" "out/dump_structure.out" %]

-   First line is [%g http_method "method" %], URL, and protocol version
-   Every HTTP request can have [%g http_header "headers" %] with extra information
-   And optionally data being uploaded (which we will see later)
-   Yes, it's all just text

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Response Structure" %]

[% multi "src/response_headers.py" "out/response_headers.out" %]

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

[% multi "src/get_404.py" "out/get_404.out" %]

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

[% multi "src/get_json.py" "out/get_json.out" %]

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

[% single "src/local_server.sh" %]

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

[% multi "src/get_local.py" "out/get_local.out" %]

-   [%g concurrency "Concurrent" %] systems are hard to debug
    -   Multiple streams of activity
    -   Order may change from run to run
-   Use `S` and `c` to show output from server and client respectively

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Our Own File Server" %]

[% single "src/file_server_unsafe.py" keep="do_get" %]

-   Our `RequestHandler` handles a single HTTP request
    -   More specifically, handles the `GET` method
-   Combine working directory with requested file path to get local path to file
-   Return that if it exists and is a file or raise an error

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Support Code" %]

-   Send content

[% single "src/file_server_unsafe.py" keep="send_content" %]

-   Handle errors

[% single "src/file_server_unsafe.py" keep="error_page" %]
[% single "src/file_server_unsafe.py" keep="handle_error" %]

-   Define our own exceptions so we're sure we're only catching what we expect

[% single "src/file_server_unsafe.py" keep="exception" %]

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Running Our File Server" %]

[% single "src/file_server_unsafe.py" keep="main" %]

-   And then get `motto.txt` as before

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Built-in Safety" %]

-   Modify `requests` script to take URL as command-line parameter

[% single "src/get_url.py" %]

-   Add a sub-directory to `site` called `sandbox` with a file `example.txt`
-   Serve that sub-directory

[% single "src/file_server_sandbox.sh" %]

-   Can get files from that directory

[% multi "src/get_url_allowed.sh" "out/get_url_allowed_server.out" "out/get_url_allowed_client.out" %]

-   But not from parent directory (which isn't part of sandbox)

[% multi "src/get_url_disallowed.sh" "out/get_url_disallowed_server.out" "out/get_url_disallowed_client.out" %]

-   But why not?
-   Looks like `requests` is stripping the leading `..` off the path
-   And if we try that URL in the browser, same thing happens
-   So we're safe, right?

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Introducing netcat" %]

-   [`netcat`][netcat] (often just `nc`) is a computer networking tool
-   Open a connection, send exactly what the user types, and show exactly what is sent in response

[% multi "src/nc_localhost.sh" "src/nc_allowed.text" "out/nc_allowed.out" %]

-   So far so good, but:

[% multi "src/nc_disallowed.text" "out/nc_disallowed.out" %]

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

[% single "src/file_server_safe.py" keep="handle_file" %]

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

[% multi "src/birds_head.sh" "out/birds_head.out" %]

-   Modify server to generate it dynamically
-   Main program

[% single "src/bird_server_whole.py" keep="main" %]

-   Create our own server class because we want to pass the dataframe in the constructor

[% single "src/bird_server_whole.py" keep="server" %]

-   `do_GET` converts the dataframe to JSON (will modify later to do more than this)

[% single "src/bird_server_whole.py" keep="get" %]

-   `send_content` [%g character_encoding "encodes" %] the JSON string as [%g utf_8 "UTF-8" %]
    and sets the MIME type to `application/json`

[% single "src/bird_server_whole.py" keep="send" %]

-   Can view in browser at `http://localhost:8000` or use `requests` to fetch as before

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Slicing Data" %]

-   URL can contain [%g query_parameter "query parameters" %]
-   Want `http://localhost:8000/?year=2021&species=rebnut` to select red-breasted nuthatches in 2021
-   Put slicing in a method of its own

[% single "src/bird_server_slice.py" keep="get" %]

-   Use `urlparse` and `parse_qs` from [`urllib.parse`][py_urllib_parse] to get query parameters
    -   (Key, list) dictionary
-   Then filter data as requested

[% single "src/bird_server_slice.py" keep="filter" %]

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

[% single "src/bird_client_password.py" %]
[% multi "src/bird_client_password_correct.sh" "out/bird_client_password_correct.out" %]
[% multi "src/bird_client_password_incorrect.sh" "out/bird_client_password_incorrect.out" %]

-   First change to server: get the password on the command line and save it

[% single "src/bird_server_password.py" keep="main" %]
[% single "src/bird_server_password.py" keep="server" %]

-   Second change: add authorization to `do_GET`
    -   Once again use our own exception class to handle unhappy cases

[% single "src/bird_server_password.py" keep="get" %]

-   Add authorization that checks header value

[% single "src/bird_server_password.py" keep="auth" %]

-   Handle errors by constructing JSON

[% single "src/bird_server_password.py" keep="error" %]

-   It works but:
    -   One password for everyone
    -   Sent as [%g cleartext "cleartext" %] over an unencrypted connection

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Basic Authentication" %]

-   Modify `do_GET`

[% single "src/bird_server_basicauth.py" keep="get" %]

-   [Basic HTTP authentication][basic_http_auth]:
    -   Header called `"Authorization"`
    -   Value is <code>Basic <em>data</em></code>
    -   Data is [%g base64 "base-64 encoded" %] <code><em>username</em>:<em>password</em></code>
-   Most of the code is checking that everything is OK and responding properly if it's not
-   Test client

[% single "src/bird_client_basicauth.py" %]
[% single "src/bird_client_basicauth_correct.sh" %]

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
[% section_break class="aside" title="Appendices" %]

### Terms

[% glossary %]

### Acknowledgments

[% thanks %]

### Links

[% link_table %]

[% section_end %]
