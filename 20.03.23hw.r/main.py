#19.1
def calculate_minimum_payment(prices):
    prices.sort(reverse=True)
    total_payment = 0
    for i in range(2, len(prices), 3):
        total_payment += prices[i]

    return total_payment


N = int(input("Введите количество товаров: "))
prices = []
for i in range(N):
    price = int(input(f"Введите стоимость товара {i + 1}: "))
    prices.append(price)

minimum_payment = calculate_minimum_payment(prices)
print(f"Минимальная сумма денег: {minimum_payment}")


#19.2
def find_closest_numbers(numbers):
    numbers.sort()
    min_difference = float('inf')
    closest_pair = []

    for i in range(len(numbers) - 1):
        difference = numbers[i + 1] - numbers[i]
        if difference < min_difference:
            min_difference = difference
            closest_pair = [numbers[i], numbers[i + 1]]

    return closest_pair



#20.1
def align_and_count_characters(strings):
    max_length = max(len(string) for string in strings)
    aligned_strings = [f"{'*' * (max_length - len(string))}{string}" for string in strings]
    return max_length, aligned_strings

M = int(input("Введите количество строк: "))
strings = []
for i in range(M):
    string = input(f"Введите строку {i + 1}: ")
    strings.append(string)

max_length, aligned_strings = align_and_count_characters(strings)
print(f"Количество символов в самой длинной строке: {max_length}")

print("Выровненные строки:")
for string in aligned_strings:
    print(string)


#20.2
def add_balance_element(arr):
    positive_sum = sum([num for num in arr if num > 0])
    negative_sum = sum([num for num in arr if num < 0])
    difference = abs(positive_sum) - abs(negative_sum)
    arr.append(difference)
    return arr

N = int(input("Введите количество элементов: "))
arr = []
for i in range(N):
    num = int(input(f"Введите элемент {i + 1}: "))
    arr.append(num)

result = add_balance_element(arr)
print("Результат:", result)

