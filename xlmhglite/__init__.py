__version__ = '1.1.0'

import warnings


def cython_warning():
    warnings.warn('Failed to import the "mhg_cython" C extension.'
                  'Falling back to the pure Python implementation, which is very slow.', ImportWarning)


from .result import mHGResult
from .test import get_xlmhg_O1_bound, xlmhg_test, get_xlmhg_test_result
from .visualize import get_result_figure

__all__ = (mHGResult, get_xlmhg_O1_bound, xlmhg_test, get_xlmhg_test_result, get_result_figure)
