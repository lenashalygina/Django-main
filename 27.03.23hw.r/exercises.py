# 21.1
# def caesar_cipher(shift, text):
#     cipher_text = ''
#     for char in text:
#         if char == ' ':
#             cipher_text += ' '
#         else:
#             shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
#             cipher_text += shifted_char
#     return cipher_text
#
#
# shift = int(input('Введите сдвиг шифрования: '))
# text = input('Введите текст для шифрования: ')
#
# ciphered_text = caesar_cipher(shift, text)
# print('Зашифрованный текст:', ciphered_text)


# 21.2
# fruits = ('apple', 'grape', 'kiwi', 'orange', 'pear', 'apple', 'kiwi')
#
# fruit_name = input('Введите название фрукта: ')
#
# fruit_count = fruits.count(fruit_name)
#
# print('Количество раз, которое фрукт "{}" встречается в кортеже: {}'.format(fruit_name, fruit_count))


# 21.4
# car_brands = ('Toyota', 'Ford', 'Porsche', 'Nissan', 'Chevrolet', 'Maybach', 'Tesla', 'Toyota')
#
# old_brand = input('Введите название производителя, который нужно заменить: ')
# new_brand = input('Введите слово для замены: ')
#
# new_car_brands = tuple([new_brand if brand == old_brand else brand for brand in car_brands])
#
# print('Исходный кортеж:', car_brands)
# print('Кортеж после замены:', new_car_brands)


# 22.1
# def superset(A, B):
#     if A == B:
#         print("Множества равны")
#     elif A.issuperset(B):
#         print(f"Объект {A} является чистым супермножеством")
#     elif B.issuperset(A):
#         print(f"Объект {B} является чистым супермножеством")
#     else:
#         print("Супермножество не обнаружено")


# 22.2
# dictionary = {}
#
#
# def add_word():
#     eng_word = input("Введите слово на английском языке: ")
#     fr_word = input("Введите перевод на французский язык: ")
#     dictionary[eng_word] = fr_word
#     print(f"Слово '{eng_word}' добавлено в словарь")
#
#
# def delete_word():
#     eng_word = input("Введите слово на английском языке для удаления: ")
#     if eng_word in dictionary:
#         del dictionary[eng_word]
#         print(f"Слово '{eng_word}' удалено из словаря")
#     else:
#         print(f"Слово '{eng_word}' не найдено в словаре")
#
#
# def search_word():
#     eng_word = input("Введите слово на английском языке для поиска: ")
#     if eng_word in dictionary:
#         print(f"Перевод слова '{eng_word}' на французский язык: {dictionary[eng_word]}")
#     else:
#         print(f"Слово '{eng_word}' не найдено в словаре")
#
#
# def update_word():
#     eng_word = input("Введите слово на английском языке для замены: ")
#     if eng_word in dictionary:
#         fr_word = input("Введите новый перевод на французский язык: ")
#         dictionary[eng_word] = fr_word
#         print(f"Перевод слова '{eng_word}' обновлен")
#     else:
#         print(f"Слово '{eng_word}' не найдено в словаре")
#
#
# def display_menu():
#     print("""
#     Меню:
#     1. Добавить слово в словарь
#     2. Удалить слово из словаря
#     3. Найти слово в словаре
#     4. Заменить перевод слова в словаре
#     5. Выйти из программы
#     """)
#
#
# def main():
#     while True:
#         display_menu()
#         choice = input("Введите номер операции, которую хотите выполнить: ")
#         if choice == "1":
#             add_word()
#         elif choice == "2":
#             delete_word()
#         elif choice == "3":
#             search_word()
#         elif choice == "4":
#             update_word()
#         elif choice == "5":
#             print("Выход из программы")
#             break
#         else:
#             print("Некорректный ввод, попробуйте еще раз")
#
#
# if __name__ == "__main__":
#     main()


#22.3
# def set_gen(nums):
#     num_set = set()
#     for num in nums:
#         count = nums.count(num)
#         if count == 1:
#             num_set.add(num)
#         else:
#             num_set.add(str(num) * count)
#     return num_set


#23.1
# def biggest_dict(**kwargs):
#     my_dict = {'first_one': 'we can do it'}
#     my_dict.update(kwargs)
#     return my_dict
#
# #Пример использования
# result = biggest_dict(k1=22, k2=31, k3=11, k4=91, name='Елена', age=31, weight=61, eyes_color='grey')
# print(result)


#23.2
# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#
# first_key, first_val = my_dict.popitem(last=False)
# last_key, last_val = my_dict.popitem()
#
# my_dict.update({last_key: last_val, first_key: first_val})
#
# del my_dict['b']
#
# my_dict.update({'new_key': 'new_value'})
#
# print(my_dict)



