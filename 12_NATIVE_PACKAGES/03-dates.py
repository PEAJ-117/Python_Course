# import time
# print(time.time())
# Output
# Seconds from 01/01/1970
# Date in UTC

# import datetime
from datetime import datetime
# date = datetime.datetime(2026, 6, 1)
date = datetime(2026, 6, 1)
date2 = datetime(2026, 7, 1)

actual = datetime.now()
# print(actual)

dateStr = datetime.strptime("2026-06-22", "%Y-%m-%d")
# print(dateStr)
# print(date.strftime("%Y.%m.%d"))
# print(date > date2)
print(date.year, date.month, date.day, date.hour, date.minute)
