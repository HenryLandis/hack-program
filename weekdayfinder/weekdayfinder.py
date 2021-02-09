#!/usr/bin/env python

"""
A packages that determines the day of the week for the current, upoming and previous day.
"""

from datetime import date
import calendar

# Set the first day of the week as Sunday, following the American convention.
calendar.setfirstweekday(calendar.SUNDAY)

def wkday(arg):
    """
    Returns the current weekday.
    """
    if arg == "today":
        wk = calendar.day_name[date.today().weekday()]
        print("Today is " + wk + ".")
    elif arg == "tomorrow":
        wk = calendar.day_name[date.today().weekday() + 1]
        print("Tomorrow is " + wk + ".")
    elif arg == "yesterday":
        wk = calendar.day_name[date.today().weekday() - 1]
        print("Yesterday was " + wk + ".")

    # Raise exception for invalid argument.
    else:
        raise Exception("Invalid argument.")


def info():
    """
    Returns information about the package.
    """
    info = "This package determines the day of the week for the current, previous and upcoming day."
    print(info)


if __name__ == "__main__":
    wkday("today")
    wkday("tomorrow")
    wkday("yesterday")
    info()
    wkday("potato")
