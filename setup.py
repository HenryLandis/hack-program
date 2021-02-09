#!/usr/bin/env python

"""
Call `pip install -e .` to install package locally for testing.
"""

from setuptools import setup

# Build setup.
setup(
    name="weekdayfinder",
    version="0.0.1",
    author="Henry Landis",
    author_email="hnl2109@columbia.edu",
    description="A packages that determines the day of the week for the current, upcoming and previous day.",
    entry_points={
        "console_scripts": ["wkday = weekdayfinder.__main__:main"]
    },
)