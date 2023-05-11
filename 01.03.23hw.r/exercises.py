#task 1
a = int(input("Введите длину стороны a: "))
b = int(input("Введите длину стороны b: "))
c = int(input("Введите длину стороны c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("True")
else:
    print("False")

#task 2
a = int(input("Введите число: "))

if a % 2 == 0:
    print("True")
else:
    print("False")

#task 3
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

if a + b > c:
    print("True")
else:
    print("False")

#task 4
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

if a > b:
    print("True")
else:
    print("False")

#dz05,task 1
login = input("Введите логин: ")
password = input("Введите пароль: ")

if login == "user" and password == "qwerty":
    print("Authentication completed")
else:
    print("Invalid login or password")

# task 2
print("Курсы валют: USD – 420, EUR – 510, RUB - 5.8")

tenge = float(input("Введите сумму в тенге: "))

currency_code = input("Введите код валюты для обмена (USD/EUR/RUB): ")

if currency_code == "USD":
    converted = tenge / 420
    print(f"Вы получите {converted:.2f} долларов США")
elif currency_code == "EUR":
    converted = tenge / 510
    print(f"Вы получите {converted:.2f} евро")
elif currency_code == "RUB":
    converted = tenge / 5.8
    print(f"Вы получите {converted:.2f} российских рублей")
else:
    print("Неправильный код валюты, попробуйте еще раз")
