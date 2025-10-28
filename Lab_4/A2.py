def draw_rectangle(rows, columns, ch):
    for _ in range(rows):
        print(ch * columns)

def draw_right_triangle(n, ch):
    for i in range(1, n + 1):
        print(ch * i)

def draw_frame(rows, columns, ch):
    print(ch * columns)
    for _ in range(rows - 2):
        print(ch + ' ' * (columns - 2) + ch)
    print(ch * columns)

# Пример использования:
n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
symbol = input("Введите символ для отрисовки: ")

print("\nПрямоугольник:")
draw_rectangle(n, m, symbol)

print("\nПравильный треугольник:")
draw_right_triangle(n, symbol)

print("\nРамка:")
draw_frame(n, m, symbol)
