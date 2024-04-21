---
title: "The Filesystem"
tagline: "How to manage files, directories, and their stranger kin."
---

-   [%issue 19 %]

## What is a Filesystem? {: #fs-filesystem}

-   [%g ball_and_stick "Ball-and-stick model" %]
    -   Computer's hard drive has files and directories
    -   Directories can contain other directories but don't contain data
    -   Files contain data but can't contain other files (or directories)
    -   Everything forms a tree under the [%g root_directory "root directory" %] `/`
-   More accurate model
    -   Computer may have many storage devices, each with its own [%g filesystem "filesystem" %]
    -   Each file is made up of one or more fixed-size [%g block_filesystem "blocks" %]
    -   The filesystem keeps track of which blocks belong to which files
        -   Adds or recycles blocks as necessary
    -   A directory is a special kind of file that keeps track of other files
        -   Files aren't physically "in" a directory

## What Does the Filesystem Know? {: #fs-know}

-   `ls` command flags:
    -   `-a`: show directories whose names begin with `.`
    -   `-i`: show inode numbers
    -   `-l`: long form (i.e., include several pieces of information)
    -   `-s`: show the number of blocks

[%inc ls_long_tmp.sh %]
[%inc ls_long_tmp.out %]

-   It's a shame there's no option for column titles, but we can add them manually ([%t ls_long_tmp %])

[%table tbl="ls_long_tmp.tbl" caption="Annotated Output of `ls`" %]

-   The [%g inode "inode" %] stores attributes and IDs of disk blocks
    -   No-one is sure any longer what the "i" stands for
    -   Each inode has a unique ID that stays the same despite renaming
    -   Design pattern: always generate and manage your own IDs
-   Number of blocks
    -   Each block is typically 4kbyte, but that may vary
    -   [%fixme "why 8 blocks for bibliography which is only 174 bytes?" %]
-   Will discuss permissions [later](#fs-perm)
-   Number of [%g link_hard "hard links" %]
    -   I.e., the number of things that point to this file or directory
    -   [Discussed below](#fs-link-hard)
-   Names of user and group that own the file or directory
    -   [Discussed below](#fs-uid-gid)
-   Size in bytes (i.e., what `wc -c` reports)
-   Finally the name
-   So now we have a bunch of concepts to explain

## What Does "Permission" Mean? {: #fs-perm}

-   The three A's
    -   [%g authentication "Authentication" %]: who are you
        (or more accurately, what is your identity on this computer system)?
    -   [%g authorization "Authorization" %]: who is allowed to do what?
    -   [%g access_control "Access control" %]: how does the system enforce those rules?
-   So operating systems needs to:
    -   Match a person to an account (we will discuss in [%x auth %])
    -   Keep track of which account each process belongs to
    -   Keep track of what operations are permitted to whom
    -   Enforce those rules (which we won't go into)

## What Are User and Group IDs? {: #fs-uid-gid}

-   Each user account has a unique name and a unique numeric ID
    -   The numeric user ID is often called a [%g uid "uid" %]
    -   Not to be confused with [%g uuid "UUID" %]
-   Each user can belong to one or more [%g user_group "groups" %]
    -   Each of which also has a unique name and a unique group ID (or [%g gid "gid" %])

[%inc id_no_args.sh %]
[%inc id_no_args.out %]

-   Tells us:
    -   User ID is 501 and name is `tut`
    -   Primary group ID is 20 (`staff`)
    -   Also belongs to 12 (`everyone`) and 61 (`localaccounts`)
-   Reports by default on the user associated with the currently-running process
-   Can provide an account name to get details of a particular account

[%inc id_nobody.sh %]
[%inc id_nobody.out %]

## What Capabilities Do Files and Directories Offer? {: #fs-capability}

-   A [%g capability "capability" %] is something that someone may or may not be able to do to a thing
    -   Which is incredibly vague
-   Files and directories capabilities are shown in [%t capabilities %]

[%table tbl="capabilities.tbl" caption="Unix File and Directory Capabilities" %]

-   Read and write make sense
-   Execute makes sense on files
    -   [See below](#fs-file-types) for how the operating system figures out how to run a file
-   Execute on directories is basically "we needed something and this bit was available"
    -   Want to be able to run `dir/program`
    -   *Without* seeing what else is in `dir`
    -   Use the "execute" bit on the directory `dir`

## How Does the Operating System Decide What Users Can Do? {: #fs-permission}

-   Go back to permissions in [%t ls_long_tmp %]
-   First letter is `-` for a regular file and `d` for a directory
    -   We will see other things [below](#fs-link-sym)
-   Then show read-write-execute permissions for user, group, and other (i.e., everyone else)
-   So `drwxr-xr-x` means "a directory with owner=RWX, group=RX, and other=RX"
-   And `-rw-r--r--` means "a file with owner=RW, group=R, and other=R"

## How Can a User Change Permissions on a File or Directory: {: #fs-chmod}

-   Change permissions with `chmod` ("change mode")
    -   Unfortunately one of the more confusing Unix shell commands
-   Simplest form: `chmod u=rw,g=r,o=r`
    -   Specify read-write-execute explicitly for user-group-other

[%inc chmod_example.text %]

## How Can a Program Do This? {: #fs-python}

-   `ls`, `chmod`, and other programs use [%g system_call "system calls" %] to get information and change things
    -   A function provided by the operating system
-   Other programs can also use those system calls

[%inc chmod_example.py mark="create" %]

-   `os.stat` returns a tuple with named fields
    -   All start with `st_` prefix because that's what the original C structure did
-   `status.st_mode` doesn't make much sense in decimal
    -   Often printed in [%g octal "octal" %]
    -   Much easier to use `stat.filemode` to turn it into an `ls`-style string

[%inc chmod_example.py mark="lockdown" %]

-   Use `os.chmod` to set the permission to nothing-nothing-nothing (i.e., 0)
-   Trying to read/write file after that causes `PermissionError` (a subclass of `OSError`)

[%inc chmod_example.py mark="lockdown" %]
-   `stat` defines constants representing various permissions
-   Add the ones we want

## What is "Systems Programming"? {: #fs-sys-prog .aside}

-   Not a precise term
-   But if it means anything,
    it includes things at this level

## What is a Hard Link? {: #fs-link-hard}

-   One of the columns in [%t ls_long_tmp %] is "links"
    -   How many references there are to a file in the filesystem
-   Can create more links to an existing file
    -   What we think of as "files" are bookkeeping entries in the filesystem that refer to inodes
-   Use the `ln` command to create a [%g link_hard "hard link" %]
    -   Syntax is like `mv`: existing first, then new name

[%inc hard_link.text %]

-   Note the number of links to `original.txt` and `duplicate.txt` is 2 when they both exist

## What is a Symbolic Link? {: #fs-link-sym}

-   A [%g link_sym "symbolic link" %] (or symlink) is a file that refers to another file
    -   [%fixme https://stackoverflow.com/questions/185899/what-is-the-difference-between-a-symbolic-link-and-a-hard-link %]

[%inc sym_link.text %]

-   Soft links can have different permissions
    -   Hard links all refer to the same inode, which is where permissions are stored
-   Often use soft links to hide version numbers of installed applications
    -   E.g., `~/conda/bin/python` is a symlink to `~/conda/bin/python3.11`
    -   Running the former actually launches the latter

## To Do

[%fixme "how to determine block size" %]

[%fixme "change user/group ID in fork/exec" %]

[%fixme "explain chown" %]

[%fixme "explain permissions are less important on laptops than multi-user systems except services" %]
