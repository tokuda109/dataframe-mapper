# -*- coding: utf-8 -*-
# pylint: disable
"""
    tests.test_column
    ~~~~~~~~~~~~~~~~~

    :copyright: (c) 2018 by Tsuyoshi Tokuda.
    :license: MIT, see LICENSE for more details.
"""

import numpy as np
from pandas import DataFrame

from dfmapper import (
    BoolColumn,
    FloatColumn,
    IntColumn,
    StrColumn,
    create_column
)

def test_bool_column():
    df_1 = DataFrame(data={'boolean': [True, False]})

    bool_col_1 = BoolColumn()

    assert bool_col_1.validate(df_1.boolean) is True


    df_2 = DataFrame(data={'boolean': [True, False, None]})

    bool_col_2 = BoolColumn()

    assert bool_col_2.validate(df_2.boolean) is False

def test_float_column():
    df_1 = DataFrame(data={'avg': [0.247, 0.304]})

    float_col_1 = FloatColumn(nullable=False)

    assert float_col_1.validate(df_1.avg) is True


    df_2 = DataFrame(data={'avg': [0.247, None]})

    float_col_2 = FloatColumn(nullable=False)

    assert float_col_2.validate(df_2.avg) is False


    df_3 = DataFrame(data={'avg': [0.247, 0.304]})

    float_col_3 = FloatColumn(nullable=True)

    assert float_col_3.validate(df_3.avg) is True


    df_4 = DataFrame(data={'avg': [0.247, None]})

    float_col_4 = FloatColumn(nullable=True)

    assert float_col_4.validate(df_4.avg) is True

def test_int_column():
    df_1 = DataFrame(data={'id': [1, 2], 'name': ['1', '2']})

    int_col_1 = IntColumn(min=1, max=5, nullable=False)

    assert int_col_1.validate(df_1.id) is True


    df_2 = DataFrame(data={'id': [1, None], 'name': ['1', '2']})

    int_col_2 = IntColumn(min=1, max=5, nullable=True)

    assert int_col_2.validate(df_2.id) is True


    df_3 = DataFrame(data={'id': [1, None], 'name': ['1', '2']})

    int_col_3 = IntColumn(min=1, max=5, nullable=False)

    assert int_col_3.validate(df_3.id) is False

def test_str_column():
    df_1 = DataFrame(data={'name': ['Rebecka Plumadore', 'Clemencia Spearman']})

    str_col_1 = StrColumn(max_length=20, nullable=False)

    assert str_col_1.validate(df_1.name) is True


    df_2 = DataFrame(data={'name': ['Rebecka Plumadore', 'Clemencia Spearman']})

    str_col_2 = StrColumn(max_length=5, nullable=False)

    assert str_col_2.validate(df_2.name) is False

def test_create_column():
    float_col_1 = create_column(np.float)

    assert isinstance(float_col_1, FloatColumn)

    float_col_2 = create_column(np.float64)

    assert isinstance(float_col_2, FloatColumn)

    float_col_3 = create_column(float)

    assert isinstance(float_col_3, FloatColumn)


    int_col_1 = create_column(np.int)

    assert isinstance(int_col_1, IntColumn)

    int_col_2 = create_column(np.int64)

    assert isinstance(int_col_2, IntColumn)

    int_col_3 = create_column(int)

    assert isinstance(int_col_3, IntColumn)


    str_col_1 = create_column(np.str)

    assert isinstance(str_col_1, StrColumn)

    str_col_2 = create_column(np.object)

    assert isinstance(str_col_2, StrColumn)

    str_col_3 = create_column(np.unicode)

    assert isinstance(str_col_3, StrColumn)
