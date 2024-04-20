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

## What Are User and Group IDs? {: #fs-uid-gid}

[%fixme "explain user IDs and group IDs" %]

[%fixme "explain difference between IDs and names" %]

## How Are Permissions Represented? {: #fs-perm}

[%fixme "explain Unix permission model" %]

## What is a Hard Link? {: #fs-link-hard}

[%fixme "explain hard links" %]

## What is a Symbolic Link? {: #fs-link-sym}

[%fixme "explain symbolic links" %]

## To Do

[%fixme "how to determine block size" %]
