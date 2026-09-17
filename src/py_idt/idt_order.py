"""the order: a collection of oligos, written out as an IDT bulk-order .xlsx."""

import os
from datetime import datetime

import pandas as pd

from py_idt.defaults import DEFAULT_PARAMS
from py_idt.oligo import Oligo


class IDTOrder:
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

    def __init__(self, scale=None, purification=None, output_dir=None):
        """IDTOrder object initialization.

        Args:
            scale (str): Optionally override the default IDT scale code for this order.
            purification (str): Optionally override the default IDT purification code
                for this order.
            output_dir (str): Optionally override the directory this order is written to.
                Applies to this order alone, unlike ``IDTOrder.settings["output_dir"]``,
                which is shared by every order in the process.

        Returns:
            None
        """
        # default settings
        self.scale = IDTOrder.settings["scale"]
        self.purification = IDTOrder.settings["purification"]
        self.output_dir = IDTOrder.settings["output_dir"]
        self.oligos = []
        self.num_oligos = 0

        # optionally override defaults
        if scale:
            self.scale = scale
        if purification:
            self.purification = purification
        if output_dir:
            self.output_dir = output_dir

    def add_oligo(self, name, seq, scale=None, purification=None):
        """Add a new Oligo object to an IDT bulk oligo order.

        Args:
            name (str): The name of the oligo to be used when ordering the oligo.
            seq (str): This oligo's sequence.
            scale (str): Optionally override the default IDT scale code for this oligo.
            purification (str): Optionally override the default IDT purification code
                for this oligo.

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
                "Name": oligo.name,
                "Sequence": oligo.seq,
                "Scale": oligo.scale,
                "Purification": oligo.purification,
            }
            rows.append(oligo_data)
        cols = ["Name", "Sequence", "Scale", "Purification"]
        df = pd.DataFrame(data=rows, columns=cols)

        # construct output .xlsx file path
        # NOTE: this reads the INSTANCE attribute. It used to read IDTOrder.settings directly,
        # so self.output_dir was assigned in __init__ and then never consulted: setting
        # order.output_dir had no effect at all.
        output_dir = self.output_dir
        # makedirs, not mkdir: a nested path like "out/orders" raised FileNotFoundError
        os.makedirs(output_dir, exist_ok=True)
        time_stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(output_dir, f"{time_stamp}_idt_order.xlsx")

        # create an excel sheet using IDT oligo data
        # NOTE: pandas 2.0 removed ExcelWriter.save(); close() is the supported way to flush and
        # write the file, and it is also what the context manager calls.
        with pd.ExcelWriter(file_path, engine="xlsxwriter") as writer:
            df.to_excel(writer, sheet_name="Sheet1", index=False)

    def __str__(self):
        """String object representation."""
        return f"<IDT Order: {self.num_oligos} oligos>"

    def __repr__(self):
        """List object representation."""
        return self.__str__()
