
from py_idt.defaults import SCALE_DICT, PURIFICATION_DICT

def get_scales():
    """Helper function to display valid IDT oligo scale options."""

    # construct IDT scale table as a formatted string
    scale_str = '\n\n~~~ IDT BULK OLIGO SCALE OPTIONS ~~~\n\n'
    scale_str += '  {:15s}{}\n'.format('Code', 'Scale')
    for scale_code in SCALE_DICT:
        scale_str += '  {:15s}{}\n'.format(scale_code, SCALE_DICT[scale_code])

    # success
    return(scale_str)


def get_purifications():
    """Helper function to display valid IDT oligo purification options."""

    # construct IDT scale table as a formatted string
    purification_str = '\n\n~~~ IDT BULK OLIGO PURIFICATION OPTIONS ~~~\n\n'
    purification_str += '  {:15s}{}\n'.format('Code', 'Purification')
    for purification_code in PURIFICATION_DICT:
        purification_str += '  {:15s}{}\n'.format(purification_code, PURIFICATION_DICT[purification_code])

    # success
    return(purification_str)
