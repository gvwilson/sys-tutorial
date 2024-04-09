---
title: "Variables"
tagline: "How the shell keeps track of things."
---

## Operating System vs. Shell

-   [%g operating_system "Operating system" %] (OS) manages your hardware
    -   Provides a set of [%g system_call "system calls" %]
        to make different machines look the same to user-level programs
-   [%g shell "Command shell" %] (or just "shell") is a text UI for interacting with the operating system
    -   And with user-level programs
-   There are many different shells for Unix and Windows
    -   [Bash][bash] and [Zsh][zsh] are compatible with the POSIX standard
    -   [Fish][fish] is nicer, but is not
    -   [Nushell][nushell] is even stranger
    -   [PowerShell][powershell] on Windows (and Unix) has a lot of nice features too
-   We use Bash in this tutorial but will discuss Nushell later

## Shell Variables

-   The shell is a program and programs have variables
-   Create or change with <code><em>name</em>=<em>value</em></code>
-   [%g shell_var "Shell variable" %] stays in the process that created it
    -   E.g., that particular running copy of the shell
-   Use <code>$<em>name</em></code> to get value
    -   `$` prefix because people type file and directory names more often

[%inc shell_var_outer.sh %]
[%inc shell_var_inner.sh %]
[%inc shell_var_outer.out %]

-   Note: variables usually written in upper case to distinguish them from filenames
    -   So use underscores as separators

## Exercise {: .exercise}

What happens if you modify the scripts shown above
to use single quotes instead of double quotes?

## Environment Variables

-   [%g env_var "Environment variable" %] is inherited by new processes
-   Use <code>export <em>name</em>=<em>value</em></code>

[%inc env_var_outer.sh %]
[%inc env_var_inner.sh %]
[%inc env_var_outer.out %]

## Exercise {: .exercise}

If a child process sets shell or environment variables,
are they visible in the parent once the child finishes executing?

## Environment Variables in Programs

-   Since environment variables are inherited by child processes,
    they are inherited by all programs run from the shell that has them

[%inc env_var_py.sh %]
[%inc env_var_py.py %]
[%inc env_var_py.out %]

## Inspecting Variables

-   `set` on its own lists variables
    -   And functions, because yes, you can create those in the shell
    -   But please don't: if you need that, write a Python script
-   `env` shows all environment variables

[%inc show_env_vars.sh %]
[%inc show_env_vars.out %]

-   Many tools rely on variables to manage configuration
    -   [NVM][nvm] defines 4, [Conda][conda] defines 8
    -   No guarantee that their names don't [%g name_collision "collide" %]


## Exercise {: .exercise}

The `os.environ` variable in Python's `os` module
is an easy way to get all of the process's environment variables.
Compare it to what `env` shows.

1.  Are there differences?

2.  If so, what are they and why do they exist?

## Important Environment Variables

-   37 environment variables in my current shell
-   Most important are shown in [%t var_common %]

[%table slug=var_common tbl="env_var.tbl" caption="Environment Variables" %]

## Search Path

-   `PATH` holds a colon-separated list of directories
-   Shell looks in these *in order* to find commands
-   Reading at them all on one line is difficult, so use `tr` to split

[%inc show_path.sh %]
[%inc show_path.out %]

-   Notice `/Users/tut/bin`
-   Common to have a `~/bin` directory with the user's own utilities

## Adding to the Search Path

-   Shell variables (of both kinds) are just strings
-   So add to search path by redefining the variable
    -   New directory at the from
    -   Entire old value at the back

[%inc change_path.sh %]
[%inc change_path.out %]

## Exercise {: .exercise}

Removing a directory from `PATH` is harder than adding one.
Write a shell script that:

1.  Splits `PATH` on colons to put one entry on each line.
2.  Uses `grep` to remove the undesired line.
3.  Uses `paste -s -d :` to recombine the lines.
4.  Uses command interpolation to assign the result back to `PATH`.

This exercise may remind you why
complicated operations should be done in Python rather than in the shell.

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
