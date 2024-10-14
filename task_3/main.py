from datetime import datetime as dt, timedelta as td


def current_datetime(delta: int) -> str:
    new_date = dt.now() + td(delta)
    formatted_time = new_date.strftime('%Y-%m-%d')

    return formatted_time


if __name__ == '__main__':
    print(current_datetime(35))
