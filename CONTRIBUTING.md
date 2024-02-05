# Contributing

Contributions are very welcome.
Please file issues or submit pull requests in our GitHub repository.
All contributors will be acknowledged.

## In Brief

-   The tutorial lives in `index.md`,
    which is translated into a static GitHub Pages website using [Jekyll][jekyll].

-   `Makefile` contains the commands used to rebuild things.

-   Add important terms to `_info/glossary.yml`,
    which is in [Glosario][glosario] format.

-   Use `{% raw %}<a href="#g:key">text</span>{% endraw %}` to link to glossary entries.
    The key must identify an entry in `_data/glossary.yml`;
    the `#` makes it an in-page reference,
    while the `g:` prefix triggers CSS styling.

-   SVG images used in the tutorial are in `img/`
    and can be edited using [draw.io][draw-io].
    Please use 12-point Helvetica for text,
    solid 1-point black lines,
    and unfilled objects.

[draw-io]: https://www.drawio.com/
[glosario]: https://glosario.carpentries.org/
[graphviz]: https://graphviz.org/
[jekyll]: https://jekyllrb.com/
[mermaid]: https://mermaid.js.org/
