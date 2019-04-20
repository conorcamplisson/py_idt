
import os
from datetime import datetime

import pandas as pd

from py_idt.defaults import DEFAULT_PARAMS, SCALE_DICT
from py_idt.oligo import Oligo

class IDTOrder(object):
    """Python representation of an IDT bulk oligonucleotide order.

    Attributes:
        scale (str): The default IDT scale code for oligos on this order.
        purification (str): The default IDT purification code for oligos on this order.
        output_dir (str): The path to the directory where .xlsx files will be stored.
        oligos (list): A list of Oligo objects on this order.
        num_oligos (int): The number of oligos on this order.
    """

    # default settings
    settings = DEFAULT_PARAMS

    def __init__(self, scale = None, purification = None):
        """IDTOrder object initialization.

        Args:
            scale (str): Optionally override the default IDT scale code for this order.
            purification (str): Optionally override the default IDT purification code for this order.

        Returns:
            None
        """

        # default settings
        self.scale = IDTOrder.settings['scale']
        self.purification = IDTOrder.settings['purification']
        self.output_dir = IDTOrder.settings['output_dir']
        self.oligos = []
        self.num_oligos = 0

        # optionally override defaults
        if scale:
            self.scale = scale
        if purification:
            self.purification = purification


    def add_oligo(self, name, seq, scale = None, purification = None):
        """Add a new Oligo object to an IDT bulk oligo order.

        Args:
            name (str): The name of the oligo to be used when ordering the oligo.
            seq (str): This oligo's sequence.
            scale (str): Optionally override the default IDT scale code for this oligo.
            purification (str): Optionally override the default IDT purification code for this oligo.

        Returns:
            None
        """

        # optionally override defaults
        if not scale:
            scale = self.scale
        if not purification:
            purification = self.purification

        # create oligo
        oligo = Oligo(name, seq, scale, purification)
        self.oligos.append(oligo)
        self.num_oligos = len(self.oligos)


    def save(self):
        """Creates an .xlsx file to be uploaded to IDT's website to create a bulk oligo order.

        Args:
            None

        Returns:
            None
        """

        # construct a pandas dataframe from associated oligo object data
        rows = []
        for oligo in self.oligos:
            oligo_data = {
                'Name': oligo.name,
                'Sequence': oligo.seq,
                'Scale': oligo.scale,
                'Purification': oligo.purification
            }
            rows.append(oligo_data)
        cols = ['Name', 'Sequence', 'Scale', 'Purification']
        df = pd.DataFrame(data=rows, columns=cols)

        # construct output .xlsx file path
        output_dir = IDTOrder.settings['output_dir']
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        time_stamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        file_path = os.path.join(output_dir, '{}_idt_order.xlsx'.format(time_stamp))

        # Create an excel sheet using IDT oligo data
        writer = pd.ExcelWriter(file_path, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1', index=False)
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']
        writer.save()


    def __str__(self):
        """String object representation."""
        return('<IDT Order: {} oligos>'.format(self.num_oligos))
    def __repr__(self):
        """List object representation."""
        return(self.__str__())
