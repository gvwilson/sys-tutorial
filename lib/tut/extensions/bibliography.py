"""Handle bibliography references and bibliography."""

import ark
from pathlib import Path
import shortcodes
import util


@shortcodes.register("b")
def bibliography_ref(pargs, kwargs, node):
    """Handle [%b key1 key2 %] biblography references."""
    util.require(
        (len(pargs) > 0) and (not kwargs),
        f"Bad 'b' shortcode with {pargs} and {kwargs} in {node}",
    )
    base = "@root/bib"
    links = [f'<a class="bib-ref" href="{base}/#{k}">{k}</a>' for k in pargs]
    links = ", ".join(links)
    return f'<span class="bib-ref">[{links}]</span>'


@shortcodes.register("bibliography")
def bibliography(pargs, kwargs, node):
    """Handle [% bibliography %] shortcode."""
    util.require(
        (not pargs) and (not kwargs),
        f"Bad 'bibliography' shortcode with {pargs} and {kwargs} in {node}",
    )
    return Path(ark.site.home(), "tmp", "bibliography.html").read_text()
