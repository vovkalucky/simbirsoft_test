from datetime import datetime


def current_day() -> int:
    current_date = datetime.now()
    return current_date.day
