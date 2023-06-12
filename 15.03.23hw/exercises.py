# 14.1
# numbers = input("Введите список цифр через пробел: ").split()
#
# count_5 = numbers.count('5')
# count_4 = numbers.count('4')
# count_3 = numbers.count('3')
# count_2 = numbers.count('2')
#
# print(count_5, count_4, count_3, count_2)
#
# total_points = len(numbers)
# vasya_average = (count_5 * 5 + count_4 * 4 + count_3 * 3 + count_2 * 2) / total_points
#
# print(vasya_average)


# 14.2
# grades_input = input("Введите список оценок через пробел: ")
#
# grades_list = grades_input.split()
#
# for i in range(len(grades_list)):
#     if grades_list[i] == '2':
#         grades_list[i] = '3'
#
# grades_output = ' '.join(grades_list)
# print(grades_output)


# 15.1
# n = int(input("Введите длину списка: "))
# numbers = []
# for i in range(n):
#     num = int(input(f"Введите число {i + 1}: "))
#     numbers.append(num)
#
# odd_count = 0
# even_count = 0
# for num in numbers:
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
#
# if odd_count > even_count:
#     print("Нет")
# else:
#     print("Да")


# 15.2
# def create_nested_list():
#     nested_list = []
#     for _ in range(3):
#         row = []
#         for _ in range(3):
#             num = int(input("Введите число: "))
#             row.append(num)
#         nested_list.append(row)
#     return nested_list
#
#
# def calculate_diagonal_sum(nested_list):
#     diagonal_sum = 0
#     for i in range(3):
#         diagonal_sum += nested_list[i][i]
#     return diagonal_sum
#
#
# my_list = create_nested_list()
#
# diagonal_sum = calculate_diagonal_sum(my_list)
#
# print("Сумма элементов главной диагонали:", diagonal_sum)



