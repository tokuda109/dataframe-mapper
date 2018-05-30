# -*- coding: utf-8 -*-
"""
    dfmapper.validator
    ~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2018 by Tsuyoshi Tokuda.
    :license: MIT, see LICENSE for more details.
"""

from abc import abstractmethod
from typing import Any

from numpy import issubdtype
from pandas import DatetimeIndex, Series, date_range, to_datetime

from dfmapper.exceptions import ValidationError

__all__ = (
    "Validator",
    "DateRangeValidator",
    "DtypeValidator",
    "MinValueValidator",
    "MaxValueValidator",
    "MaxLengthValidator",
    "NullableValidator"
)


class Validator:
    """
    The base validator class that defines some interfaces.

    .. versionchanged:: 0.0.2
    """

    def __init__(self, message: str = None):
        self.message = message

        self.value = None

    def clear(self):
        """
        .. versionchanged:: 0.0.2
        """
        self.value = None

    @abstractmethod
    def get_error(self) -> ValidationError:
        """
        :return:
        :rtype: dfmapper.ValidationError

        .. versionchanged:: 0.0.2
        """
        raise NotImplementedError()


class DateRangeValidator(Validator):
    """
    .. versionchanged:: 0.0.3
    """

    def __init__(self, date_range: DatetimeIndex, message=None):
        super().__init__(message)

        assert isinstance(date_range, DatetimeIndex)

        self.date_range = date_range

    def __call__(self, value: Series) -> bool:
        self.value = value

        from_date = to_datetime(min(self.date_range.tolist()).date())
        to_date = to_datetime(max(self.date_range.tolist()).date())

        in_range_amount = len(value.loc[
            (value > from_date) & (value <= to_date)
        ])

        return len(value) == in_range_amount

    def get_error(self) -> ValidationError:
        """
        :return:
        :rtype: dfmapper.ValidationError

        .. versionchanged:: 0.0.2
        """
        return ValidationError(self.message)


class DtypeValidator(Validator):
    """
    .. versionchanged:: 0.0.2
    """

    def __init__(self, dtype: Any, message=None):
        super().__init__(message)

        self.dtype = dtype

    def __call__(self, value: Series) -> bool:
        self.value = value

        return issubdtype(self.dtype, value.dtype)

    def get_error(self) -> ValidationError:
        """
        :return:
        :rtype: dfmapper.ValidationError

        .. versionchanged:: 0.0.2
        """
        return ValidationError(self.message)


class MinValueValidator(Validator):
    """
    .. versionchanged:: 0.0.2
    """

    def __init__(self, min_value: int, message=""):
        """
        :param min_value:
        :type: int
        :param message:
        :type: str
        """
        super().__init__(message)

        self.min_value = min_value

    def __call__(self, value: Series) -> bool:
        self.value = value

        return value.min() >= self.min_value

    def get_error(self) -> ValidationError:
        """
        :return:
        :rtype: dfmapper.ValidationError

        .. versionchanged:: 0.0.2
        """
        return ValidationError(self.message)


class MaxValueValidator(Validator):
    """
    .. versionchanged:: 0.0.2
    """

    def __init__(self, max_value: int, message=""):
        super().__init__(message)

        self.max_value = max_value

    def __call__(self, value: Series) -> bool:
        self.value = value

        return value.max() <= self.max_value

    def get_error(self) -> ValidationError:
        """
        :return:
        :rtype: dfmapper.ValidationError

        .. versionchanged:: 0.0.2
        """
        return ValidationError(self.message)


class MaxLengthValidator(Validator):
    """
    .. versionchanged:: 0.0.2
    """

    def __init__(self, max_length: int, message=""):
        super().__init__(message)

        self.max_length = max_length

    def __call__(self, value: Series) -> bool:
        self.value = value

        return value.str.len().max() <= self.max_length

    def get_error(self) -> ValidationError:
        """
        :return:
        :rtype: dfmapper.ValidationError

        .. versionchanged:: 0.0.2
        """
        return ValidationError(self.message)


class NullableValidator(Validator):
    """
    .. versionchanged:: 0.0.2
    """

    def __init__(self, nullable: bool = True, message=""):
        super().__init__(message)

        self.nullable = nullable

    def __call__(self, value: Series) -> bool:
        self.value = value

        has_null = True

        if not self.nullable:
            return not value.isnull().values.any()

        return has_null

    def get_error(self) -> ValidationError:
        """
        :return:
        :rtype: dfmapper.ValidationError

        .. versionchanged:: 0.0.2
        """
        return ValidationError(self.message)
