# Tutorial data.
title = "Web Programming for Wary Data Scientists"
subtitle = ""
repo = "https://github.com/gvwilson/web-tutorial"
release = "https://github.com/gvwilson/web-tutorial/raw/main/web-tutorial.zip"
plausible = "gvwilson.github.io/web-tutorial"
author = {
    "name": "Greg Wilson",
    "email": "gvwilson@third-bit.com",
}

# Theme information.
theme = "tut"
src_dir = "pages"
out_dir = "docs"
rouge_style = "github.css"
lang = "en"
extension = "/"

# Directories to copy verbatim.
copydir = [
    "out",
    "site",
    "src",
]

# Files to copy verbatim.
copyext = [
    ".html",
    ".json",
    ".out",
    ".py",
    ".sh",
    ".text",
    ".txt",
]

# Enable various Markdown extensions.
markdown_settings = {
    "extensions": [
        "markdown.extensions.extra",
        "markdown.extensions.smarty",
        "pymdownx.superfences",
    ]
}


if __name__ == "__main__":
    import sys
    USAGE = "usage: config.py [copydir | copyext | lang]"
    status = 0
    if len(sys.argv) == 1:
        print(USAGE, file=sys.stderr)
    elif len(sys.argv) != 2:
        print(USAGE, file=sys.stderr)
        status = 1
    elif sys.argv[1] == "copydir":
        print(" ".join(copydir))
    elif sys.argv[1] == "copyext":
        print(" ".join(copyext))
    elif sys.argv[1] == "lang":
        print(lang)
    else:
        print(USAGE, file=sys.stderr)
        status = 1
    sys.exit(status)
