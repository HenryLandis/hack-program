# weekdayfinder

`weekdayfinder` determines the day of the week for the current, upcoming and previous day.


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
  
  Specifying ``--tzinfo`` without an input for ``-a`` will return a request to provide this input.
