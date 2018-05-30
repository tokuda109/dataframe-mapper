# -*- coding: utf-8 -*-
# pylint: disable
"""
    tests.test_validator
    ~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2018 by Tsuyoshi Tokuda.
    :license: MIT, see LICENSE for more details.
"""

import numpy as np
from pandas import Series, date_range, to_datetime

from dfmapper import (
    DateRangeValidator,
    DtypeValidator,
    MinValueValidator,
    MaxValueValidator,
    MaxLengthValidator,
    NullableValidator
)

def test_date_range_validator():
    series_1 = Series(['2018-01-15 12:00:00', '2018-01-15 13:00:00'])
    series_1 = to_datetime(series_1)

    date_range_validator_1 = DateRangeValidator(date_range(start='2018-01-01', end='2018-01-30'))

    assert date_range_validator_1(series_1) == True


    series_2 = Series(['2018-01-15 12:00:00', '2018-01-15 13:00:00'])
    series_2 = to_datetime(series_2)

    date_range_validator_2 = DateRangeValidator(date_range(start='2018-01-20', end='2018-01-30'))

    assert date_range_validator_2(series_2) == False

def test_type_validator():
    series_1 = Series([1, 2, 3, 4, 5], dtype='int')

    dtype_validator_1 = DtypeValidator(dtype=np.int64)

    assert dtype_validator_1(series_1) == True


    series_2 = Series([1, 2, 3, 4, None])

    dtype_validator_2 = DtypeValidator(dtype=np.float64)

    assert dtype_validator_2(series_2) == True


    series_3 = Series([1.0, 2.0, 3.0])

    dtype_validator_3 = DtypeValidator(dtype=np.float64)

    assert dtype_validator_3(series_3) == True


    series_4 = Series([1.0, 2.0, None])

    dtype_validator_4 = DtypeValidator(dtype=np.float64)

    assert dtype_validator_4(series_4) == True


    series_5 = Series([True, False])

    dtype_validator_5 = DtypeValidator(dtype=np.bool)

    assert dtype_validator_5(series_5) == True


    series_6 = Series([True, False, None])

    dtype_validator_6 = DtypeValidator(dtype=object)

    assert dtype_validator_6(series_6) == True


    series_7 = Series(["YES", "NO"])

    dtype_validator_7 = DtypeValidator(dtype=object)

    assert dtype_validator_7(series_7) == True

def test_min_value_validator():
    series = Series([1, 2, 3, 4, 5], dtype='int')

    min_validator_1 = MinValueValidator(2)

    assert min_validator_1(series) == False
    assert series.equals(min_validator_1.value)

    min_validator_1.clear()

    assert min_validator_1.value == None


    min_validator_2 = MinValueValidator(1)

    assert min_validator_2(series) == True
    assert series.equals(min_validator_2.value)

    min_validator_2.clear()

    assert min_validator_2.value == None

def test_max_value_validator():
    series = Series([1, 2, 3, 4, 5], dtype='int')

    max_validator_1 = MaxValueValidator(4)

    assert max_validator_1(series) == False
    assert series.equals(max_validator_1.value)

    max_validator_1.clear()

    assert max_validator_1.value == None


    max_validator_2 = MaxValueValidator(5)

    assert max_validator_2(series) == True
    assert series.equals(max_validator_2.value)

    max_validator_2.clear()

    assert max_validator_2.value == None

def test_max_length_validator():
    series_1 = Series(["abcdef", "abcd"], dtype='str')

    max_length_validator_1 = MaxLengthValidator(max_length=3)

    assert max_length_validator_1(series_1) == False
    assert series_1.equals(max_length_validator_1.value)

    max_length_validator_1.clear()

    assert max_length_validator_1.value == None


    series_2 = Series(["abcdef", "abcd"], dtype='str')

    max_length_validator_2 = MaxLengthValidator(max_length=10)

    assert max_length_validator_2(series_2) == True
    assert series_2.equals(max_length_validator_2.value)

    max_length_validator_2.clear()

    assert max_length_validator_2.value == None

def test_nullable_validator():
    series_1 = Series([1, None, 3, 4, 5])

    nullable_validator_1 = NullableValidator(nullable=True)

    assert nullable_validator_1(series_1) == True

    nullable_validator_2 = NullableValidator(nullable=False)

    assert nullable_validator_2(series_1) == False


    series_2 = Series([1, 2, 3, 4, 5])

    nullable_validator_3 = NullableValidator(nullable=True)

    assert nullable_validator_3(series_2) == True

    nullable_validator_4 = NullableValidator(nullable=False)

    assert nullable_validator_4(series_2) == True
