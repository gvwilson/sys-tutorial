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

# Files to copy verbatim.
copy = [
    "*.out",
    "*.py",
    "*.sh",
    "*.text",
]

# Enable various Markdown extensions.
markdown_settings = {
    "extensions": [
        "markdown.extensions.extra",
        "markdown.extensions.smarty",
        "pymdownx.superfences",
    ]
}
