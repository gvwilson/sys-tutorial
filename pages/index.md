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
[% section_break class="aside" title="Appendices" %]

### Terms

[% glossary %]

### Acknowledgments

[% thanks %]

### Links

[% link_table %]

[% section_end %]
