---
title: "Variables"
syllabus:
- FIXME
---

## Shell Variables

-   The shell is a program and programs have variables
-   Create or change with <code><em>name</em>=<em>value</em></code>
-   [%g shell_var "Shell variable" %] stays in the process
-   Use <code>$<em>name</em></code> to get value
    -   Because people type file and directory names more often

[%inc shell_var_outer.sh %]
[%inc shell_var_inner.sh %]
[%inc shell_var_outer.out %]

-   Note: variables usually written in upper case to distinguish them from filenames
    -   So underscores as separators

## Environment Variables

-   [%g env_var "Environment variable" %] is inherited by new processes
-   Use <code>export <em>name</em>=<em>value</em></code>

[%inc env_var_outer.sh %]
[%inc env_var_inner.sh %]
[%inc env_var_outer.out %]

## Environment Variables in Programs

-   Environment variables are inherited by child process…
-   …so they are inherited by programs (not just shell scripts)

[%inc env_var_py.sh %]
[%inc env_var_py.py %]
[%inc env_var_py.out %]

## Inspecting Variables

-   `set` on its own lists variables, functions, etc.
-   `env` shows all environment variables

[%inc show_env_vars.sh %]
[%inc show_env_vars.out %]

-   Many tools create variables to manage configuration
    -   No guarantees that they don't collide with each other

## Important Environment Variables

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

## Search Path

-   `PATH` holds a colon-separated list of directories
-   Shell looks in these *in order* to find commands
-   Looking at them all on one line is annoying, so use `tr` to split

[%inc show_path.sh %]
[%inc show_path.out %]

-   Notice `/Users/tut/bin`
-   Common to have a `~/bin` directory with the user's own utilities

## Adding to the Search Path

-   Shell variables (of both kinds) are just strings
-   So redefine the variable to the old value with a new directory at the front

[%inc change_path.sh %]
[%inc change_path.out %]

## Startup Files

-   Bash shell runs commands in `~/.bash_profile` for login shells
-   Bash shell runs commands in `~/.bashrc` for interactive shells
-   Yes, the terminology is confusing
-   Common to have `~/.bash_profile` [%g source_shell "source" %] `~/.bashrc`
    -   I.e., run those commands in the current shell

[%inc source_bashrc.sh %]

## Command Interpolation {: .aside}

-   Can use <code>outer $(<em>inner</em>)</code> to run `inner` and use its output as arguments to `outer`
-   Long-winded way to count lines in some text files

[%inc interpolate.sh %]
[%inc interpolate.out %]

## Exercises {: #var-exercises}

1.  What happens if you modify the scripts shown above
    to use single quotes instead of double quotes?

1.  If a child process sets shell or environment variables,
    are they visible in the parent once the child finishes executing?

1.  The `os.environ` variable in Python's `os` module
    is an easy way to get all of the process's environment variables.
    Compare it to what `env` shows.
    Are there differences?
    If so, what are they and why do they exist?

1.  Removing a directory from `PATH` is harder than adding one.
    Write a shell script that:

    1.  Splits `PATH` on colons to put one entry on each line.
    2.  Uses `grep` to remove the undesired line.
    3.  Uses `paste -s -d :` to recombine the lines.
    4.  Uses command interpolation to assign the result back to `PATH`.

    This exercise may remind you why complicated operations should be done in Python
    rather than in the shell.
