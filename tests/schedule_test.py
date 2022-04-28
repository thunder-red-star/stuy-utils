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


def format_td(td_: td) -> str:
    """Converts a timedelta object to a formatted string.
    Args:
        td_ (datetime.timedelta): A timedelta object from the datetime library.
    Returns:
        str: A parsed, formatted string.
    """

    # MS moment
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

print(f"Cycle: {day_info.cycle if day_info.cycle else None}")
print(f"Periods: {day_info.period if day_info.period else None}")
print(f"Testing Day: {day_info.testing if day_info.testing else None}")
print(f"Event(s): {day_info.event if day_info.event else None}\n")

if current_class:
    cprint("School is in session!", Fore.GREEN, Style.BRIGHT)

    current_period = current_class[0]

    if current_period.startswith("Passing"):
        current_period = "Passing"
    elif day_info.period == "6-10" and current_period.startswith("Period"):
        current_period = f"Period {int(current_period[-1]) + 5}"

    cprint(f"Current Period: {current_period}", Fore.BLUE)
    cprint(f"Over In: {format_td(current_class[1].end - day)}", Fore.YELLOW)
else:
    cprint("School is not in session!", Fore.RED)

if next_class:
    next_period = next_class[0]

    if day_info.period == "6-10" and next_period.startswith("Period"):
        next_period = f"Period {int(next_period[-1]) + 5}"

    if dt(day.year, day.month, day.day, 16, 30) < day < next_class[1].start:
        next_period = "Period 1" if next_period == "Period 6" else "Period 6"

    print(f"{next_period} will start in: "
          f"{format_td(next_class[1].start - day)}")
print("==========")