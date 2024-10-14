from datetime import datetime as dt


def current_datetime():

    curr_time = dt.now()
    week_number = curr_time.isocalendar()[1]
    formatted_time = curr_time.strftime('%Y-%m-%d %H:%M:%S\nДень недели - %A\nНомер недели - ') + str(week_number)

    return formatted_time


if __name__ == '__main__':
    print(current_datetime())
