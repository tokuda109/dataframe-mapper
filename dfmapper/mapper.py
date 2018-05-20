# -*- coding: utf-8 -*-
"""
    dfmapper.mapper
    ~~~~~~~~~~~~~~~

    :copyright: (c) 2018 by Tsuyoshi Tokuda.
    :license: MIT, see LICENSE for more details.
"""

from collections import OrderedDict

from pandas import DataFrame

from .column import DataFrameColumn

__all__ = (
    "DataFrameMapper"
)


class DataFrameMetaClass(type):

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
            if not isinstance(column, DataFrameColumn):
                continue

            new_class._columns[column_name] = column

        return new_class


class DataFrameMapper(dict, metaclass=DataFrameMetaClass):

    #: source DataFrame
    _src_df = None

    #: working DataFrame
    _working_df = None

    #: DataFrameColumn list
    _columns = None

    def __init__(self, df_or_definition=None):
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
                self._columns[key] = DataFrameColumn(self._src_df[key].dtypes)

            if not hasattr(self, key):
                setattr(self, key, self._columns[key])

        self._working_df = self._src_df.copy()
