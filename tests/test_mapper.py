# -*- coding: utf-8 -*-
"""
    tests.test_mapper
    ~~~~~~~~~~~~~~~~~

    :copyright: (c) 2018 by Tsuyoshi Tokuda.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from collections import OrderedDict

from pandas import DataFrame

from dfmapper import DataFrameMapper, DataFrameColumn

def test_init_1():
    class Test1Dfm(DataFrameMapper): pass

    test_1_dfm = Test1Dfm()

    assert test_1_dfm._columns is not None
    assert len(test_1_dfm._columns) is 0

    assert isinstance(test_1_dfm._columns, OrderedDict)
    assert isinstance(test_1_dfm._src_df, DataFrame)
    assert test_1_dfm._src_df.empty is True
    assert isinstance(test_1_dfm._working_df, DataFrame)
    assert test_1_dfm._working_df.empty is True

def test_init_2():
    class Test2Dfm(DataFrameMapper):
        id = DataFrameColumn(int)

    test_2_dfm = Test2Dfm()

    assert test_2_dfm._columns is not None
    assert len(test_2_dfm._columns) is 1
    assert hasattr(test_2_dfm, 'id')
    assert isinstance(test_2_dfm.id, DataFrameColumn)

    assert isinstance(test_2_dfm._columns, OrderedDict)
    assert isinstance(test_2_dfm._src_df, DataFrame)
    assert test_2_dfm._src_df.empty is True
    assert isinstance(test_2_dfm._working_df, DataFrame)
    assert test_2_dfm._working_df.empty is True

def test_init_3():
    class Test3Dfm(DataFrameMapper):
        id = DataFrameColumn(int)
        title = DataFrameColumn(str)

    test_3_dfm = Test3Dfm({
        'id': [1, 2, 3],
        'title': ['title_1', 'title_2', 'title_3']
    })

    assert test_3_dfm._columns is not None
    assert len(test_3_dfm._columns) is 2
    assert hasattr(test_3_dfm, 'id')
    assert isinstance(test_3_dfm.id, DataFrameColumn)
    assert hasattr(test_3_dfm, 'title')
    assert isinstance(test_3_dfm.title, DataFrameColumn)

    assert isinstance(test_3_dfm._columns, OrderedDict)
    assert isinstance(test_3_dfm._src_df, DataFrame)
    assert test_3_dfm._src_df.empty is False
    assert len(test_3_dfm._src_df) is 3
    assert isinstance(test_3_dfm._working_df, DataFrame)
    assert test_3_dfm._working_df.empty is False
    assert len(test_3_dfm._working_df) is 3
