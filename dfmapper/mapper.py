# -*- coding: utf-8 -*-
"""
    dfmapper.mapper
    ~~~~~~~~~~~~~~~

    :copyright: (c) 2018 by Tsuyoshi Tokuda.
    :license: MIT, see LICENSE for more details.
"""

from collections import OrderedDict
from typing import List, Optional, Union

from pandas import DataFrame

from dfmapper.column import create_column, BaseColumn
from dfmapper.exceptions import ValidationError, ValidatorDoesNotCallable

__all__ = (
    "DataFrameMapper"
)


class DataFrameMetaClass(type):
    """
    .. versionchanged:: 0.0.1
    """

    def __new__(cls, name, bases, attrs, **kwargs):
        new_class = super(DataFrameMetaClass, cls).__new__(
            cls,
            name,
            bases,
            attrs,
            **kwargs
        )

        new_class._columns = OrderedDict()

        for column_name, column in attrs.items():
            if isinstance(column, BaseColumn):
                new_class._columns[column_name] = column

        return new_class


class DataFrameMapper(dict, metaclass=DataFrameMetaClass):
    """
    .. versionchanged:: 0.0.1
    """

    #: source DataFrame.
    #:
    #: .. versionadded:: 0.0.1
    _src_df: Optional[DataFrame] = None

    #: working DataFrame.
    #:
    #: .. versionadded:: 0.0.1
    _working_df: Optional[DataFrame] = None

    #: List of columns.
    #:
    #: .. versionadded:: 0.0.1
    _columns: Optional[List[BaseColumn]] = None

    #: List of errors.
    #:
    #: .. versionadded:: 0.0.2
    _errors: List[ValidationError] = []

    def __init__(self, df_or_definition: Union[DataFrame, dict] = None) -> None:
        """
        Constructor for :class:`DataFrameMapper`.

        :param df_or_definition:
        :type: Union[pandas.DataFrame, dict, None]

        .. versionadded:: 0.0.1
        """
        if isinstance(df_or_definition, DataFrame):
            self._src_df = df_or_definition
        elif isinstance(df_or_definition, dict):
            self._src_df = DataFrame(df_or_definition)
        elif df_or_definition is None:
            self._src_df = DataFrame()
        else:
            raise TypeError("must be pandas.DataFrame or dict, not {}".format(
                type(df_or_definition)
            ))

        for key in self._src_df.columns:
            if not key in self._columns:
                self._columns[key] = create_column(self._src_df[key].dtype)

            if not hasattr(self, key):
                setattr(self, key, self._columns[key])

        self._working_df = self._src_df.copy()

    @property
    def df(self) -> DataFrame:
        """
        Return working :class:`pandas.DataFrame`.

        :return: return `DataFrameMapper._working_df`.
        :rtype: pandas.DataFrame

        .. versionadded:: 0.0.1
        """
        return self._working_df

    def is_valid(self) -> bool:
        """
        Return True if the :class:`DataFrameMapper` has no errors,
        or False otherwise. And raise a :exc:`ValidatorDoesNotCallable` if
        validator does not callable.

        :return: validation result.
        :rtype: bool
        :raise ValidatorDoesNotCallable: if validator does not callable.

        .. versionadded:: 0.0.1
        """
        self._errors = []

        valid_amount = 0

        for key in self._columns:
            validator = self._columns[key]
            try:
                if validator.validate(self.df[key]):
                    valid_amount += 1
                else:
                    self._errors.append(validator.get_error())
            except ValidatorDoesNotCallable as e:
                raise ValidatorDoesNotCallable()

        return valid_amount == len(self._columns)
