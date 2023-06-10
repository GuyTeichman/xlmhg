XL-mHG Lite
=============


**Useful links:** `Documentation <https://guyteichman.github.io/xlmhglite>`_ |
`Source code <https://github.com/GuyTeichman/xlmhglite>`_ |
`Bug reports <https://github.com/GuyTeichman/xlmhglite/issues>`_ | |pipimage| | |versionssupported| | |githubactions| | |downloads| | |license|

`xlmhg` is an efficient Python/Cython implementation of the semiparametric
`XL-mHG test`__ for enrichment in ranked lists. The XL-mHG test is an extension
of the nonparametric `mHG test`__, which was developed by `Dr. Zohar
Yakhini`__ and colleagues.

`xlmhglite` is a fork of the original `xlmhg` package (which is unfortunately no longer being maintained).
This fork was updated to support modern Python versions (Python >=3.8), fix bugs in the original implementation,
and reduce the mandatory dependencies of the project to a minimum.
To that end, the plotting functionality of `xlmhg` is not part of the core `xlmhglite` package, instead being an optional requirement.

__ xlmhg_paper_
__ mhg_paper_
__ zohar_

Installation
------------

To install the core ("lite") version of `xlmhglite`:
.. code-block:: bash

    $ pip install xlmhglite

To install the complete version of `xlmhglite` (including the plotting functionality):
.. code-block:: bash

    $ pip install xlmhglite['all']

Getting started
---------------

The `xlmhglite` package provides two functions (one simple and more more advanced)
for performing XL-mHG tests. These functions are documented in the
`User Manual`__. Here's a quick example using the "simple" test function:

.. code-block:: python

    import xlmhglite
    stat, cutoff, pval = xlmhglite.xlmhg_test(v, X, L)

Where: ``v`` is the ranked list of 0's and 1's, represented by a NumPy array of
integers, ``X`` and ``L`` are the XL-mHG parameters, and the return values have
the following meanings:

- ``stat``: The XL-mHG test statistic
- ``cutoff``: The cutoff at which XL-mHG test statistic was attained
- ``pval``: The XL-mHG p-value

__ user_manual_

Documentation
-------------

Please refer to the `XL-mHG User Manual`__ (hosted on ReadTheDocs).

__ user_manual_

Citing XL-mHG
-------------

If you use the XL-mHG test in your research, please cite `Eden et al. (PLoS
Comput Biol, 2007)`__ and `Wagner (PLoS One, 2015)`__.

__ mhg_paper_
__ go_pca_paper_

Copyright and License
---------------------

Copyright (c) 2015-2019 Florian Wagner

::

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice, this
    list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.

    * Neither the name of the copyright holder nor the names of its
    contributors may be used to endorse or promote products derived from
    this software without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


.. _xlmhg_paper: https://doi.org/10.7287/peerj.preprints.1962v2

.. _zohar: http://bioinfo.cs.technion.ac.il/people/zohar

.. _mhg_paper: https://dx.doi.org/10.1371/journal.pcbi.0030039

.. _go_pca_paper: https://dx.doi.org/10.1371/journal.pone.0143196

.. _user_manual: https://guyteichman.github.io/xlmhglite

.. |license| image:: https://img.shields.io/pypi/l/xlmhglite.svg
    :target: https://pypi.python.org/pypi/xlmhg
    :alt: License


.. |pipimage| image:: https://img.shields.io/pypi/v/xlmhglite.svg
    :target: https://pypi.python.org/pypi/xlmhglite
    :alt: PyPI version
.. |downloads| image:: https://pepy.tech/badge/xlmhglite
    :target: https://pepy.tech/project/xlmhglite
    :alt: Downloads
.. |versionssupported| image:: https://img.shields.io/pypi/pyversions/xlmhglite.svg
    :target: https://pypi.python.org/pypi/xlmhglite
    :alt: Python versions supported

..  |githubactions| image:: https://github.com/guyteichman/xlmhglite/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/GuyTeichman/xlmhglite/actions/workflows/tests.yml
    :alt: Build status