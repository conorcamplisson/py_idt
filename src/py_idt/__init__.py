"""A python interface for creating IDT bulk oligo order forms in Excel."""

# the version is re-exported from _version.py, the single source of truth (canon/05)
from ._version import __version__
from .idt_order import IDTOrder
from .oligo import Oligo

__all__ = ["IDTOrder", "Oligo", "__version__"]
