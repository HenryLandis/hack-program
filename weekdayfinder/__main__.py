#!/usr/bin/env python

"""
Command line interface for weekdayfinder.
"""

import argparse
from weekdayfinder import WeekdayFinder, tzlist, info


def parse_command_line():
    "Parses arguments for weekdayfinder functions."

    # Init parser and add arguments.
    parser = argparse.ArgumentParser()

    # Add long arguments.
    parser.add_argument(
        "-a", "--arg",
        help = "Find weekday (default is current day).",
        nargs = "?",
        const = "today"
    )

    # "nargs" sets up flexible param entry, with "today" as the default.
    parser.add_argument(
        "--tzinfo",
        help = "Specify timezone (default is UTC).",
        nargs = "?",
        const = None
    )

    parser.add_argument(
        "--tzlist",
        help = "Show list of timezones.",
        action = "store_true"
    )

    parser.add_argument(
        "-ww", "--wkday_world",
        help = "Show weekdays around the world.",
        action = "store_true"
    )

    parser.add_argument(
        "-p", "--package",
        help = "Returns info about package.",
        action = "store_true")

    # Parse arguments.
    args = parser.parse_args()
    return args


def main():
    """
    Run main function on parsed arguments.
    """

    # Get arguments from command line as a dict-like object.
    args = parse_command_line()

    # An instance of the class object must be initialized (as opposed to calling the class directly).
    wkf = WeekdayFinder()

    # Pass arguments to call functions.
    if args.arg:
        if args.tzinfo is not None:
            if args.arg == "today":
                wkf.wkday("today", tzinfo = args.tzinfo)
            elif args.arg == "tomorrow":
                wkf.wkday("tomorrow", tzinfo = args.tzinfo)
            elif args.arg == "yesterday":
                wkf.wkday("yesterday", tzinfo = args.tzinfo)
            else:
                print("Invalid argument.")
        else:
            if args.arg == "today":
                wkf.wkday("today")
            elif args.arg == "tomorrow":
                wkf.wkday("tomorrow")
            elif args.arg == "yesterday":
                wkf.wkday("yesterday")
            else:
                print("Invalid argument.")

    if args.tzinfo and not args.arg:
        print("Please specify a day to find for this timezone.")

    if args.wkday_world:
        wkf.wkday_world()

    if args.tzlist:
        tzlist()
    
    if args.package:
        info()


if __name__ == "__main__":
    wkf = WeekdayFinder()
    wkf.wkday("today")
    wkf.wkday("tomorrow")
    wkf.wkday("yesterday")
    wkf.wkday_world()
    info()