print("Введите координаты первой точки:")
x1 = int(input("x1: "))
y1 = int(input("y1: "))

print("Введите координаты второй точки:")
x2 = int(input("x2: "))
y2 = int(input("y2: "))

if x1 > 0 and y1 > 0 and x2 > 0 and y2 > 0:
    print("Yes, I")
elif x1 < 0 and y1 > 0 and x2 < 0 and y2 > 0:
    print("Yes, II")
elif x1 < 0 and y1 < 0 and x2 < 0 and y2 < 0:
    print("Yes, III")
elif x1 > 0 and y1 < 0 and x2 > 0 and y2 < 0:
    print("Yes, IV")
else:
    print("No")

