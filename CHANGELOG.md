# Changelog

All notable changes to this project are documented here. Hand-edited, newest first (canon/05).

## [Unreleased]

### Changed

- **Breaking:** `Oligo` now raises `ValueError` on an unrecognized scale or purification code,
  instead of calling `sys.exit()`. A library that exits kills its caller's process; a caller can
  catch a `ValueError`.

- Packaging brought to the develop-python canon: hatchling replaces setuptools, the version moves
  to `src/py_idt/_version.py`, and the package moves to a `src/` layout. No functional change to
  any module.
- `xlrd` dropped from the dependencies; it was declared but never imported.

### Fixed

- `IDTOrder.save()` no longer calls `pd.ExcelWriter.save()`, removed in pandas 2.0. Writing an
  order file raised `AttributeError` on every currently maintained pandas.

### Removed

- `build/`, `dist/` and `py_idt.egg-info/` are no longer tracked in git.
