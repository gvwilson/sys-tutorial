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
-   About the author:
    [Greg Wilson][wilson-greg] is a programmer, author, and educator based in Toronto
    -   Co-founder and first Executive Director of [Software Carpentry][carpentries]
    -   Currently a senior software engineering manager at a startup in Toronto

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
    -   Intermediate Unix command line: `find`, `grep`, shell scripts using `for`
    -   Data analysis with Python: Polars, Plotly, Jupyter notebooks, argparse, regular expressions
    -   Using Git and GitHub on months-long projects with two or three colleagues
-   Learning outcomes
    1.  TODO

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Setup" %]

-   Download [the latest release]([% config "release" %])
-   Unzip the file in a temporary directory to create:
    -   `./src/*.*`: shell scripts and Python programs
    -   `./site/*.*`: the pages and data files used in the examples
    -   `./out/*.*`: expected output for examples

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Background Concepts" %]

-   TODO

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Start with Something Simple" %]

[% double stem="requests_get_motto" suffix="py out" %]

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
[% section_break class="aside" title="Appendices" %]

### Terms

[% glossary %]

### Acknowledgments

[% thanks %]

### Links

[% link_table %]

[% section_end %]
