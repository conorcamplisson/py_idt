"""tests for assembling and writing an order."""

from pathlib import Path

from py_idt import IDTOrder


def test_a_new_order_is_empty():
    order = IDTOrder()
    assert order.num_oligos == 0
    assert order.oligos == []


def test_adding_oligos_counts_them():
    order = IDTOrder()
    order.add_oligo("probe_1", "ACGTACGTAC")
    order.add_oligo("probe_2", "TGCATGCATG")
    assert order.num_oligos == 2
    assert [o.name for o in order.oligos] == ["probe_1", "probe_2"]


def test_an_oligo_inherits_the_order_defaults():
    order = IDTOrder(scale="100nm", purification="HPLC")
    order.add_oligo("probe_1", "ACGT")
    assert order.oligos[0].scale == "100nm"
    assert order.oligos[0].purification == "HPLC"


def test_an_oligo_can_override_the_order_defaults():
    order = IDTOrder(scale="100nm", purification="HPLC")
    order.add_oligo("probe_1", "ACGT", scale="250nm", purification="PAGE")
    assert order.oligos[0].scale == "250nm"
    assert order.oligos[0].purification == "PAGE"


def test_save_writes_an_xlsx(tmp_path, monkeypatch):
    # settings is a CLASS attribute, so point it at tmp_path for the duration of this test
    monkeypatch.setitem(IDTOrder.settings, "output_dir", str(tmp_path / "orders"))
    order = IDTOrder()
    order.add_oligo("probe_1", "ACGTACGTAC")
    order.save()

    written = list(Path(tmp_path / "orders").glob("*_idt_order.xlsx"))
    assert len(written) == 1, f"expected one .xlsx, found {written}"
    assert written[0].stat().st_size > 0


def test_output_dir_is_per_order_not_global(tmp_path):
    # the regression: self.output_dir was set in __init__ and never read back, so assigning it
    # (or passing output_dir=) silently went to the class-wide setting instead
    one = IDTOrder(output_dir=str(tmp_path / "one"))
    two = IDTOrder(output_dir=str(tmp_path / "two"))
    one.add_oligo("probe_1", "ACGT")
    two.add_oligo("probe_2", "TGCA")
    one.save()
    two.save()
    assert len(list((tmp_path / "one").glob("*.xlsx"))) == 1
    assert len(list((tmp_path / "two").glob("*.xlsx"))) == 1


def test_assigning_output_dir_after_construction_works(tmp_path):
    order = IDTOrder()
    order.output_dir = str(tmp_path / "later")
    order.add_oligo("probe_1", "ACGT")
    order.save()
    assert len(list((tmp_path / "later").glob("*.xlsx"))) == 1


def test_a_nested_output_dir_is_created(tmp_path):
    # os.mkdir could not create intermediate directories; os.makedirs can
    order = IDTOrder(output_dir=str(tmp_path / "deeply" / "nested" / "out"))
    order.add_oligo("probe_1", "ACGT")
    order.save()
    assert len(list((tmp_path / "deeply" / "nested" / "out").glob("*.xlsx"))) == 1
