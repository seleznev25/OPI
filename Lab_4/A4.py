def luhn_check(card_number):
    # Удаляем пробелы и проверяем, что номер состоит только из цифр
    card_number = card_number.replace(" ", "")
    if not card_number.isdigit():
        return False

    total = 0
    reverse_digits = card_number[::-1]

    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        # Удваиваем каждую вторую цифру, начиная с индекса 1
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n

    return total % 10 == 0

# Пример использования
card = input("Введите номер кредитной карты: ")
if luhn_check(card):
    print("Номер карты валиден.")
else:
    print("Номер карты НЕ валиден.")
