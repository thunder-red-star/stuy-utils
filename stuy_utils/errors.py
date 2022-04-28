"""Defines custom exceptions used for StuyUtils."""


class StuyException(Exception):
    """Base exception class for StuyUtils."""


class InvalidDate(StuyException):
    """Thrown if the input is not a date or datetime object."""

    def __init__(self, day):
        self.day = day
        super().__init__(f"'{day}' is not a date or datetime object.")


class DayNotInData(StuyException):
    """Thrown if the inputted day is not in term_days.csv."""

    def __init__(self, day):
        self.day = day
        super().__init__(f"Unable to access '{day}' from the data.")


class DeprecatedMethod(StuyException):
    """Thrown if the method is no longer supported."""

    def __init__(self, method):
        self.method = method
        super().__init__(f"{method} is not or no longer supported.")