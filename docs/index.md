# py_idt

A python interface for creating [IDT](https://www.idtdna.com/site/order/oligoentry) bulk oligo
order forms in Excel.

You design oligos in python; IDT wants a spreadsheet. `py_idt` is the bit in between: describe an
order in code, get an `.xlsx` you can upload to IDT's bulk input page.

## Install

```bash
pip install py_idt
```

## A first order

```python
from py_idt import IDTOrder

IDTOrder.settings["output_dir"] = "example_order"

order = IDTOrder()
order.add_oligo("Test_oligo_1", "ACGTACGTACGTACGTACGT")
order.save()
```

That writes `example_order/<timestamp>_idt_order.xlsx`.

```{toctree}
:maxdepth: 2
:hidden:

usage
api
changelog
```

## Where to go next

- [Usage](usage.md) — scales, purifications, defaults and overrides, and uploading to IDT.
- [API reference](api.md) — every public class and function.
- [Changelog](changelog.md) — what changed, newest first.
