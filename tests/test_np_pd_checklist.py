# -*- coding: utf-8 -*-
# pylint: disable
"""
    tests.test_numpy_dtypes
    ~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2018 by Tsuyoshi Tokuda.
    :license: MIT, see LICENSE for more details.
"""

import numpy as np
import pandas as pd

def test_basic_numpy_dtypes():
    assert np.int != np.int8
    assert np.int != np.int16
    assert np.int != np.int32
    assert np.int != np.int64

    assert np.int == int
    assert np.int8 != int
    assert np.int16 != int
    assert np.int32 != int
    assert np.int64 != int

    assert np.dtype(np.int) == np.dtype('int') == np.dtype(int)
    assert np.dtype(np.int8) == np.dtype('int8') == np.int8
    assert np.dtype(np.int16) == np.dtype('int16') == np.int16
    assert np.dtype(np.int32) == np.dtype('int32') == np.int32
    assert np.dtype(np.int64) == np.dtype('int64') == np.int64

def test_pandas_dtypes():
    assert pd.DataFrame([1, 2]).dtypes.values[0] == np.dtype('int64') == np.int64
    assert pd.DataFrame([1, 2, None]).dtypes.values[0] == np.dtype('float64') == np.float64

    assert pd.DataFrame([1.0, 2.0]).dtypes.values[0] == np.dtype('float64') == np.float64
    assert pd.DataFrame([1.0, 2.0, None]).dtypes.values[0] == np.dtype('float64') == np.float64

    assert pd.DataFrame([True, False]).dtypes.values[0] == np.dtype('bool') == np.bool
    assert pd.DataFrame([True, False, None]).dtypes.values[0] == np.dtype('object') == np.object

    assert pd.DataFrame(["A", "B"]).dtypes.values[0] == np.dtype('object') == np.object
    assert pd.DataFrame(["A", "B", None]).dtypes.values[0] == np.dtype('object') == np.object
