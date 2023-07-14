#16.1
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Введите число n: "))
result = fibonacci(n)
print(f"n-е число Фибоначчи: {result}")


#16.2
def is_power_of_two(number):
    if number <= 0:
        return False
    else:
        return (number & (number - 1)) == 0

number = int(input("Введите число: "))
result = is_power_of_two(number)
print(result)



#17.1
import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Функции тригонометрических операций
trig_functions = {
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'asin': math.asin,
    'acos': math.acos,
    'atan': math.atan
}

print("Добро пожаловать в инженерный калькулятор!")

while True:
    print("\nВыберите операцию:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Возведение в степень (^)")
    print("6. Факториал (!)")
    print("7. Числа Фибоначчи (fib)")
    print("8. Тригонометрические функции (sin, cos, tan, asin, acos, atan)")
    print("9. Выход")

    choice = input("Введите номер операции: ")

    if choice == '1':
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = num1 + num2
        print("Результат: ", result)
    elif choice == '2':
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = num1 - num2
        print("Результат: ", result)
    elif choice == '3':
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = num1 * num2
        print("Результат: ", result)
    elif choice == '4':
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = num1 / num2
        print("Результат: ", result)
    elif choice == '5':
        num1 = float(input("Введите число: "))
        num2 = float(input("Введите степень: "))
        result = num1 ** num2
        print("Результат: ", result)
    elif choice == '6':
        num = int(input("Введите число для вычисления факториала: "))
        result = factorial(num)
        print("Результат: ", result)
    elif choice == '7':
        num = int(input("Введите номер числа Фибоначчи: "))
        result = fibonacci(num)
        print("Результат: ", result)
    elif choice == '8':
        func = input("Введите тригонометрическую функцию (sin, cos, tan, asin, acos, atan): ")
        num = float(input("Введите число: "))
        if func in trig_functions:
            result = trig_functions[func](num)
            print("Результат: ", result)
        else:
            print("Неверная функция!")
    elif choice == '9':
        print("До свидания!")
        break
    else:
        print("Неверный выбор операции!")



#17.2
def draw_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def make_move(board, player):
    while True:
        row = int(input("Введите номер строки (0-2): "))
        col = int(input("Введите номер столбца (0-2): "))
        if board[row][col] == " ":
            board[row][col] = player
            break
        else:
            print("Эта клетка уже занята!")

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]

    players = ["X", "O"]
    current_player = 0

    while True:
        draw_board(board)

        print(f"Ход игрока {players[current_player]}")
        make_move(board, players[current_player])

        if check_win(board, players[current_player]):
            draw_board(board)
            print(f"Игрок {players[current_player]} победил!")
            break

        if all(board[row][col] != " " for row in range(3) for col in range(3)):
            draw_board(board)
            print("Ничья!")
            break

        current_player = (current_player + 1) % 2

tic_tac_toe()
