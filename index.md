---
home: true
---
<section markdown="1">

{% include h2_unnumbered.md title="what this is" %}

-   notes and working examples that instructors can use to perform a lesson
    -   do *not* expect novices with only basic command-line experience
        to be able to learn from them on their own
-   musical analogy
    -   this is the chord changes and melody
    -   we expect instructors to create an arrangement and/or improvise while delivering
    -   see [*Teaching Tech Together*][t3] for background
-   please see [the license](./license/) for terms of use,
    the [Code of Conduct](./conduct/) for community standards,
    and [these guidelines](./contributing/) for notes on contributing
-   about the author:
    [Greg Wilson][wilson-greg] is a programmer, author, and educator based in Toronto

</section>
<section markdown="1">

{% include h2_unnumbered.md title="scope" %}

-   [intended audience][persona]
    -   Ning has a bachelor's degree in geology and a master's degree in data science,
        and now works for a 30-person forestry management consulting company
    -   They occasionally teach [Carpentries workshops][carpentries] at their old university
        and help colleagues write and run [Metaflow][metaflow] workflows on [AWS][aws].
    -   Ning would like to learn more about how to build and maintain the systems they use,
        but are struggling to understand the differences between
	systems administration, dev ops, and data engineering
	and doesn't know which pieces to focus on.
    -   Their work schedule is unpredictable and highly variable,
        so they need to be able to learn a bit at a time.
-   prerequisites
    -   Unix shell commands covered in [this Software Carpentry lesson][sc-shell]:
        -   `pwd`; `ls`; `cd`; `.` and `..`; `rm` and `rmdir`; `mkdir`; `touch`;
            `mv`; `cp`; `tree`; `cat`; `wc`; `head`; `tail`; `less`; `cut`; `echo`;
            `history`; `find`; `grep`; `zip`; `man`
        -   current working directory; absolute and relative paths; naming files;
            editing with `nano`
        -   standard input; standard output; standard error; redirection; pipes
        -   `*` and `?` wildcards; shell variable with `$` expansion; `for` loop;
            shell scripts with numbered arguments; the `PATH` variable; `$(…)` expansion
    -   Git commands and workflow covered in [this Software Carpentry lesson][sc-git]
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
	    `pytest` (but not mock objects); writing docstrings (but not [Sphinx][sphinx])
-   learning outcomes
    1.  Create a virtual environment and explain what this actually does.
    1.  Create `requirements.txt` file for [`pip`][pip] and explain version pinning.
    1.  Explain what a filesystem is (disk partitions, inodes, symbolic links)
        and use `df`, `ln`, similar commands to explore with them.
    1.  Use Python in place of shell scripts:
        1.  Operate on files matching glob patterns.
        1.  Create/delete directories.
        1.  Explain how Unix permissions work and read/modify them.
	1.  Explain how file hashing works and how to use it in programs.
-   TODO:
    -   what to teach about Docker and why?
        -   what if anything to teach about Linux?
    -   what to teach about authentication and for what purpose?
    -   what to teach about continuous integration, using what system?
    -   what to teach about batch jobs, using what system?
    -   what to teach about generating docs from docstrings, using what system?
    -   what to teach about cron jobs (if anything)?
    -   what if anything to teach about networking, firewalls, certificates, etc.?

</section>

{% include links.md links=site.data.links %}
