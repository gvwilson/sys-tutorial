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
copy = [
    "*.html",
    "*.out",
    "*.py",
    "*.sh",
    "*.text",
    "*.txt",
]

# Enable various Markdown extensions.
markdown_settings = {
    "extensions": [
        "markdown.extensions.extra",
        "markdown.extensions.smarty",
        "pymdownx.superfences",
    ]
}
