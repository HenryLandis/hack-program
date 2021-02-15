# weekdayfinder

`weekdayfinder` determines the day of the week for the current, upcoming and previous day.  You can additionally specify a preferred timezone, get a list of timezones from the [tz database](https://en.wikipedia.org/wiki/Tz_database) (also known as the Olson database), or view a table of current weekdays in selected timezones around the world.


## CLI instructions

```
wkf -h
```

```
usage: wkf [-h] [-a [ARG]] [--tzinfo [TZINFO]] [--tzlist] [-ww] [-p]

optional arguments:
  -h, --help            show this help message and exit
  -a [ARG], --arg [ARG] Find weekday (default is current day).
  --tzinfo [TZINFO]     Specify timezone (default is UTC).
  --tzlist              Show list of timezones.
  -ww, --wkday_world    Show weekdays around the world.
  -p, --package         Returns info about package.
  ```
  
  Valid inputs for ``-a`` are "today", "tomorrow" or "yesterday".
  
  Specifying ``--tzinfo`` without ``-a`` will return a request to provide ``-a.``
  
  Use ``--tzlist`` to view a list of timezone options.
