
import sys

from py_idt.defaults import SCALE_DICT, PURIFICATION_DICT
from py_idt.utils import get_scales, get_purifications

class Oligo(object):
    """Python representation of an IDT oligonucleotide to be ordered.

    Attributes:
        name (str): The name of the oligo to be used when ordering the oligo.
        seq (str): This oligo's sequence.
        scale (str): The IDT scale code to be used when ordering the oligo.
        purification (str): The IDT purification code to be used when ordering the oligo.
        length (int): The length of this oligo's sequence.
    """

    def __init__(self, name, seq, scale, purification):
        """Oligo object initialization.

        Args:
            name (str): The name of the oligo to be used when ordering the oligo.
            seq (str): This oligo's sequence.
            scale (str): The IDT scale code to be used when ordering the oligo.
            purification (str): The IDT purification code to be used when ordering the oligo.

        Returns:
            None
        """

        # store provided attributes
        self.name = name
        self.seq = seq
        self.scale = scale
        self.purification = purification

        # calculate this oligo's length
        self.length = len(seq)

        # validate scale and purification
        if self.scale not in SCALE_DICT:
            sys.exit('\nError: {} is not a valid oligo scale. Try: {}'.format(scale, get_scales()))
        if self.purification not in PURIFICATION_DICT:
            sys.exit('\nError: {} is not a valid oligo purification. Try: {}'.format(purification, get_purifications()))

    def __str__(self):
        """String object representation."""
        return('<Oligo: {} ({} bp), {}, {}>'.format(self.name, self.length, self.scale, self.purification))
    def __repr__(self):
        """List object representation."""
        return(self.__str__())
