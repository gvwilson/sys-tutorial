---
title: "Authentication"
tagline: "How to tell who someone is."
---

-   See [%issue 16 %]

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
