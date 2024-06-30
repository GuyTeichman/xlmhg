
History
=======



1.1.1 (2024-06-30)
------------------
xlmhglite now runs on numpy version 2 and above.

1.1.0 (2023-06-11)
------------------
This version improves clarity of warning messages and addresses some additional bugs.
Moreover, the project has been transitioned to use pyproject.toml and setup.cfg, and old code was cleaned up for better maintainability.

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