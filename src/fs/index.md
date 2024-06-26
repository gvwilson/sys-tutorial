---
title: "The Filesystem"
tagline: "How to manage files, directories, and their stranger kin."
---

-   [%issue 19 %]

## Definitions {: #fs-filesystem}

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

## Information About Files and Directories {: #fs-know}

-   `ls` command flags:
    -   `-a`: show directories whose names begin with `.`
    -   `-i`: show inode numbers
    -   `-l`: long form (i.e., include several pieces of information)
    -   `-s`: show the number of blocks

[%inc ls_long_tmp.sh %]
[%inc ls_long_tmp.out %]

-   It's a shame there's no option for column titles, but we can add them manually ([%t ls_long_tmp %])

[%table slug=ls_long_tmp tbl=ls_long_tmp.tbl caption="Annotated Output of `ls`" %]

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

## Permissions in Principle {: #fs-perm}

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

## User and Group IDs {: #fs-uid-gid}

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

## Capabilities {: #fs-capability}

-   A [%g capability "capability" %] is something that someone may or may not be able to do to a thing
    -   Which is incredibly vague
-   Files and directories capabilities are shown in [%t capabilities %]

[%table slug=capabilities tbl=capabilities.tbl caption="Unix File and Directory Capabilities" %]

-   Read and write make sense
-   Execute makes sense on files
    -   [See below](#fs-file-types) for how the operating system figures out how to run a file
-   Execute on directories is basically "we needed something and this bit was available"
    -   Want to be able to run `dir/program`
    -   *Without* seeing what else is in `dir`
    -   Use the "execute" bit on the directory `dir`

## Permissions in Practice {: #fs-permission}

-   Go back to permissions in [%t ls_long_tmp %]
-   First letter is `-` for a regular file and `d` for a directory
    -   We will see other things [below](#fs-link-sym)
-   Then show read-write-execute permissions for user, group, and other (i.e., everyone else)
-   So `drwxr-xr-x` means "a directory with owner=RWX, group=RX, and other=RX"
-   And `-rw-r--r--` means "a file with owner=RW, group=R, and other=R"

## Changing Permissions {: #fs-chmod}

-   Change permissions with `chmod` ("change mode")
    -   Unfortunately one of the more confusing Unix shell commands
-   Simplest form: `chmod u=rw,g=r,o=r`
    -   Specify read-write-execute explicitly for user-group-other

[%inc chmod_example.text %]

## Changing Permissions Programmatically {: #fs-python}

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

## Not Important Until It Is {: #fs-perm-important .aside}

-   Permissions are less important on laptops than they were on multi-user systems…
-   …until we start to run web servers and databases that other people can access

## Systems Programming? {: #fs-sys-prog .aside}

-   Not a precise term
-   But if it means anything,
    it includes things at this level

## Hard Links {: #fs-link-hard}

-   One of the columns in [%t ls_long_tmp %] is "links"
    -   How many references there are to a file in the filesystem
-   Can create more links to an existing file
    -   What we think of as "files" are bookkeeping entries in the filesystem that refer to inodes
-   Use the `ln` command to create a [%g link_hard "hard link" %]
    -   Syntax is like `mv`: existing first, then new name

[%inc hard_link.text %]

-   Note the number of links to `original.txt` and `duplicate.txt` is 2 when they both exist

## Symbolic Links {: #fs-link-sym}

-   A [%g link_sym "symbolic link" %] (or symlink) is a file that refers to another file
    ([%f fs_links %])

[% figure
   slug=fs_links
   img="links.svg"
   alt="Relationship between hard and symbolic Links"
   caption="Hard and Symbolic Links"
%]

[%inc sym_link.text %]

-   Soft links can have different permissions
    -   Hard links all refer to the same inode, which is where permissions are stored
-   Often use soft links to hide version numbers of installed applications
    -   E.g., `~/conda/bin/python` is a symlink to `~/conda/bin/python3.11`
    -   Running the former actually launches the latter

## Other Kinds of "Files" {: #fs-other}

-   Unix (and other modern operating systems) make [%g device "devices" %] look like files
    -   Reading from the keyboard and writing to the screen are like file I/O
-   The pseudofiles representing devices live in `/dev`
-   `ls /dev` on my machine shows 345 different devices
-   Key difference between different kinds is whether access is [%g buffer_verb "buffered" %]
    -   Does the operating system read a block at a time and then give the user access to the block?
    -   Does it store data in a block temporarily and write that block all at once?
-   A [%g character_device "character device" %] allows direct (unbuffered) access
    -   Example: terminals whose names are `/dev/tty*`
    -   `ls -l` shows `c` as the first letter instead of `d` for directory
-   A [%g block_device "block device" %] always buffers
    -   Example: a disk whose name is `/dev/disk*`
    -   `ls -l` shows `b` instead of `c`, `d`, `l`, or `-`
-   There are stranger things as well
    -   `dev/urandom` produces random bits

[%inc random_bits.py %]
[%inc random_bits.out %]

## Disks {: #fs-df}

-   Run the `df` command (for "disk free space")

[%inc df_output.out %]

-   The physical disk in this laptop is divided into several filesystems
    -   Each has its own inodes
-   How many 512-byte blocks does each have?
-   How many are used and available?
-   How many inodes are used and available?
-   Where is the filesystem [%g mount "mounted" %]?
    -   I.e., what path do we use to tell the operating system we want that data?
-   Most people won't ever have to worry about disks at this level
    -   But we *will* think about mounting in [%x virt %]

## Disk Usage {# #fs-du}

-   Use the `du` command with `-h` for human-readable suffixes and `-s` for summary

[%inc du_h_s.text %]

-   But this doesn't include `.git` or other files and directories whose names start with `.`
-   Simple solution `du -h -s .*` tries to summarize `..`, which isn't what we want
-   Use [%g command_interpolation "command interpolation" %] and `ls -A`
    -   All of these tools evolved piece by piece over time, and it shows

[%inc du_h_s_all.text %]
