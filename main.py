from datetime import datetime, timedelta
def get_birthdays_per_week(users):
    weekdays = {i: [] for i in range(7)}
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    current_datetime = datetime.now()
    current_date = current_datetime.date()
    current_year = current_date.year
    week_interval = timedelta(weeks=1)
    end_of_period = current_date + week_interval

    delta = timedelta(days=1)
    dates = []

    if current_date.weekday() == 0:
            current_date = current_date - timedelta(days=2)

    while current_date <= end_of_period:
        dates.append(current_date.isoformat())
        current_date += delta

    for colleague in users:
        name = colleague.get('name')
        birthday = colleague.get('birthday')
        current_birthday = birthday.replace(year=current_year).date()

        if str(current_birthday) in dates:
            weekday = current_birthday.weekday()
            if weekday in [5, 6]:
                weekday = 0
            weekdays[weekday].append(name)

    for day in days:
        if 0 <= days.index(day) <= 4:
            i = days.index(day)
            print(f'{day}: {", ".join(weekdays.get(i))}')

# LIST OF BIRTHDAYS FOR CHECK
colleagues_birthdays = [
        {'name': 'Alex', 'birthday': datetime(year=2001, month=7, day=29)},
        {'name': 'Natalia','birthday': datetime(year=2000, month=7, day=30)},
        {'name': 'Danylo', 'birthday': datetime(year=1999, month=7, day=31)},
        {'name': 'Vlad', 'birthday': datetime(year=1998, month=8, day=1)},
        {'name': 'Kseniia', 'birthday': datetime(year=1997, month=8, day=3)},
        {'name': 'Yevhen', 'birthday': datetime(year=1996, month=8, day=2)},
        {'name': 'Katya', 'birthday': datetime(year=1995, month=7, day=29)},
        {'name': 'Daryna', 'birthday': datetime(year=1994, month=9, day=30)},
        {'name': 'Sonya', 'birthday': datetime(year=1993, month=7, day=31)},
        {'name': 'Oleh', 'birthday': datetime(year=1992, month=8, day=4)},
       ]


if __name__ == '__main__':
    get_birthdays_per_week(colleagues_birthdays)

