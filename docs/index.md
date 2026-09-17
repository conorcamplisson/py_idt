# py_idt

A python interface for creating IDT bulk oligo order forms in Excel.

## Install

```bash
pip install py_idt
```

## Quickstart

```python
from py_idt import IDTOrder

# an order carries defaults that each oligo can override
order = IDTOrder(scale="100nm", purification="STD")

order.add_oligo("probe_1", "ACGTACGTACGTACGTACGT")
order.add_oligo("probe_2", "TGCATGCATGCATGCATGCA", scale="250nm", purification="PAGE")

# writes a timestamped .xlsx into IDTOrder.settings["output_dir"]
order.save()
```

## API reference

```{eval-rst}
.. automodule:: py_idt.idt_order
   :members:

.. automodule:: py_idt.oligo
   :members:

.. automodule:: py_idt.utils
   :members:
```
