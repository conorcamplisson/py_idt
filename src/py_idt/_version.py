"""the single source of truth for the package version.

the build backend reads it, __init__ re-exports it, and the release workflow checks the git tag
against it. nothing else declares a version.
"""

__version__ = "0.1.0"
