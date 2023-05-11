#task 1
user_input = input("Введите строку с двумя словами, разделенными пробелом: ")
words = user_input.split()
if len(words) != 2:
    print("Ошибка: введите строку с двумя словами, разделенными пробелом")
else:
    new_string = words[1] + " " + words[0]

    print("Новая строка:", new_string)

#task 2
user_input = input("Введите строку с словами, разделенными пробелами: ")
num_words = user_input.count(' ') + 1
print("Количество слов в строке:", num_words)

#task 3
user_input = input("Введите строку с номером старого года: ")
new_string = user_input.replace("2020", "2023")
print("Новая строка:", new_string)

#dz13,task 1
numbers = []
while sum(numbers) != 0:
    num = int(input("Введите число: "))
    numbers.append(num)

square_sum = sum([num**2 for num in numbers])

print("Сумма квадратов введенных чисел:", square_sum)
numbers = []
while sum(numbers) != 0:
    num = int(input("Введите число: "))
    numbers.append(num)

square_sum = sum([num**2 for num in numbers])
print("Сумма квадратов введенных чисел:", square_sum)

