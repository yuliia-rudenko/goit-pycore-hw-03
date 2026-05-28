import random

def get_numbers_ticket(min, max, quantity):
    """
    Генерує набір унікальних випадкових чисел для лотереї.

    :param min: мінімальне число (не менше 1)
    :param max: максимальне число (не більше 1000)
    :param quantity: кількість чисел (між min і max)
    :return: відсортований список унікальних чисел або []
    """
    if min < 1 or max > 1000 or quantity < 1:
        return []
    if quantity > (max - min + 1):
        return []
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)
# Тест
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

print(get_numbers_ticket(0, 49, 6))   # [] бо min < 1
print(get_numbers_ticket(1, 49, 50))  # [] бо quantity > діапазону
