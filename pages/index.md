<!-- ---------------------------------------------------------------- -->
[% section_start class="aside" title="what this is" %]

-   notes and working examples that instructors can use to perform a lesson
    -   do *not* expect novices with no prior Python or Unix experience to be able to learn from them
-   musical analogy
    -   this is the chord changes and melody
    -   we expect instructors to create an arrangement and/or improvise while delivering
    -   see [*Teaching Tech Together*][t3] for background
-   please see [the license](./license/) for terms of use,
    the [Code of Conduct](./conduct/) for community standards,
    and [these guidelines](./contributing/) for notes on contributing
-   about the author:
    [Greg Wilson][wilson-greg] is a programmer, author, and educator based in Toronto

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Scope" %]

-   [intended audience][persona]
    -   Ning did a bachelor's degree in economics
        and now works as a data analyst for the Ministry of Health
    -   They learned Python in an intensive 16-week data science bootcamp program
        and are comfortable working with Unix command-line tools
        and writing data analysis programs with Pandas and Polars
    -   Ning wants to build dashboards that people in the Ministry can use to query data in real time,
        but doesn't really understand how web browsers get data
        or what a server actually does
    -   Their work schedule is unpredictable and highly variable,
        so they need to be able to learn a bit at a time
-   prerequisites
    -   intermediate Unix command line: `find`, `grep`, shell scripts using `for`
    -   data analysis with Python: Pandas, Polars, Plotly, Jupyter notebooks, argparse, regular expressions
    -   using Git and GitHub on months-long projects with two or three colleagues
-   learning outcomes
    1.  TODO

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Setup" %]

-   Download [the latest release]([% config "release" %])
-   Unzip the file in a temporary directory to create:
    -   `./data/*.*`: the datasets used in the examples
    -   `./src/*.*`: shell scripts and Python programs
    -   `./out/*.*`: expected output for examples

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Background Concepts" %]

-   TODO

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Requesting a File" %]

[% double stem="get_motto" suffix="py out" %]

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

-   Open a connection to the server (we need to investigate that)
-   Send an [%g http_request "HTTP request" %] for the file we want (yup, going to investigate that as well)
-   Server creates a [%g http_response "response" %] that includes the contents of the file (ditto)
-   Sends it back
-   `requests` parses the response and creates a Python object for us (also deserves a closer look)

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Headers" %]

[% double stem="show_response_headers" suffix="py out" %]

-   Every HTTP request and response has [%g http_header "headers" %] with extra information
    -   Does *not* include status code (handled separately)
-   Most important for now are:
    -   `Content-Length`: number of bytes in response data (i.e., how much to read)
    -   `Content-Type`: [%g mime_type "MIME type" %] of data (e.g., `text/plain`)
-   Requests have headers too, which we will see soon

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="When Things Go Wrong" %]

[% double stem="get_nonexistent" suffix="py out" %]

-   The 404 status code tells us something went wrong
-   The 9 kilobyte response is an HTML page with an embedded image (the GitHub logo)
-   The page contains error messages, but we have to know page format to pull them out

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Getting JSON" %]

[% double stem="get_json" suffix="py out" %]

-   Parsing data out of HTML is called [%g web_scraping "web scraping" %]
    -   Painful and error prone
-   Better: have the server return data as data
    -   Preferred format these days is [%g json "JSON" %]
    -   So common that `requests` has built-in support

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Local Server" %]

[% single "src/run_site_server.sh" %]

-   Use Python's [`http.server`][py_http_server] module
    to run a [%g local_server "local server" %]
    -   Host name is [%g localhost "`localhost`" %]
    -   Uses port 8000 by default
    -   So URLs look like `http://localhost:8000/path/to/file`
-   `-d site` tells the server to pretend `site` is root directory
-   Use this local server for the next few examples
    -   Build our own server later on to show how it works

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Checking Local Server" %]

[% double stem="get_local_motto" suffix="py out" %]

-   [%g concurrency "Concurrent" %] systems are hard to debug
    -   Multiple streams of activity
    -   Order may change from run to run

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Secure Sockets" %]

[% double stem="basic_http_client" suffix="py out" %]

-   There's a lot going on here (which is why we use `requests`)
-   Create a [%g socket "socket" %]
-   Wrap it with [%g tls_ssl "TLS/SSL" %] security (which GitHub requires)
-   Connect to server
-   Send HTTP request
    -   `GET` plus path to file plus HTTP version
    -   One header identifying the host (because a single address might be home to several)
-   Read data back
    -   First chunk of reply is standard HTTP response with lots of headers
    -   Second chunk is content
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
