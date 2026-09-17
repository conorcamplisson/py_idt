# Usage

## Orders and oligos

An **order** is a collection of oligos plus the defaults they inherit. An **oligo** is a name, a
sequence, a scale and a purification.

```python
from py_idt import IDTOrder

order = IDTOrder()
order.add_oligo("probe_1", "ACGTACGTACGTACGTACGT")
order.add_oligo("probe_2", "TGCATGCATGCATGCATGCA")
print(order)          # <IDT Order: 2 oligos>
```

## Defaults, and overriding them

The order carries a default scale and purification. Give them once on the order, and override per
oligo only where they differ:

```python
order = IDTOrder(scale="100nm", purification="HPLC")

order.add_oligo("probe_1", "ACGTACGTAC")                              # 100nm, HPLC
order.add_oligo("probe_2", "TGCATGCATG", scale="250nm",
                purification="PAGE")                                  # overridden
```

## Valid scale and purification codes

IDT accepts a fixed set of codes. An unrecognized one raises `ValueError` naming the valid
options:

```python
from py_idt import Oligo

Oligo("probe_1", "ACGT", "not-a-scale", "STD")
# ValueError: 'not-a-scale' is not a valid oligo scale.
#             Valid codes: 25nm, 100nm, 250nm, 1um, 5um, 10um, 4nmU, 20nmU, PU, 25nmS
```

To see the full tables, with what each code means:

```python
from py_idt.utils import get_scales, get_purifications

print(get_scales())
print(get_purifications())
```

## Modifications in a sequence

IDT modification codes go inline in the sequence, in their usual `/…/` form:

```python
order.add_oligo("phosphorylated", "/5Phos/AAAAACCCCCGGGGGTTTTT")
```

`py_idt` passes the sequence through unchanged; IDT validates it on upload.

## Where the file goes

Set it per order, which is usually what you want:

```python
order = IDTOrder(output_dir="example_order")
# or later:
order.output_dir = "somewhere/else"
```

`IDTOrder.settings["output_dir"]` is the process-wide default every order starts from. Prefer the
per-order form unless you really do want to move every order at once. Nested paths are created for
you.

`save()` creates the directory if needed and writes `<timestamp>_idt_order.xlsx`, so repeated runs
never overwrite each other.

## Uploading to IDT

1. Open IDT's [bulk input page](https://www.idtdna.com/site/order/oligoentry).
2. Upload the generated `.xlsx`.
3. Click **Update** to generate the oligos.
4. Add them to your cart and check out.
