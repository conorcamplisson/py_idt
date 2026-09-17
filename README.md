# py_idt

A python interface for creating [IDT](https://www.idtdna.com/site/order/oligoentry) bulk oligo order forms in Excel.

[![PyPI](https://img.shields.io/pypi/v/py_idt.svg)](https://pypi.org/project/py_idt/)
[![Python versions](https://img.shields.io/pypi/pyversions/py_idt.svg)](https://pypi.org/project/py_idt/)
[![CI](https://github.com/conorcamplisson/py_idt/actions/workflows/ci.yml/badge.svg)](https://github.com/conorcamplisson/py_idt/actions/workflows/ci.yml)
[![Docs](https://img.shields.io/badge/docs-latest-blue.svg)](https://conorcamplisson.github.io/py_idt/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

You might find this module useful if you design DNA oligos in python and then order them from IDT.

## Install

```bash
pip install py_idt
```

## Quickstart

```python
from py_idt import IDTOrder

# where the .xlsx will be written
IDTOrder.settings['output_dir'] = 'example_order'

# an order carries defaults that each oligo can override
order = IDTOrder()

order.add_oligo('Test_oligo_1', 'ACGTACGTACGTACGTACGT')
order.add_oligo('Test_oligo_2', 'TGCATGCATGCATGCATGCATGCATGCATGCATGCATGCA',
                scale='250nm', purification='PAGE')
order.add_oligo('Test_oligo_3', '/5Phos/AAAAACCCCCGGGGGTTTTT',
                scale='100nm', purification='HPLC')

# write the IDT bulk order form
order.save()
```

That writes an Excel file suitable for upload to IDT's custom DNA oligo bulk input form:

`example_order/<timestamp>_idt_order.xlsx`

[![Example IDT Order](./images/idt_example_order.PNG)](#)

A runnable version of this is in [examples/basic_order.py](./examples/basic_order.py).

## Ordering from the generated file

1. Upload the Excel file to IDT's Bulk Input page: https://www.idtdna.com/site/order/oligoentry

   [![IDT bulk input](./images/idt_bulk_input.PNG)](#)

2. Click "Update" to generate the oligos.

   [![IDT oligo input](./images/idt_oligo_input.PNG)](#)

3. Add the oligos to your cart and check out.

   [![IDT checkout](./images/idt_checkout.PNG)](#)

## Documentation

Full documentation, including the API reference, is at
<https://conorcamplisson.github.io/py_idt/>.

## License

MIT. See [LICENSE](./LICENSE).
