from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Розраховує кількість днів між заданою датою і поточною датою.
    
    :param date: рядок дати у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09')
    :return: ціле число — кількість днів від заданої дати до сьогодні
             (від'ємне, якщо дата в майбутньому)
    """
    try:
        # Крок 1: перетворюємо рядок у об'єкт datetime
        given_date = datetime.strptime(date, "%Y-%m-%d").date()

        # Крок 2: отримуємо поточну дату (без часу)
        today = datetime.today().date()

        # Крок 3: обчислюємо різницю в днях
        delta =  today - given_date

        # Крок 4: повертаємо кількість днів як ціле число
        return (delta.days)
    
    except ValueError:
        print(f"Помилка: невірний формат дати '{date}'")
        return None
# Тест
print(get_days_from_today("2021-10-09"))
print(get_days_from_today("2030-01-01"))
print(get_days_from_today("abc-abc"))
