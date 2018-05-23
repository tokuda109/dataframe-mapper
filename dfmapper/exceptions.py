# -*- coding: utf-8 -*-
"""
    dfmapper.exceptions
    ~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2018 by Tsuyoshi Tokuda.
    :license: MIT, see LICENSE for more details.
"""

__all__ = (
    "DataFrameMapperException",
    "ValidationError",
    "ValidatorDoesNotCallable"
)


class DataFrameMapperException(Exception):
    """Plain DataFrame Mapper exception."""

    pass


class ValidationError(DataFrameMapperException):
    """An error while validating data."""

    def __init__(self, message: str):
        super().__init__(message)

        self.message = message


class ValidatorDoesNotCallable(DataFrameMapperException):
    """Validator is not a function or subclass of class:`dfmapper.Validator`."""

    def __init__(self):
        super().__init__("Validator doesn't callable.")
