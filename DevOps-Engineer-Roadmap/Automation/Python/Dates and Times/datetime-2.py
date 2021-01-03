>>> from datetime import datetime, date, time
>>> valentines_lunch = datetime(2020, 2, 14, 12, 14, 10)
>>> valentines_lunch.strftime("%B %d, %Y @ %I:%M %p")
'February 14, 2020 @ 12:14 PM'


>>> right_now = datetime.now().isoformat()
>>> right_now
'2020-05-01T14:29:29.211322'
>>> now_as_dt = datetime.strptime(right_now, "%Y-%m-%dT%H:%M:%S.%f")
>>> now_as_dt.isoformat()
'2020-05-01T14:29:29.211322'
>>> now_as_dt.isoformat() == right_now
True

>>> valentines_lunch.isoformat()
'2020-02-14T12:14:10'
