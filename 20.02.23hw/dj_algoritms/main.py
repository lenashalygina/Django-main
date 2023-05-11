# Рекурсия
def is_palindrome_recursive(string1):
    string1 = string1.lower().replace(" ", "").replace(",", "").replace("'", "")
    if len(string1) < 2:
        return True
    if string1[0] != string1[-1]:
        return False
    return is_palindrome_recursive(string1[1:-1])


string1 = "Мадам"
print(is_palindrome_recursive(string1))


# Реверс строки
def is_palindrome_reverse(string2):
    string2 = string2.lower().replace(" ", "").replace(",", "").replace("'", "")
    reversed_string2 = string2[::-1]
    return string2 == reversed_string2


string2 = "Аргентина манит негра"
print(is_palindrome_reverse(string2))


def is_palindrome_pointers(string3):
    string3 = string3.lower().replace(" ", "").replace(",", "").replace("'", "")
    left = 0
    right = len(string3) - 1
    while left < right:
        if string3[left] != string3[right]:
            return False
        left += 1
        right -= 1
    return True


string3 = "No lemon,no melon"
print(is_palindrome_pointers(string3))


#Task 2
def second_algoritm(list1):
    list1.sort()
    start = end = list1[0]
    result = ""
    for i in range(1, len(list1)):
        if list1[i] == end + 1:
            end = list1[i]
        else:
            if start == end:
                result += str(start) + ","
            else:
                result += str(start) + "-" + str(end) + ","
            start = end = list1[i]
    if start == end:
        result += str(start)
    else:
        result += str(start) + "-" + str(end)
    return result


print(second_algoritm([1, 4, 5, 2, 3, 9, 8, 11, 0]))
print(second_algoritm([1, 4, 3, 2]))
print(second_algoritm([1, 4]))