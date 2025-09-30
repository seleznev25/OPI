# Вводим координаты первой клетки
x1 = int(input())
y1 = int(input())

# Вводим координаты второй клетки
x2 = int(input())
y2 = int(input())

# Определяем цвет клеток
# Сумма координат четная — белая клетка, нечетная — черная.
def cell_color(x, y):
    if (x + y) % 2 == 0:
        return 'White'
    else:
        return 'Black'

color1 = cell_color(x1, y1)
color2 = cell_color(x2, y2)

if color1 == color2:
    print("YES")
    print(color1)
else:
    print("NO")