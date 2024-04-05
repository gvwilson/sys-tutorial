<div class="row">
  <div class="col-4 center">
    <img class="splash" src="@root/advent_05_356-resized.png" alt="cover art by Danielle Navarro"/>
  </div>
  <div class="col-8">
    <p>
      Many think they know Unix.
      Few realize that what they know is just a shell.
      Beneath it lie mysteries both bewildering and wonderful:
      ports, processes, permissions,
      files that are not files,
      and components built atop other, older components
      that occasionally rise to the surface like ancient sea creatures believed long extinct.
    </p>
    <p>
      Like such creatures,
      Unix will outlive those who mock it.
      Welcome, then, to a world in which the strange will become familiar, and the familiar, strange.
      Welcome, thrice welcome, to Unix systems programming.
    </p>
    <p class="italic">
      "[% config "title" %]" is a <a href="[% config "author.site" %]">Third Bit</a> production.
    </p>
  </div>
</div>

[% toc %]

## To Do

-   How can I find things on my system?
    -   `find | xargs` and alternatives
-   How can I found out what kind of system I'm using (`uname`)
-   How do I see who has accounts on a machine?
-   How do I create a new account?
-   How do I delete an account?
-   How do I see who owns a file?
-   What does it actually mean to own a file?
-   What other kinds of permissions are there?
-   How can I specify what program to use to run a file?
-   How can I tell what kind of file a file is?
-   How can I see what's using a computer's processor/memory/disk/network?
-   How are files and directories stored (i.e., what is an inode)?
-   How can I see how much disk space is in use (`df`, `du`)?
-   When is a file not a file?
-   How can I create a shortcut (link) for a file?
-   What is a port?
-   How can I tell which ports are being used and by which processes?
-   How can I run a job repeatedly (`cron` and `watch`)?
-   What is a process group?
-   What are keys and how do I manage them?
-   What are certificates and how do I manage them?
-   How can I run a web server?
-   What other services might I want to run, when, and why?
-   How can I check my network connection (ping, traceroute)?
-   What is an IP address?
-   How can I connect to another computer (ssh)?
-   What is a user group and why do I care?
-   How can I view the computer's system log and what will I find there?
-   What are alternatives to classic password authentication?
