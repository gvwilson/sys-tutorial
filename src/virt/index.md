---
title: "Virtualization"
tagline: "How and why to pretend you have lots of computers."
---

## Virtual Environments

-   If two directories `A` and `B` contain a program `xyz`
    and `A` comes before `B` in the user's `PATH`,
    the command `xyz` will run `A/xyz` instead of `B/xyz`
-   This is how [%g virtual_env "virtual environments" %] work

[%inc show_virtual_env.sh %]
[%inc show_virtual_env.out %]

-   Virtual environment is initially a minimal Python installation
-   Installing new packages puts them in the environment's directory

## Package Installation

1.  Create a new virtual environment called `example`: `conda create -n example python=3.12`
2.  Activate that virtual environment: `conda activate example`
3.  Install the `faker` package: `pip install faker`

[%inc find_faker.sh %]
[%inc find_faker.out %]

-   The script in `bin` loads the module and runs it

[%inc faker_bin.py %]

-   The directory under `site-packages` has 642 Python files (as of version 24.3.0)
-   The `python` in the virtual environment' `bin` directory
    knows to look in that environment's `site-packages` directory

## Exercises {: .exercise}

What is the `re.sub` call in the `faker` script doing and why?

## Limits of Virtual Environments {: .aside}

-   `conda` (and equivalents like `python -m venv`) work for Python
-   But what if you need an isolated environment for several languages at once?
    -   Rust, JavaScript, and other languages all have their own solutions
-   And what if you want other people to be able to reproduce that environment?

## Docker

-   [Docker][docker] solves these problems (and others)
-   Define an [%g docker_image "image" %] with its own copy of the operating system, filesystem, etc.
-   Run it in a [%g docker_container "container" %] that is isolated from the rest of your computer

[%inc docker_image_ls.sh %]
[%inc docker_image_ls.out %]
[%inc docker_container_ls.sh %]
[%inc docker_container_ls.out %]

-   Because we haven't created or run anything yet

## Common Error Message {: .aside}

-   Docker requires a [%g daemon "daemon" %] process
    to be running in the background to start images

[%inc docker_image_ls.sh %]
[%inc docker_image_ls_err.out %]

## Running a Container

[%inc docker_run_fresh.text %]

-   Ask Docker to run a container with `ubuntu:latest`
    -   I.e., latest stable version of Ubuntu Linux from [Docker Hub][docker_hub]
-   Docker can't find a [%g cache "cached" %] copy locally, so it downloads the image
-   Then runs it
-   But its default command is `/bin/bash` with no inputs, so it exits immediately.

## Re-running a Container

[%inc docker_run_again.text %]

-   Docker doesn't need to download the image again (it's cached)
-   Runs the given command instead of the default `/bin/bash`

## This Doesn't Work {: .aside}

[%inc docker_run_error.text %]

-   There is no executable in the image's search path called `echo hello` (all one word)

## Pulling Images {: .aside}

-   We don't have to run immediately

[%inc docker_pull.text %]

## What Have We Got?

[%inc os_release.text %]

-   Don't need `:latest` every time (defaults)

## Inside the Container

[%inc docker_run_interactive.text %]

-   `-i`: interactive
-   `-t`: terminal (kind of)
    -   Combination often abbreviated `-it`
-   The hexadecimal number after `root@` is the container's unique ID

## Persistence

[%inc docker_run_nonpersistent.text %]

-   Container starts fresh each time it runs
-   Notice that the container's ID changes each time it runs

## What Is Running

[%inc docker_container_ls_id.text %]

-   `docker container ls` on its own shows a wide table
-   Use [Go][golang] format strings to format output
    -   Yes, really…

## Installing Software

[%inc docker_install_python.text %]

-   `apt update` to update available package lists
-   `apt install` to install the desired package
    -   Installs lots of dependencies as well
-   Doesn't create `python` (note lack of output)
-   Creates `python3` instead
-   Version is most recent in the default repository
-   But *it isn't there the next time we run*

[%inc docker_install_python_nonpersistent.text %]

## Actually Installing Software

-   Create a [%g dockerfile "Dockerfile" %]
    -   Usually called that and in a directory of its own
    -   Ours is `src/ubuntu_python3/Dockerfile`

[%inc ubuntu_python3/Dockerfile %]

-   Tell docker to build the image

[%inc ubuntu_python3_build.text %]

-   `CACHED` because we ran this several times
    while building this tutorial

[%inc ubuntu_python3_run.text %]

## Layers

[%inc docker_image_history.text %]

-   Docker images are built in layers
-   Layers can be shared between images to reduce disk space

[%inc docker_system_df.text %]

-   First line (`Images`) shows actual disk space
    -   `df` because there's a Unix command with that name to show free disk space

## Choosing a Command

-   Add `CMD` with a list of arguments to specify default command when image runs

[%inc python3_interpreter/Dockerfile %]

-   Build

[%inc python3_interpreter_build.text %]

-   Run

[%inc python3_interpreter_run.text %]

## To Do

-   Managing secrets (also shows up in authentication)
