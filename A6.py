# Ввод количества секунд с клавиатуры
N = int(input())

# Вычисление часов, минут и секунд
hours = N // 3600
remaining_seconds = N % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{hours}:{format(minutes, '02')}:{format(seconds, '02')}")