---
title: "Virtualization"
syllabus:
- FIXME
---

## Virtual Environments

-   If two directories `A` and `B` contain a program `xyz` and `A` comes before `B`,
    `xyz` on its own will run `A/xyz` instead of `B/xyz`
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

## Limits of Virtual Environments {: .aside}

-   `conda` and `python -m venv` work for Python
-   But what about Rust, JavaScript, and other languages?
-   In particular, what if you need an isolated environment for several languages at once?
-   And you want other people to be able to reproduce it?
-   We will build something worth installing and then return to this problem

## What's the Magic Word?

-   Only allow access to data if client:
    -   [%g authentication "Authenticates" %] (i.e., establishes their identity)
    -   Is [%g authorization "authorized" %] (i.e., has the right to view the data)
-   Simplest possible is wrong in many ways: does the client know a password?

[%inc bird_client_password.py %]
[%inc bird_client_password_correct.sh %]
[%inc bird_client_password_correct.out %]
[%inc bird_client_password_incorrect.sh %]
[%inc bird_client_password_incorrect.out %]

-   First change to server: get the password on the command line and save it

[%inc bird_server_password.py mark=main %]
[%inc bird_server_password.py mark=server %]

-   Second change: add authorization to `do_GET`
    -   Once again use our own exception class to handle unhappy cases

[%inc bird_server_password.py mark=get %]

-   Add authorization that checks header value

[%inc bird_server_password.py mark=auth %]

-   Handle errors by constructing JSON

[%inc bird_server_password.py mark=error %]

-   It works but:
    -   One password for everyone
    -   Sent as [%g cleartext "cleartext" %] over an unencrypted connection

## Basic Authentication

-   Modify `do_GET`

[%inc bird_server_basicauth.py mark=get %]

-   [Basic HTTP authentication][basic_http_auth]:
    -   Header called `"Authorization"`
    -   Value is <code>Basic <em>data</em></code>
    -   Data is [%g base64 "base-64 encoded" %] <code><em>username</em>:<em>password</em></code>
-   Most of the code is checking that everything is OK and responding properly if it's not
-   Test client

[%inc bird_client_basicauth.py %]
[%inc bird_client_basicauth_correct.sh %]

## Changing the Root Directory

-   The `chroot` command
    -   Changes the process's idea of the [%g root_directory "root directory" %]
    -   Runs a command
-   But…

[%inc chroot_example.sh %]
[%inc chroot_example.out %]

-   Need special permission (discussed below)
-   Everything needed to run `echo` and other commands needs to be in the new filesystem
-   Only isolates the filesystem

## sudo

-   Every machine has a [%g superuser "superuser" %] account called [%g root_user "root" %]
    -   Which has nothing to do with the root directory of the filesystem
-   Use `sudo` ("superuser do") to change identity temporarily

[%inc sudo_example.sh %]
[%inc sudo_example.out %]

-   At least it's a different error message…
-   `sudo` is a way to give yourself permission to mess up everything on your computer
-   So another requirement for virtual environments:
    break them without breaking anything else

## Docker

-   [Docker][docker] solves all of these problems
-   Define an [%g docker_image "image" %] with its own copy of the operating system, filesystem, etc.
-   Run it in a [%g docker_container "container" %] that is isolated from the rest of your computer

[%inc docker_image_ls.sh %]
[%inc docker_image_ls.out %]
[%inc docker_container_ls.sh %]
[%inc docker_container_ls.out %]

## Common Error Message {: .aside}

-   Docker requires a [%g daemon "daemon" %] process to be running in the background to start images

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

-   Doesn't need to download again
-   Runs the given command instead of the default `/bin/bash`

## This Doesn't Work {: .aside}

[%inc docker_run_error.text %]

## Pulling Images {: .aside}

-   Don't have to run immediately

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
-   Use [Go][golang] format strings to format output (no, really)

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

-   Create a Dockerfile
    -   Usually called that and in a directory of its own
    -   Ours is `src/ubuntu_python3/Dockerfile`

[%inc ubuntu_python3/Dockerfile %]

-   Tell docker to build the image

[%inc ubuntu_python3_build.text %]

-   `CACHED` because we've run this several times while building this tutorial

[%inc ubuntu_python3_run.text %]

## Layers

[%inc docker_image_history.text %]

-   Docker images are built in layers
-   Layers can be shared between images to reduce disk space

[%inc docker_system_df.text %]

-   First line (`Images`) shows actual disk space
    -   We'll see the original `df` command again…

## Choosing a Command

-   Add `CMD` with a list of arguments to specify default command when image runs

[%inc python3_interpreter/Dockerfile %]

-   Build

[%inc python3_interpreter_build.text %]

-   Run

[%inc python3_interpreter_run.text %]

## Exercises {: #virt-exercises}

1.  What is the `re.sub` call in the `faker` script doing and why?
