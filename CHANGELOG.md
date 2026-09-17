# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1] - 2026-09-17

`0.1.0` was tagged but its release run failed before publishing, so `0.1.1` is the first
published version. The changes below are everything since the pre-packaging code.

### Added

- `IDTOrder(output_dir=...)`, and assigning `order.output_dir`, now control where that order is
  written. Previously the only way to choose a directory was `IDTOrder.settings["output_dir"]`,
  which every order in the process shares.
- `IDTOrder.save(path=...)` writes to an exact file of your choosing, creating parent directories
  as needed.
- `IDTOrder.save()` returns the path it wrote, so the caller no longer has to re-derive a
  timestamped filename to find the file.

### Changed

- The changelog follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
- Every link and image in the README is an absolute URL. They were relative, so the screenshots and
  file links rendered broken on the PyPI project page while looking correct on GitHub.

- `Oligo`'s validation errors name the valid codes on one line, rather than embedding the full
  printable table. `utils.scale_codes()` and `utils.purification_codes()` are the compact form;
  `get_scales()` and `get_purifications()` still return the table a human reads.
- **Breaking:** `Oligo` now raises `ValueError` on an unrecognized scale or purification code,
  instead of calling `sys.exit()`. A library that exits kills its caller's process; a caller can
  catch a `ValueError`.

- Packaging brought to the develop-python canon: hatchling replaces setuptools, the version moves
  to `src/py_idt/_version.py`, and the package moves to a `src/` layout. No functional change to
  any module.
- `xlrd` dropped from the dependencies; it was declared but never imported.
- A nested `output_dir` such as `out/orders` is created rather than raising `FileNotFoundError`.

### Fixed

- `IDTOrder.save()` no longer calls `pd.ExcelWriter.save()`, removed in pandas 2.0. Writing an
  order file raised `AttributeError` on every currently maintained pandas.

### Removed

- `build/`, `dist/` and `py_idt.egg-info/` are no longer tracked in git.
- The source distribution no longer contains the rendered docs site. It carried `docs/_build/`,
  fonts included, at 2.4 MB against a 6.8 KB wheel; sdist contents are now declared explicitly.

[Unreleased]: https://github.com/conorcamplisson/py_idt/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/conorcamplisson/py_idt/releases/tag/v0.1.1
