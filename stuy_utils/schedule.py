"""Hey ACPlayGames, going through and using your comment format was a pain but I tried my best :hugging:."""

"""Functions for retriving schedule and day info of a day in the semester."""

import csv
from collections import namedtuple
from datetime import date
from datetime import datetime as dt
from datetime import time
from pathlib import Path
from typing import Dict, Optional, Tuple, Union

from stuy_utils import errors

Info = namedtuple("Info", ("school", "cycle", "schedule", "testing", "events"))
Time = namedtuple("Time", ("start", "end"))

TERM_PATH = f"{Path(__file__).parent}/data/term_days.tsv"
REGULAR_BELLS_PATH = f"{Path(__file__).parent}/data/regular.tsv"
CONFERENCE_BELLS_PATH = f"{Path(__file__).parent}/data/conference.tsv"
HOMEROOM_BELLS_PATH = f"{Path(__file__).parent}/data/homeroom.tsv"

with open(TERM_PATH, "r") as term_tsv, open(REGULAR_BELLS_PATH, "r") as regular_tsv, open(CONFERENCE_BELLS_PATH, "r") as conference_tsv, open(HOMEROOM_BELLS_PATH, "r") as homeroom_tsv:
    TERM_DAYS = {row[0]: Info(*row[1:]) for row in list(csv.reader(term_tsv, delimiter="\t"))[1:]}
    REGULAR_BELL_SCHEDULE = {row[0]: Time(*[time.fromisoformat(element) for element in row[1:]]) for row in list(csv.reader(regular_tsv, delimiter="\t"))[1:]}
    CONFERENCE_BELL_SCHEDULE = {row[0]: Time(*[time.fromisoformat(element) for element in row[1:]]) for row in list(csv.reader(conference_tsv, delimiter="\t"))[1:]}
    HOMEROOM_BELL_SCHEDULE = {row[0]: Time(*[time.fromisoformat(element) for element in row[1:]]) for row in list(csv.reader(homeroom_tsv, delimiter="\t"))[1:]}


def convert_12h_to_24h(hours12: str) -> str:
    """Converts a 12-hour time to a 24-hour time.

    Converts a 12-hour time to a 24-hour time by adding 12 hours to the
    hour if the time is in the PM.

    Args:
        hours12: A string representing a 12-hour time.
        e.g "1:00 PM"

    Raises:
        errors.InvalidTime: Thrown if the input is not a string.
        errors.InvalidTime: Thrown if the input isn't a 12 hour time (i.e. doesn't contain AM or PM, or hours > 12).

    Returns:
        str: A string representing a 24 hour time, with 0 prepended to the front of the time if the hour is less than 10.
    """

    if not isinstance(hours12, str):
        raise errors.InvalidTime(hours12)

    if "AM" in hours12 or "PM" in hours12:
        hours12 = hours12.split(" ")[0]
    else:
        raise errors.InvalidTime(hours12)

    if ":" not in hours12:
        raise errors.InvalidTime(hours12)

    hours, minutes = hours12.split(":")

    if int(hours) > 12:
        raise errors.InvalidTime(hours12)

    if "PM" in hours12:
        hours = str(int(hours) + 12)

    if int(hours) < 10:
        hours = f"0{hours}"

    return f"{hours}:{minutes}"

def convert_24h_to_minutes(hours24: str) -> int:
    """Convert a 24-hour time to minutes.

    Converts a 24-hour time to minutes by converting the hours and minutes

    Args:
        hours24: A string representing a 24-hour time.
        e.g "13:00"

    Raises:
        errors.InvalidTime: Thrown if the input is not a string.
        errors.InvalidTime: Thrown if the input isn't a 24 hour time (i.e. doesn't contain :, or hours > 24).

    Returns:
        int: The number of minutes since midnight.
    """

    if not isinstance(hours24, str):
        raise errors.InvalidTime(hours24)

    if ":" not in hours24:
        raise errors.InvalidTime(hours24)

    hours, minutes = hours24.split(":")

    if int(hours) > 24:
        raise errors.InvalidTime(hours24)

    return int(hours) * 60 + int(minutes)

def convert_to_isoformat(day: Union[date, dt]) -> str:
    """Convert a date object to an ISO-formatted date string.

    Convert a date or datetime object from the datetime library to a string
    formatted using the ISO 8601 format, while also checking if 'date' is a
    valid date and if it exists in the data.

    Args:
        day (Union[datetime.date, datetime.datetime]): A date or datetime
        object from the datetime library.

    Raises:
        errors.InvalidDate: Thrown if the input is not a date or a datetime
        object.
        errors.DayNotInData: Thrown if the inputted day is not in
        term_days.csv.

    Returns:
        str: A date using the ISO 8601 format (yyyy-mm-dd).
    """
    if not isinstance(day, date):
        raise errors.InvalidDate(day)

    if isinstance(day, dt):
        day = day.date()  # Converts datetime to date to remove time

    iso_date = day.isoformat()

    # if this code is not commented out, it will throw errors since TERM_DAYS is nonexistent.
    """
    if iso_date not in TERM_DAYS:
        raise errors.DayNotInData(iso_date)
    """

    return iso_date


def get_day_info(day: Union[date, dt]) -> Info:
    """Returns information about a given day.

    Returns the cycle, period, testing subjects, and any events of a given
    day. If a category does not apply, a value of None is returned.

    Args:
        day (Union[datetime.date, datetime.datetime]): A date or datetime
        object from the datetime library.

    Raises:
        errors.InvalidDate: Thrown if the input is not a date or a datetime
        object.
        errors.DayNotInData: Thrown if the inputted day is not in
        term_days.csv.

    Returns:
        Info: A namedtuple with fields 'school', 'cycle', 'schedule', 'testing', and 'events'.
    """

    if not isinstance(day, date):
        raise errors.InvalidDate(day)

    if isinstance(day, dt):
        day = day.date()  # Converts datetime to date to remove time

    iso_date = day.isoformat()

    if iso_date not in TERM_DAYS:
        raise errors.DayNotInData(iso_date)

    ret_tuple = Info(
        school=True if TERM_DAYS[iso_date]["school"] != "True" else False,
        cycle=TERM_DAYS[iso_date]["cycle"] if TERM_DAYS[iso_date]["cycle"] != "None" else None,
        schedule=TERM_DAYS[iso_date]["schedule"] if TERM_DAYS[iso_date]["schedule"] != "None" else None,
        testing=TERM_DAYS[iso_date]["testing"] if TERM_DAYS[iso_date]["testing"] != "None" else None,
        events=TERM_DAYS[iso_date]["events"] if TERM_DAYS[iso_date]["events"] != "None" else None,
    )



def get_next_school_day(
        day: Union[date, dt], always_same: bool = False) -> Optional[date]:
    """Returns when the next school day is.

    Returns a date object of the next school day from the given day. The given
    datetime will be returned as a date if school is still in session.

    Args:
        day (Union[datetime.date, datetime.datetime]): A date or datetime
        object from the datetime library.
        always_same (bool, optional): Whether or not to always return the given
        day if the given day is a school day. Defaults to False.

    Raises:
        errors.InvalidDate: Thrown if the input is not a datetime object.
        errors.DayNotInData: Thrown if the inputted day is not in
        term_days.csv.

    Returns:
        Optional[datetime.date]: A date object with the year, month, and day
        of the next school day.
    """

    """
    schedule_list = list(TERM_DAYS.items())
    day_index = list(TERM_DAYS).index(convert_to_isoformat(day))

    dt_ = day

    if not isinstance(dt_, dt):
        # Converts date to datetime with time 12:00 AM
        dt_ = dt.combine(dt_, time.min)

    # Loops through each day during or after the given day
    for day_ in schedule_list[day_index:]:
        # Return the same day if always_same is True, or if the given day is
        # before school is over (before AIS Tutoring ends)
        if always_same or (day_[1].cycle and dt_ <= dt.combine(
                date.fromisoformat(day_[0]),
                BELL_SCHEDULE["AIS Tutoring"].end)):
            return date.fromisoformat(day_[0])

    return None
    """

    raise errors.DeprecatedMethod("get_next_school_day")


def get_bell_schedule(day: Union[date, dt]) -> Dict[str, Time]:
    """Returns the bell periods of the next school day.

    Returns a dictionary of bell periods of the next school day. If the given
    day is a school day, then the bell schedule of that day will be returned,
    even if it is afterschool.

    Args:
        day (Union[datetime.date, datetime.datetime]): A date or datetime
        object from the datetime library.

    Raises:
        errors.InvalidDate: Thrown if the input is not a datetime object.
        errors.DayNotInData: Thrown if the inputted day is not in
        term_days.csv.

    Returns:
        Dict[str, Time]: A dictionary of keys of strings of the category name
        (see data/bell_schedule.csv) and values of Time namedtuple objects with
        fields 'start' and 'end', which returns a datetime object.
    """

    """
    return {cat[0]:  # key with category name (e.g. "Period 1")
            # Creates a Time namedtuple with the datetimes of the next school
            # day combined with the start and end times of the current category
            Time(*[dt.combine(get_next_school_day(day), time)
                   for time in cat[1]])  # Loop through the start and end times
            for cat in BELL_SCHEDULE.items()}  # Loop through the categories
    """
    raise errors.DeprecatedMethod("get_bell_schedule")

def get_current_class(day: dt) -> Optional[Tuple[str, Time]]:
    """Returns information of the current class.

    Returns a tuple of information of the current class, where the first
    element is a string of the category, such as the class period, and a Time
    namedtuple object, which includes when said period starts and ends.

    Args:
        day (datetime.datetime): A datetime object from the datetime library.

    Raises:
        errors.InvalidDate: Thrown if the input is not a datetime object.
        errors.DayNotInData: Thrown if the inputted day is not in
        term_days.csv.

    Returns:
        Optional[Tuple[str, Time]]: A tuple of a string of the category name
        (see data/bell_schedule.csv), and a Time namedtuple object with fields
        'start' and 'end', which returns a datetime object.
    """
    schedule = get_bell_schedule(day)

    # If school is in session, iterate and check through all of the categories
    if schedule["Period 1"].start <= day <= schedule["AIS Tutoring"].end:
        for cat in schedule.items():
            if cat[1].start <= day <= cat[1].end:
                return cat

    return None


def get_next_class(day: dt) -> Optional[Tuple[str, Time]]:
    """Returns information of the next class.

    Returns a tuple of information of the next class, where the first element
    is a string of the category, such as the class period, and a Time
    namedtuple object, which includes when said period starts and ends.

    Args:
        day (datetime.datetime): A datetime object from the datetime library.

    Raises:
        errors.InvalidDate: Thrown if the input is not a datetime object.
        errors.DayNotInData: Thrown if the inputted day is not in
        term_days.csv.

    Returns:
        Optional[Tuple[str, Time]]: A tuple of a string of the category name
        (see data/bell_schedule.csv), and a Time namedtuple object with fields
        'start' and 'end', which returns a datetime object.
    """

    """
    current_class = get_current_class(day)

    # Checks if school is in session and there is a class after the current
    # class (anything before AIS Tutoring)
    if current_class and current_class[0] != "AIS Tutoring":
        schedule_list = list(get_bell_schedule(day).items())

        # Gets the next class in the schedule list, but skip passing periods
        next_class = schedule_list[schedule_list.index(current_class) + 1]
        return next_class if not next_class[0].startswith("Passing") \
            else schedule_list[schedule_list.index(next_class) + 1]

    # Gets the first period datetime for the next school day
    if get_next_school_day(day):
        return list(get_bell_schedule(get_next_school_day(day)).items())[0]

    return None
    """

    return

def get_current_period(time: dt) -> Optional[str]:
    """Returns the current period.

    Returns the current period, where the first element is a string of the
    category, such as the class period, and a Time namedtuple object, which
    includes when said period starts and ends.

    Args:
        time (datetime.datetime): A datetime object from the datetime library.

    Raises:
        errors.InvalidDate: Thrown if the input is not a datetime object.
        errors.DayNotInData: Thrown if the inputted day is not in
        term_days.csv.

    Returns:
        Optional[str]: A string of the category name (see data/bell_schedule.csv)
    """

    raise NotImplementedError
