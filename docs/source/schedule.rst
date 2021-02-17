========
Schedule
========

.. toctree::
   :maxdepth: 2

.. py:function:: convert_to_isoformat(day)
   :module: stuy_utils.schedule

   Convert a date object to an ISO-formatted date string.

   Convert a date or datetime object from the datetime library to a string formatted using the ISO 8601 format, while also checking if 'date' is a valid date and if it exists in the data.

   :param day: A date or datetime object from the datetime library.
   :type day: Union[`datetime.date`, `datetime.datetime`]

   :raises errors.InvalidDate: Thrown if the input is not a date or a datetime object.
   :raises errors.DayNotInData: Thrown if the inputted day is not in term_days.csv.

   :return: A date using the ISO 8601 format (yyyy-mm-dd).
   :rtype: str

.. py:function:: get_day_info(day)
   :module: stuy_utils.schedule

   Returns information about a given day.

   Returns the cycle (A/B), period (1-5/6-10), testing subjects, and any events of a given day. If a category does not apply, an empty string will be returned.

   :param day: A date or datetime object from the datetime library.
   :type day: Union[`datetime.date`, `datetime.datetime`]

   :raises errors.InvalidDate: Thrown if the input is not a date or a datetime object.
   :raises errors.DayNotInData: Thrown if the inputted day is not in term_days.csv.

   :return: A namedtuple with the fields 'cycle', 'period', 'testing' and 'event'.
   :rtype: `Info`

.. py:function:: get_next_school_day(day, force_next, always_same)
   :module: stuy_utils.schedule

   Returns when the next school day is.

   Returns a date object of the next school day from the given day. The given datetime will be returned as a date if school is still in session (can be changed with the 'force_next' parameter).

   :param day: A date or datetime object from the datetime library.
   :type day: Union[`datetime.date`, `datetime.datetime`]

   :param force_next: Whether or not to always return a school day after the given day. Defaults to False.
   :type force_next: bool, optional

   :param always_same: Whether or not to always return the given day if the given day is a school day. Defaults to False.
   :type always_same: bool, optional

   :raises errors.InvalidDate: Thrown if the input is not a date or a datetime object.
   :raises errors.DayNotInData: Thrown if the inputted day is not in term_days.csv.

   :return: A date object with the year, month, and day of the next school day.
   :rtype: `datetime.date`, optional

.. py:function:: get_bell_schedule(day)
   :module: stuy_utils.schedule

   Returns the bell periods of the next school day.

   Returns a dictionary of bell periods of the next school day. If the given day is a school day, then the bell schedule of that day will be returned, even if it is afterschool.

   :param day: A date or datetime object from the datetime library.
   :type day: Union[`datetime.date`, `datetime.datetime`]

   :raises errors.InvalidDate: Thrown if the input is not a date or a datetime object.
   :raises errors.DayNotInData: Thrown if the inputted day is not in term_days.csv.

   :return: A dictionary of keys 'period_1', 'passing_1', 'period_2', 'passing_2', ... 'period_5', 'passing_5', 'office_hours', and 'ais_tutoring', and values of Time namedtuple objects with fields 'start' and 'end', which returns a datetime object.
   :rtype: Dict[str, time]

.. py:function:: get_current_class(day)
   :module: stuy_utils.schedule

   Returns information of the current class.

   Returns a tuple of information of the current class, where the first element is a string of the category, such as the class period, and a `Time` namedtuple object, which includes when said period starts and ends.

   :param day: A datetime object from the datetime library.
   :type day: `datetime.date`

   :raises errors.InvalidDate: Thrown if the input is not a date or a datetime object.
   :raises errors.DayNotInData: Thrown if the inputted day is not in term_days.csv.

   :return: A tuple of a string of either 'period_1', 'passing_1', 'period_2', 'passing_2', ... 'period_5', 'pasing_5', 'office_hours', and 'ais_tutoring', and a `Time` namedtuple object with fields 'start' and 'end', which returns a datetime object.
   :rtype: Tuple[str, time], optional

.. py:function:: get_next_class(day)
   :module: stuy_utils.schedule

   Returns information of the next class.

   Returns a tuple of information of the next class, where the first element is a string of the category, such as the class period, and a `Time` namedtuple object, which includes when said period starts and ends.

   :param day: A datetime object from the datetime library.
   :type day: `datetime.date`

   :raises errors.InvalidDate: Thrown if the input is not a date or a datetime object.
   :raises errors.DayNotInData: Thrown if the inputted day is not in term_days.csv.

   :return: A tuple of a string of either 'period_1', 'passing_1', 'period_2', 'passing_2', ... 'period_5', 'pasing_5', 'office_hours', and 'ais_tutoring', and a `Time` namedtuple object with fields 'start' and 'end', which returns a datetime object.
   :rtype: Tuple[str, time], optional
