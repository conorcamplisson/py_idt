"""sphinx configuration (canon/06)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from py_idt import __version__

project = "py_idt"
author = "Conor Camplisson"
copyright = "2026, Conor Camplisson"
release = __version__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",  # reads the Google-style docstrings (canon/01)
    "myst_parser",  # docs pages are Markdown, like the README (canon/06)
]

# napoleon is configured for Google style only; numpy style is not used here.
napoleon_google_docstring = True
napoleon_numpy_docstring = False

html_theme = "pydata_sphinx_theme"
# The switcher entry for a development build is literally "dev", because that is the folder CI
# writes it to; a released build matches its own version. Without this the dropdown on the dev
# site would look for "0.2.0.dev1", find no such entry, and highlight nothing.
version_match = "dev" if "dev" in release else release

html_theme_options = {
    # the version switcher is populated by the docs workflow writing switcher.json
    "switcher": {
        "json_url": "https://conorcamplisson.github.io/py_idt/switcher.json",
        "version_match": version_match,
    },
    "navbar_end": ["version-switcher", "theme-switcher", "navbar-icon-links"],
    "github_url": "https://github.com/conorcamplisson/py_idt",
    "use_edit_page_button": False,
}

html_title = f"py_idt {release}"

exclude_patterns = ["_build"]
