#!/usr/bin/env python

"""
Command line interface for weekdayfinder.
"""

import argparse
from weekdayfinder import wkday, info


def parse_command_line():
    "Parses arguments for weekdayfinder functions."

    # Init parser and add arguments.
    parser = argparse.ArgumentParser()

    # Add long arguments.
    parser.add_argument(
        "--today",
        help = "Prints current weekday.",
        action = "store_true"
        )

    parser.add_argument(
        "--tomorrow",
        help = "Prints upcoming weekday.",
        action = "store_true"
        )

    parser.add_argument(
        "--yesterday",
        help = "Prints previous weekday.",
        action = "store_true"
        )

    parser.add_argument(
        "--info",
        help = "Returns info about package.",
        action ="store_true")

    # Parse arguments.
    args = parser.parse_args()

    # Check that only one argument was entered.
    if sum([args.today, args.tomorrow, args.yesterday, args.info]) > 1:
        raise SystemExit(
            "Enter only one argument at a time.")
    return args


def main():
    """
    Run main function on parsed arguments.
    """

    # Get arguments from command line as a dict-like object.
    args = parse_command_line()

    # Pass argument to call weekdayfinder function.
    if args.today:
        wkday("today")
    elif args.tomorrow:
        wkday('tomorrow')
    elif args.yesterday:
        wkday('yesterday')
    elif args.info:
        info()


if __name__ == "__main__":
    wkday("today")
    wkday("tomorrow")
    wkday("yesterday")
    info()
    wkday("potato")