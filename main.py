from datetime import datetime, timedelta
def get_birthdays_per_week(users):
    monday_birthdays = []
    tuesday_birthdays = []
    wednesday_birthdays = []
    thursday_birthdays = []
    friday_birthdays = []

    current_datetime = datetime.now()
    current_date = current_datetime.date()
    current_year = current_date.year
    week_interval = timedelta(weeks=1)
    end_of_period = current_date + week_interval

    delta = timedelta(days=1)
    dates = []
    week_birthdays = []

    while current_date <= end_of_period:
        dates.append(current_date.isoformat())
        current_date += delta

    for colleague in users:
        name = colleague.get('name')
        birthday = colleague.get('birthday')
        current_birthday = birthday.replace(year=current_year).date()
        current_birthday_weekday = current_birthday.weekday()

        if str(current_birthday) in dates:
            week_birthdays.append(current_birthday)

            if current_birthday_weekday==1:
                tuesday_birthdays.append(name)
            elif current_birthday_weekday==2:
                wednesday_birthdays.append(name)
            elif current_birthday_weekday==3:
                thursday_birthdays.append(name)
            elif current_birthday_weekday==4:
                friday_birthdays.append(name)
            else:
                monday_birthdays.append(name)

    monday_birthdays_str = ', '.join(monday_birthdays)
    tuesday_birthdays_str = ', '.join(tuesday_birthdays)
    wednesday_birthdays_str = ', '.join(wednesday_birthdays)
    thursday_birthdays = ', '.join(thursday_birthdays)
    friday_birthdays = ', '.join(friday_birthdays)

    print(f'Do not forget to congratulate your colleagues:\nHave birthdays on Monday: {monday_birthdays_str}.'
          f'\nHave birthdays on Tuesday: {tuesday_birthdays_str}'
          f'\nHave birthdays on Wednesday: {wednesday_birthdays_str}'
          f'\nHave birthdays on Thursday: {thursday_birthdays}'
          f'\nHave birthdays on Friday: {friday_birthdays}')

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

