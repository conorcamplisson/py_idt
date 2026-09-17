"""helpers for reporting the valid scale and purification codes."""

from py_idt.defaults import PURIFICATION_DICT, SCALE_DICT


def get_scales():
    """Helper function to display valid IDT oligo scale options."""
    # construct IDT scale table as a formatted string
    scale_str = "\n\n~~~ IDT BULK OLIGO SCALE OPTIONS ~~~\n\n"
    scale_str += "  {:15s}{}\n".format("Code", "Scale")
    for scale_code in SCALE_DICT:
        scale_str += f"  {scale_code:15s}{SCALE_DICT[scale_code]}\n"

    # success
    return scale_str


def get_purifications():
    """Helper function to display valid IDT oligo purification options."""
    # construct IDT scale table as a formatted string
    purification_str = "\n\n~~~ IDT BULK OLIGO PURIFICATION OPTIONS ~~~\n\n"
    purification_str += "  {:15s}{}\n".format("Code", "Purification")
    for purification_code in PURIFICATION_DICT:
        purification_str += f"  {purification_code:15s}{PURIFICATION_DICT[purification_code]}\n"

    # success
    return purification_str
