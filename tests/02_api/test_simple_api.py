# Copyright (c) 2016-2019 Florian Wagner
#
# This file is part of XL-mHG.

"""Tests for the simple Python API (`xlmhg_test`)."""

import numpy as np
import platform
import pytest

from xlmhglite import mHGResult, xlmhg_test, get_xlmhg_test_result

IS_ARM = platform.processor() == 'arm'


@pytest.fixture
def my_indices(my_v):
    indices = np.uint16(np.nonzero(my_v)[0])
    return indices


def test_mhg(my_v):
    # test regular mHG test
    res = xlmhg_test(my_v)
    assert np.isclose(res[0], 0.01393188854489164, atol=0)
    assert res[1] == 6
    pval_truth = 0.0244453044375645
    if IS_ARM:
        assert np.isclose(res[1], pval_truth, atol=0)
    else:
        assert res[2] == truth


def test_X(my_v):
    # test effect of X
    res = xlmhg_test(my_v, X=4)
    pval_truth = 0.01876934984520124
    if IS_ARM:
        assert np.isclose(res[1], pval_truth, atol=0)
    else:
        assert res[2] == truth


def test_L(my_v):
    res = xlmhg_test(my_v, L=6)
    assert np.isclose(res[2], 0.019801341589267284, atol=0)


def test_result(my_ind, my_v):
    N = my_v.size
    result = get_xlmhg_test_result(N, my_ind)
    assert isinstance(result, mHGResult)


def test_limit_stat(my_incredible_stat_v):
    res = xlmhg_test(my_incredible_stat_v)
    assert res[0] == 0.0
    assert res[1] == 500
    assert res[2] == 0.0


def test_list_too_long(my_much_too_long_v):
    with pytest.raises(ValueError):
        result = xlmhg_test(my_much_too_long_v)


def test_table_too_small(my_N, my_ind, my_v):
    K = my_ind.size
    with pytest.raises(ValueError):
        table = np.empty(((my_N - K), (my_N - K)), np.longdouble)
        result = xlmhg_test(my_v, table=table)
