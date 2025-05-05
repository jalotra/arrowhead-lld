import datetime
from repository.impl.configuration import Time



# finds the day given a date
def get_day(date: Time) -> str:
    return datetime.datetime.strptime(
        f"{date.date} {date.hour}:{date.minute}:{date.second}", "%Y-%m-%d %H:%M:%S"
    ).strftime("%A")
