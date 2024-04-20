---
title: "The Filesystem"
tagline: "How to manage files, directories, and their stranger kin."
---

-   [%issue 19 %]

## What is a Filesystem? {: #fs-filesystem}

-   Ball-and-stick model
    -   Computer's hard drive has files and directories
    -   Directories can contain other directories but don't contain data
    -   Files contain data but can't contain other files (or directories)
    -   Everything forms a tree under the root directory `/`
-   More accurate model
    -   Computer may have many storage devices, each with its own filesystem
    -   Each file is made up of one or more fixed-size blocks
    -   The filesystem keeps track of which blocks belong to which files
        -   Adds or recycles blocks as necessary
    -   A directory is a special kind of file that keeps track of other files
        -   Files aren't physically "in" a directory

## 