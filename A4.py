# Считываем два целых числа от 1 до 1000
A = int(input())
B = int(input())

max_value = (A + B + (A - B) * ((A - B) // abs(A - B))) // 2

print(max_value)