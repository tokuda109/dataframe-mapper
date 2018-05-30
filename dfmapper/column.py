# -*- coding: utf-8 -*-
"""
    dfmapper.column
    ~~~~~~~~~~~~~~~

    A column in a DataFrame Mapper.

    :copyright: (c) 2018 by Tsuyoshi Tokuda.
    :license: MIT, see LICENSE for more details.
"""

from typing import Any, List, Optional

import numpy as np
import pandas as pd

from dfmapper.exceptions import (
    DataFrameMapperException,
    ValidatorDoesNotCallable
)
from dfmapper.validator import (
    Validator,
    DateRangeValidator,
    DtypeValidator,
    MinValueValidator,
    MaxValueValidator,
    MaxLengthValidator,
    NullableValidator
)

__all__ = (
    "BaseColumn",
    "BoolColumn",
    "DateTimeColumn",
    "FloatColumn",
    "IntColumn",
    "StrColumn",
    "create_column"
)


class BaseColumn(object):
    """
    .. versionchanged:: 0.0.2
    """

    #: A list of error messages.
    errors: List[DataFrameMapperException] = None

    #: A list of validators.
    validators: List[Validator] = None

    def __init__(self, dtype: np.dtype, *args, **kwargs):
        """
        Creates a new Column object.

        :param dtype: The numpy dtype to check the column.
        :type: numpy.dtype
        """
        self.errors = []
        self.validators = []

        self.dtype = dtype

        self.nullable = kwargs.get("nullable", True)

        self.null_types = kwargs.get("null_types", [])

        self.validators.append(NullableValidator(self.nullable))

    def __repr__(self) -> str:
        return "<BaseColumn> type: {}".format(self.dtype)

    def has_error(self) -> bool:
        return len(self.errors) > 0

    def validate(self, values: Any) -> bool:
        """
        :param values:
        :type: Any
        :return:
        :rtype: bool
        """
        self.errors = []

        for validator in self.validators:
            if not callable(validator):
                raise ValidatorDoesNotCallable()
    
            result = validator(values)

            if not result:
                self.errors.append(validator.get_error())

        return len(self.errors) == 0


class BoolColumn(BaseColumn):
    """
    .. versionchanged:: 0.0.2
    """

    def __init__(self, *args, **kwargs):
        super().__init__(bool, *args, **kwargs)

        self.validators.append(DtypeValidator(bool))

    def __repr__(self) -> str:
        return "<BoolColumn>"


class DateTimeColumn(BaseColumn):
    """
    .. versionchanged:: 0.0.3
    """

    def __init__(self, *args, **kwargs):
        super().__init__(bool, *args, **kwargs)

        self.validators.append(DtypeValidator(np.datetime64))

        self.start = kwargs.get("start", None)
        self.end = kwargs.get("end", None)

        if self.start and self.end:
            date_range = pd.date_range(start=self.start, end=self.end)
            self.validators.append(DateRangeValidator(date_range))

    def __repr__(self) -> str:
        return "<DateTimeColumn>"


class FloatColumn(BaseColumn):
    """
    .. versionchanged:: 0.0.2
    """

    def __init__(self, *args, **kwargs):
        super().__init__(float, *args, **kwargs)

        self.validators.append(DtypeValidator(np.float64))

    def __repr__(self) -> str:
        return "<FloatColumn>"


class IntColumn(BaseColumn):
    """
    .. versionchanged:: 0.0.2
    """

    def __init__(self, *args, **kwargs):
        super().__init__(np.int64, *args, **kwargs)

        self.min = kwargs.get("min", None)
        self.max = kwargs.get("max", None)

        if self.nullable:
            self.validators.append(DtypeValidator(np.float64))
        else:
            self.validators.append(DtypeValidator(np.int64))

        if self.min is not None:
            self.validators.append(MinValueValidator(self.min))

        if self.max is not None:
            self.validators.append(MaxValueValidator(self.max))

    def __repr__(self) -> str:
        return "<IntColumn> min: {}, max: {}".format(self.min, self.max)


class StrColumn(BaseColumn):
    """
    .. versionchanged:: 0.0.2
    """

    def __init__(self, *args, **kwargs):
        super().__init__(str, *args, **kwargs)

        self.max_length = kwargs.get("max_length", None)

        self.validators.append(DtypeValidator(object))

        if self.max_length is not None:
            self.validators.append(MaxLengthValidator(self.max_length))

    def __repr__(self) -> str:
        return "<StrColumn>"


def create_column(dtype: Any, *args, **kwargs) -> Optional[BaseColumn]:
    """
    :param dtype:
    :type: typing.Any
    :return:
    :rtype: typing.Optional[dfmapper.BaseColumn]

    .. versionchanged:: 0.0.2
    """
    if dtype == object or dtype == str:
        return StrColumn(args, kwargs)
    elif dtype == np.float64 or dtype == float:
        return FloatColumn(args, kwargs)
    elif dtype == np.int64 or dtype == int:
        return IntColumn(args, kwargs)
    else:
        return None
