"""tests for the Oligo value object."""

import pytest

from py_idt_order import Oligo


def test_records_what_it_was_given():
    oligo = Oligo("probe_1", "ACGTACGTAC", "25nm", "STD")
    assert oligo.name == "probe_1"
    assert oligo.seq == "ACGTACGTAC"
    assert oligo.scale == "25nm"
    assert oligo.purification == "STD"


def test_length_is_derived_from_the_sequence():
    assert Oligo("p", "ACGT", "25nm", "STD").length == 4


def test_repr_carries_the_useful_fields():
    text = repr(Oligo("probe_1", "ACGT", "25nm", "STD"))
    assert "probe_1" in text and "4 bp" in text


def test_an_invalid_scale_is_rejected():
    with pytest.raises(ValueError, match="not a valid oligo scale"):
        Oligo("p", "ACGT", "not-a-scale", "STD")


def test_an_invalid_purification_is_rejected():
    with pytest.raises(ValueError, match="not a valid oligo purification"):
        Oligo("p", "ACGT", "25nm", "not-a-purification")
