"""Manage headers for display."""

def headers(text, *args):
    """Show only desired headers."""
    lines = [ln.strip() for ln in text.split("\n")]
    keep = [ln for ln in lines if any(ln.startswith(a) for a in args)]
    if len(keep) < len(lines):
        keep.append(f"…plus {len(lines) - len(keep)} more lines…")
    return "\n".join(keep)
