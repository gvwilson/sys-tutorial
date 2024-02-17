<!-- ---------------------------------------------------------------- -->
[% section_start class="aside" title="What This Is" %]

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
        and are comfortable working with Unix command-line tools,
        writing data analysis programs in Python,
	and downloading data from the web to use in those programs
    -   Ning wants to build real-time dashboards for people in the Ministry,
        but doesn't understand how to do that
	without exposing confidential data or opening the Ministry up to attack
    -   Their work schedule is unpredictable and highly variable,
        so they need to be able to learn a bit at a time
-   prerequisites
    -   intermediate Unix command line: `find`, `grep`, shell scripts using `for`
    -   data analysis with Python: Polars, Plotly, Jupyter notebooks, argparse, regular expressions
    -   using Git and GitHub on months-long projects with two or three colleagues
-   learning outcomes
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
[% section_break class="aside" title="Appendices" %]

### Terms

[% glossary %]

### Acknowledgments

[% thanks %]

### Links

[% link_table %]

[% section_end %]
