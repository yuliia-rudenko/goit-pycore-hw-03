import re

def normalize_phone(phone_number):
    """
    Нормалізує телефонний номер до формату +38XXXXXXXXXX.

    :param phone_number: рядок з номером у будь-якому форматі
    :return: нормалізований номер у форматі +38XXXXXXXXXX
    """
    # Видаляємо всі символи, крім цифр
    phone = re.sub(r"[^\d+]", "", phone_number)

    if phone.startswith("+"):
        pass  # вже має + на початку, нічого не робимо
    elif phone.startswith("380"):
        phone = "+" + phone  # є код без +, просто додаємо +
    else:
        phone = "+38" + phone  # немає коду зовсім, додаємо +38
    return phone

# Тест
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери:", sanitized_numbers)
