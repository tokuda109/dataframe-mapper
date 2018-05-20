# -*- coding: utf-8 -*-
"""
    dataframe-mapper.column
    ~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2018 by Tsuyoshi Tokuda.
    :license: MIT, see LICENSE for more details.
"""

__all__ = (
    "DataFrameColumn"
)


class DataFrameColumn(object):

    def __init__(self, *args, **kwargs):
        self.type = type(list(args).pop(0))
        # self.nullable = kwargs.pop('nullable', True)

    def __repr__(self):
        return "<DataFrameColumn> type: {}".format(
            self.type
        )
