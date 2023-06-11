=======
History
=======

1.1.0 (2023-06-12)
------------------

Changed
********
* Warning messages regarding failed import of the cython module were made more informative.
* Transitioned the project to use pyproject.toml and setup.cfg, and cleaned up legacy code from setup.py.

Fixed
******
* Fixed bug where calculating enrichment scores using the pure Python implementation would raise an AttributeError.
* Fixed bug where the pure Python implementation would raise an ImportError if numba is not already installed on the system.

1.0.1 (2023-06-11)
------------------
Minor patch addressing installation issues.

1.0.0 (2023-06-10)
------------------
First stable release.