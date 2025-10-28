def analyze_packets():
    packets = input("Введите строку из 0 и 1 (не менее 5 символов): ")
    if len(packets) < 5 or not all(c in '01' for c in packets):
        print("Ошибка: строка должна содержать только 0 и 1 и быть длиной не менее 5 символов.")
        return

    total = len(packets)
    lost = packets.count('0')
    max_loss_streak = max(map(len, packets.split('1')))
    loss_percent = lost / total * 100

    if loss_percent <= 1:
        quality = "отличное"
    elif loss_percent <= 5:
        quality = "хорошее"
    elif loss_percent <= 10:
        quality = "удовлетворительное"
    elif loss_percent <= 20:
        quality = "плохое"
    else:
        quality = "критическое состояние сети"

    print(f"Общее количество пакетов: {total}")
    print(f"Количество потерянных пакетов: {lost}")
    print(f"Длина самой длинной последовательности потерянных пакетов: {max_loss_streak}")
    print(f"Процент потерь: {loss_percent:.1f}%")
    print(f"Качество связи: {quality}")

analyze_packets()
