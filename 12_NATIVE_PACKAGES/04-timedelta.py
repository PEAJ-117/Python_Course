from datetime import datetime, timedelta

date = datetime(2026, 6, 22) + timedelta(weeks=2)
date2 = datetime(2026, 7, 22)

delta = date2 - date
# print(delta)
print(
    delta.days, "Dias\n",
    delta.seconds, "Segundos\n",
    delta.microseconds, "Microsegundos\n",
    delta.total_seconds(), "Segundos totales"
)
