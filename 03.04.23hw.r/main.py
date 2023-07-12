#34
class Roman:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def __add__(self, other):
        if isinstance(other, Roman):
            result = self._roman_to_decimal(self.value) + self._roman_to_decimal(other.value)
            return self._decimal_to_roman(result)
        elif isinstance(other, int):
            result = self._roman_to_decimal(self.value) + other
            return self._decimal_to_roman(result)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Roman):
            result = self._roman_to_decimal(self.value) - self._roman_to_decimal(other.value)
            return self._decimal_to_roman(result)
        elif isinstance(other, int):
            result = self._roman_to_decimal(self.value) - other
            return self._decimal_to_roman(result)
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, Roman):
            result = self._roman_to_decimal(self.value) * self._roman_to_decimal(other.value)
            return self._decimal_to_roman(result)
        elif isinstance(other, int):
            result = self._roman_to_decimal(self.value) * other
            return self._decimal_to_roman(result)
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other):
        if isinstance(other, Roman):
            result = self._roman_to_decimal(self.value) / self._roman_to_decimal(other.value)
            return self._decimal_to_roman(result)
        elif isinstance(other, int):
            result = self._roman_to_decimal(self.value) / other
            return self._decimal_to_roman(result)
        else:
            raise TypeError("Unsupported operand type for /")

    @staticmethod
    def _roman_to_decimal(roman):
        pass

    @staticmethod
    def _decimal_to_roman(decimal):
        pass


#35
def plus_two(number):
    try:
        result = 2 + number
        print(f"Результат сложения: {result}")
    except TypeError:
        print("Ожидаемый тип данных - число!")


number = input("Введите число: ")
try:
    number = int(number)
    plus_two(number)
except ValueError:
    print("Введено некорректное значение числа!")


#36
def access_array_element(array, index):
    try:
        value = array[index]
        print(f"Значение элемента с индексом {index}: {value}")
    except IndexError:
        print("Индекс выходит за границы массива!")

array = [1, 2, 3, 4, 5]
index = int(input("Введите индекс элемента: "))
access_array_element(array, index)
