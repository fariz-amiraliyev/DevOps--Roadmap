datetime.date - Represents a simple date according to the Gregorian calendar
datetime.time - Represents a time on a 24-hour clock, independent of a date
datetime.datetime - A combination of date and time
datetime.timedelta - The difference between two date, time, or datetimes in milliseconds

datetime.tzinfo - An abstract class to encompass timezone offset information
datetime.timezone - An implementation of the tzinfo abstract class:
This class provides an easy way to access various important timezones like UTC.


exmple:

 import datetime
 valentines = datetime.date(2020, 2, 14)
 valentines.day
 valentines.weekday()


 >>> edt = datetime.timezone(datetime.timedelta(hours=-4))
>>> quarter_past_twelve = datetime.time(12, 15, 10, tzinfo=edt)
>>> quarter_past_twelve.utcoffset()
datetime.timedelta(days=-1, seconds=72000)
>>> quarter_past_twelve.tzname()
'UTC-04:00'
>>> quarter_past_twelve.hour
12
>>> quarter_past_twelve.minute
15
>>> quarter_past_twelve.isoformat()
'12:15:10-04:00'


>>> birthday = datetime.datetime(2020, 2, 6, 8, 0)
>>> vday_lunch - birthday
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    vday_lunch - birthday
TypeError: can't subtract offset-naive and offset-aware datetimes

>>> birthday = datetime.datetime(2020, 2, 6, 8, 0, tzinfo=edt)
>>> vday_lunch - birthday
datetime.timedelta(days=8, seconds=15310)
