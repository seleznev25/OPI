password = input("Введите пароль: ")
ok = True

if len(password) != 8:
    print("Ошибка: длина пароля должна быть 8 символов")
    ok = False

if password.lower() == password:
    print("Ошибка: нет заглавных букв")
    ok = False

if password.upper() == password:
    print("Ошибка: нет строчных букв")
    ok = False

if not ("0" in password or "1" in password or "2" in password or "3" in password or
        "4" in password or "5" in password or "6" in password or "7" in password or
        "8" in password or "9" in password):
    print("Ошибка: нет цифр")
    ok = False

if not ("*" in password or "-" in password or "#" in password):
    print("Ошибка: нет специальных символов (* - #)")
    ok = False

for c in password:
    if not (c.isalpha() or c.isdigit() or c in "*-#"):
        print("Ошибка: недопустимый символ:", c)
        ok = False
        break

if ok:
    print("Надёжный пароль")


