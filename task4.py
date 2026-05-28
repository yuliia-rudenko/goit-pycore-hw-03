from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    """
    Визначає колег, яких треба привітати з ДН протягом 7 днів.

    :param users: список словників з ключами name та birthday
    :return: список словників з name та congratulation_date
    """
    today = datetime.today().date()
    upcoming = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta = (birthday_this_year - today).days
        if 0 <= delta < 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming


# Тест
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Alex Born", "birthday": "1992.05.28"},
    {"name": "Saturday Person", "birthday": "1995.05.31"},
    {"name": "Sunday Person", "birthday": "2000.06.01"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)