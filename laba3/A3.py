prev = int(input("Введите предыдущее показание: "))
curr = int(input("Введите текущее показание: "))

if curr >= prev:
    used = curr - prev
else:
    used = 10000 - prev + curr

if used == 0:
    print("Газ не использован. Оплата: 0.00, Средняя цена: 0.00")
else:
    if used <= 300:
        cost = 21
    elif used <= 600:
        cost = 21 + (used - 300) * 0.06
    elif used <= 800:
        cost = 21 + 300 * 0.06 + (used - 600) * 0.04
    else:
        cost = 21 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025

    avg_price = cost / used

    print(f"{'Предыдущее':<12}{'Текущее':<10}{'Использовано':<13}{'К оплате':<10}{'Ср. цена m^3'}")
    print(f"{prev:<12}{curr:<10}{used:<13}{round(cost, 2):<10}{round(avg_price, 2)}")
