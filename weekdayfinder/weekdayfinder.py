#!/usr/bin/env python

"""
A packages that determines the day of the week for the current, upoming and previous day.
"""

import pytz
import calendar
from datetime import datetime, timezone
import pandas as pd

# Load a csv file as a database template.
csv = "https://raw.githubusercontent.com/HenryLandis/hack-program/main/data/timezones.csv"

# Get UTC time.
utc = pytz.utc.localize(datetime.utcnow())

class WeekdayFinder:
    def __init__(self):
        self.data = pd.read_csv(csv)

    def wkday(self, arg, tzinfo = None):
        """
        Returns the current weekday.  If tzinfo is not provided, the default is UTC time.  The tzlist function returns a list of
        commonly used timezones.
        """
        if arg == "today":

            # Use timezone if provided.
            if tzinfo is not None:
                tz = utc.astimezone(pytz.timezone("{}".format(tzinfo)))
                wk = calendar.day_name[tz.weekday()]

            # If no timezone is provided, use UTC time.
            else:
                wk = calendar.day_name[utc.weekday()]

            # Return weekday.    
            print("Today is {}.".format(wk))

        elif arg == "tomorrow":
            if tzinfo is not None:
                tz = utc.astimezone(pytz.timezone("{}".format(tzinfo)))

                # Avoid indexing range errors due to weekday numbering.
                if calendar.day_name[tz.weekday()] == "Sunday":
                    wk = "Monday"
                else:
                    wk = calendar.day_name[tz.weekday() + 1]
            else:
                if calendar.day_name[utc.weekday()] == "Sunday":
                    wk = "Monday"
                else:
                    wk = calendar.day_name[utc.weekday() + 1]
            print("Tomorrow is {}.".format(wk))

        elif arg == "yesterday":
            if tzinfo is not None:
                tz = utc.astimezone(pytz.timezone("{}".format(tzinfo)))
                if calendar.day_name[tz.weekday()] == "Monday":
                    wk = "Sunday"
                else:
                    wk = calendar.day_name[tz.weekday() - 1]
            else:
                if calendar.day_name[utc.weekday()] == "Monday":
                    wk = "Sunday"
                else:
                    wk = calendar.day_name[utc.weekday() - 1]
            print("Yesterday was {}.".format(wk))

        # Raise exception for invalid argument.
        else:
            raise Exception("Invalid argument.")

    def wkday_world(self):
        """
        Determines the day of the week in selected timezones, saves results to dataframe and prints it.
        """
        for idx in self.data.index:
            tz = utc.astimezone(pytz.timezone("{}".format(self.data.loc[idx, "timezone"])))
            self.data.loc[idx, "weekday"] = calendar.day_name[tz.weekday()]
        print(self.data[["timezone", "weekday"]])


def tzlist():
    """
    Returns a list of timezones, which can be used as arguments for tzinfo in the wkday function of the WeekdayFinder class.
    """
    for tz in pytz.all_timezones:
        print(tz)


def info():
    """
    Returns information about the package.
    """
    info = "This package determines the day of the week for the current, previous and upcoming day."
    print(info)


if __name__ == "__main__":
    wkf = WeekdayFinder()
    wkf.wkday("today")
    wkf.wkday("tomorrow")
    wkf.wkday("yesterday")
    wkf.wkday_world()
    info()