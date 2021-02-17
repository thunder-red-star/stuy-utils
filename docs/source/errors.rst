======
Errors
======

.. toctree::
   :maxdepth: 2

.. py:class:: StuyException(Exception)
   :module: stuy_utils.errors

   Base exception class for StuyUtils.

.. py:class:: InvalidDate(StuyException)
   :module: stuy_utils.errors

   Thrown if the input is not a date or datetime object.

.. py:class:: DayNotInData(StuyException)
   :module: stuy_utils.errors

   Thrown if the inputted day is not in term_days.csv.
