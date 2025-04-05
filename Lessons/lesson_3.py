# def function_name(arguments): - создание функции
# lambda arg: - создание анонимной функции
# return - вернуть результат функции
# *args - любое количество элементов
# * - распаковка
# **kwargs - любое количество именованных элементов
# ** - распаковка с именем

# map(func, list) - применить функцию к каждому элементу списка
# filter(func, list) - отфильтровать элементы списка

# class Name(Parent): - создание класса
# def __init__(self, *args) - инициализация класса

# eval() - вычислить значение выражения


# class Animal:
#     def __init__(self, voice: str):
#         self.voice = voice
#         self.is_sleeping = True
#
#     def speak(self) -> str:
#         return self.voice
#
#     def sleep(self, s: bool):
#         self.is_sleeping = s
#
#
# class Cat(Animal):
#     def __init__(self, voice: str, size: int):
#         super().__init__(voice)
#         self.size = size
#
#     def is_big(self) -> str:
#         if self.size > 5:
#             return 'Big'
#         else:
#             return 'Small'
#


# ДЗ:

# 1. Напишите функцию, которая создаёт прогрессию. Вам будет дан первый член прогрессии, знаменатель прогрессии,
# вид прогрессии, и номер цифры, которую вам надо высчитать.
# progression(1, 3, '+', 4) => 10
# + - алгебраическая прогрессия
# progression(3, 2, '*', 5) => 48
# * - геометрическая прогрессия


# 2. Напишите функцию, которая принимает предложение и определяет, заикается ли человек. Человек заикается,
# если в предложении есть хотя бы одно слово, за которым идёт слово, содержащее в начале первое слово.
# stutter('Я люблю ре решать задачки') => true //ре - решать
# stutter('Мои любимые тны животные - собаки') => false //тны - НЕ начало слова животные


# 3. Создайте класс объекта обыкновенной дроби. Он поддерживает все базовые математические методы (+, -, *, /)
# с другими экземплярами объекта дроби, а также метод, который переводит обыкновенную дробь в десятичную дробь
# Например:
# fraction1 = Fraction(3, 5)
# fraction2 = Fraction(1, 3)
# fraction1.add(fraction2) = '14/15'
# fraction1.substract(fraction2) = '4/15'
# fraction1.multiply(fraction2) = '3/15'
# fraction1.divide(fraction2) = '1 4/5'
# fraction1.to_decimal() = 0.6



# 1. Напишите функцию, которая создаёт прогрессию. Вам будет дан первый член прогрессии, знаменатель прогрессии,
# вид прогрессии, и номер цифры, которую вам надо высчитать.
# progression(1, 3, '+', 4) => 10
# + - алгебраическая прогрессия
# progression(3, 2, '*', 5) => 48
# * - геометрическая прогрессия
from typing import Union

def progression(first_num: Union[int, float], dif: Union[int, float], operation: str, participant: int) -> Union[int, float]:
    for i in range(participant-1):
        first_num = eval(f'{first_num}{operation}{dif}')
    return first_num

# print(progression(1, 3, '+', 4))
# print(progression(3, 2, '*', 5))
# print()


# 2. Напишите функцию, которая принимает предложение и определяет, заикается ли человек. Человек заикается,
# если в предложении есть хотя бы одно слово, за которым идёт слово, содержащее в начале первое слово.
# stutter('Я люблю ре решать задачки') => true //ре - решать
# stutter('Мои любимые тны животные - собаки') => false //тны - НЕ начало слова животные


def stutter(sting: str) -> Union[bool, str]:
    flag = False
    if isinstance(sting, str) and len(sting.replace(' ', '')):
        words_list = sting.split(' ')
        for i in range(1, len(words_list)):
            if words_list[i - 1] == words_list[i][:len(words_list[i - 1])]:
                flag = True
        return flag
    else:
        return 'Empty input'


# print(stutter('Я люблю ре решать задачки'))
# print(stutter('Мои любимые тны животные - собаки'))
# print()



# 3. Создайте класс объекта обыкновенной дроби. Он поддерживает все базовые математические методы (+, -, *, /)
# с другими экземплярами объекта дроби, а также метод, который переводит обыкновенную дробь в десятичную дробь
# Например:
# fraction1 = Fraction(3, 5)
# fraction2 = Fraction(1, 3)
# fraction1.add(fraction2) = '14/15'
# fraction1.substract(fraction2) = '4/15'
# fraction1.multiply(fraction2) = '3/15'
# fraction1.divide(fraction2) = '1 4/5'
# fraction1.to_decimal() = 0.6


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    def __dividers_list(self, num: int, flag: str) -> list:
        locator = num
        while locator > 1:
            dividers = list(range(locator-1, 1, -1)) if flag == 'min' else list(range(2, locator+1))
            res = []
            for div in dividers:
                if locator % div == 0:
                    res.append(div)
                    locator = int(locator / div)
            return res if len(res) else [num]

    def __least_common_multiple(self, num_1: int, num_2: int) -> int:
        min_num, max_num = min(num_1, num_2), max(num_1, num_2)
        res = 1

        operants_for_min = self.__dividers_list(min_num, 'min')
        operants_for_max = self.__dividers_list(max_num, 'max')

        if len(operants_for_min) > 1 and len(operants_for_max) > 1:
            shortest_length = min([len(operants_for_min), len(operants_for_max)])
            all_dividers = operants_for_min[:shortest_length] + operants_for_max[:shortest_length]
            for div in all_dividers:
                res *= div
            return res
        else:
            return num_1 * num_2

    def __greatest_common_divisor(self,numerator: int, denominator: int):
        gcd = 0
        for i in range(2, numerator):
            if numerator % i == 0 and denominator % i ==0:
                gcd = i
        if gcd > 0:
            return int(numerator / gcd), int(denominator / gcd)
        else:
            return numerator, denominator

    def improper_fraction_converter(self, numerator: int, denominator: int) -> str:
        if numerator >= denominator:
            whole_part = numerator//denominator
            numerator, denominator = self.__greatest_common_divisor(numerator - denominator * whole_part, denominator)
            return f"{whole_part} {numerator}/{denominator}"
        else:
            numerator, denominator = self.__greatest_common_divisor(numerator, denominator)
            return f"{numerator}/{denominator}"

    def add(self, fraction) -> str:
        if fraction.denominator == self.denominator:
            numerator = self.numerator + fraction.numerator
            return self.improper_fraction_converter(numerator, self.denominator)
        else:
            lcm = self.__least_common_multiple(self.denominator, fraction.denominator)
            numerator = int((self.numerator * lcm / self.denominator) + (fraction.numerator * lcm / fraction.denominator))
            return self.improper_fraction_converter(numerator, lcm)

    def substract(self, fraction) -> str:
        if fraction.denominator == self.denominator:
            numerator = self.numerator - fraction.numerator
            return self.improper_fraction_converter(numerator, self.denominator)
        else:
            lcm = self.__least_common_multiple(self.denominator, fraction.denominator)
            numerator = int((self.numerator * lcm / self.denominator) - (fraction.numerator * lcm / fraction.denominator))
            return self.improper_fraction_converter(numerator, lcm)

    def multiply(self, fraction) -> str:
        return self.improper_fraction_converter(self.numerator * fraction.numerator,
                                                self.denominator * fraction.denominator)

    def divide(self, fraction) -> str:
        return self.improper_fraction_converter(self.numerator * fraction.denominator,
                                                self.denominator * fraction.numerator)

    def to_decimal(self) -> float:
        return self.numerator / self.denominator


fraction1 = Fraction(3, 5)
fraction2 = Fraction(1, 3)
# fraction1 = Fraction(12, 15)
# fraction2 = Fraction(4, 9)

# print(fraction1.add(fraction2))
# print(fraction1.substract(fraction2))
# print(fraction1.multiply(fraction2))
# print(fraction1.divide(fraction2))
# print(fraction1.to_decimal())


def gena(num):
    for i in range(2,num):
        if easy_numbers(i):
            yield i


def easy_numbers(number):
    for i in range(2, number-1):
        if number % i == 0:
            return False
    return True


a = gena(16)
print(next(a))
print(next(a))
print(next(a))
print(next(a))


a = [10, 14, 100, 5, 0]
b = [-15, -20, 11, 16, -16]


def numbers(lst: list):
    ans = []
    ans.append(f"+{abs(lst[0] - lst[-1])}" if lst[-1] < lst[0] else f"-{abs(lst[0] - lst[-1])}")

    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            ans.append(f'+{abs(lst[i] - lst[i+1])}')
        else:
            ans.append(f'-{abs(lst[i] - lst[i+1])}')

    return ans

#
print(numbers(a))
print(numbers(b))






