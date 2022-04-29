"""Sample code to test schedule.py."""
from datetime import datetime as dt
from datetime import timedelta as td

from colorama import Fore, Style, init
from stuy_utils import schedule

init()

day = dt.now()

day_info = schedule.get_day_info(day)

current_class = schedule.get_current_class(day)
next_class = schedule.get_next_class(day)

today_bell_schedule = schedule.get_bell_schedule(day)

def format_td(td_: td) -> str:
    """Converts a timedelta object to a formatted string.
    Args:
        td_ (datetime.timedelta): A timedelta object from the datetime library.
    Returns:
        str: A parsed, formatted string.
    """
    days = td_.days
    hrs = td_.seconds // 3600
    mins = (td_.seconds % 3600) // 60
    secs = td_.seconds % 60

    days = "1 day" if days == 1 else f"{days} days"
    hrs = "1 hour" if hrs == 1 else f"{hrs} hours"
    mins = "1 minute" if mins == 1 else f"{mins} minutes"
    secs = "1 second" if secs == 1 else f"{secs} seconds"

    if days != "0 days":
        return f"{days}, {hrs}, {mins}, and {secs}!"
    if hrs != "0 hours":
        return f"{hrs}, {mins}, and {secs}!"
    if mins != "0 minutes":
        return f"{mins} and {secs}!"
    return f"{secs}!"


def cprint(text: str, *colors):
    """Prints a string with colors/styles from colorama.
    Args:
        text (str): A string to print with colors.
    """
    print("".join(colors) + text + Style.RESET_ALL)


print("==========")
print(f"Inputted Datetime: {day}\n")

print(day.strftime("Today is %A, %B %d, %Y!\n"))

print(f"School: {day_info.school}")
print(f"Cycle: {day_info.cycle if day_info.cycle else None}")
print(f"Schedule: {day_info.schedule}")
print(f"Testing Day: {day_info.testing if day_info.testing else None}")
print(f"Event(s): {day_info.event if day_info.events else None}\n")

if current_class:
    print(f"Current Class: {current_class[0]}")
    print(f"Current Class Start: {current_class[1][0]}")
    print(f"Current Class End: {current_class[1][1]}")

if next_class:
    print(f"Next Class: {next_class[0]}")
    print(f"Next Class Start: {next_class[1][0]}")
    print(f"Next Class End: {next_class[1][1]}")

print("==========")