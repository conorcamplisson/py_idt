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
html_theme_options = {
    # the version switcher is populated by the docs workflow writing switcher.json
    "switcher": {
        "json_url": "https://conorcamplisson.github.io/py_idt/switcher.json",
        "version_match": release,
    },
    "navbar_end": ["version-switcher", "theme-switcher", "navbar-icon-links"],
}

exclude_patterns = ["_build"]
