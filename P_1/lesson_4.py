# import module_name - импортировать модуль
# from module_name import func - импортировать функцию из модуля

# yield - создание генераторов
# next(gen) или gen.__next__() - вывод значения

# @decorator
# def func():
# использование декораторов

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#     return wrapper
# создание декоратора

# def bye_world(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         result = result.split()
#         result[0] = 'Bye'
#         return ' '.join(result)
#     return wrapper


# get from version control - скопировать проект с github


# ДЗ:
# Возьмите функцию, код которой скинул Андрей.
# Представим, что нам понадобилось изменить эту функцию, чтобы она возвращала int, а не str. Напишите декоратор,
# который будет менять тип данных результата данной функции на int


# Напишите функцию, которая принимает три числа. Третье число – результат какой-то операции над первыми двумя числами
# (+, -, *, /). Выведите, какая это была операция.
# get_operation(2, 5, 7) => '+'
# get_operation(11.1, 8, 88.8) => '*'
# Иногда пользователь может не понять, что передавать в функцию, и передать совсем другие вещи. Числа,
# которые друг с другом вообще не связаны, строки, списки.
# Для этого добавьте в функцию отлова базовых ошибок с различными сообщениями и предупреждениями.


# Напишите декоратор, который будет выводить имя запускаемой функции. Это задачка на самостоятельный поиск информации!
# Есть несколько разных способов это сделать, попытайтесь найти один из них.
# Не стесняйтесь гуглить и искать любую доступную информацию.



# Представим, что нам понадобилось изменить эту функцию, чтобы она возвращала int, а не str. Напишите декоратор,
# который будет менять тип данных результата данной функции на int



def change_type(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        int_res = [int(i) for i in res]
        return int_res
    return wrapper

@change_type
def numbers(lst: list):
    ans = []
    ans.append(f"+{abs(lst[0] - lst[-1])}" if lst[-1] < lst[0] else f"-{abs(lst[0] - lst[-1])}")
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            ans.append(f'+{abs(lst[i] - lst[i+1])}')
        else:
            ans.append(f'-{abs(lst[i] - lst[i+1])}')
    return ans


a = [10,14,80,100,5]
b = [-7,15,3,28,31]
print(numbers(a))
print(numbers(b))


# Напишите функцию, которая принимает три числа. Третье число – результат какой-то операции над первыми двумя числами
# (+, -, *, /). Выведите, какая это была операция.
# get_operation(2, 5, 7) => '+'
# get_operation(11.1, 8, 88.8) => '*'
# Иногда пользователь может не понять, что передавать в функцию, и передать совсем другие вещи. Числа,
# которые друг с другом вообще не связаны, строки, списки.
# Для этого добавьте в функцию отлова базовых ошибок с различными сообщениями и предупреждениями.


def operation_correct(func):
    def wrapper(*args, **kwargs):
        correct_data_type = True

        for param in  list(args):
            if not isinstance(param, (int, float)):
                correct_data_type = False
                return f'Incorrect data type of param {param}. Was expected int or float, but received {type(param)}!'

        if correct_data_type:
            ans = func(*args, **kwargs)
            return ans if ans is not None else 'Any mathematical operations with numbers will not give the expected result!'
    return wrapper

@operation_correct
def get_operation(first: int|float, second: int|float, result: int|float) -> str:
    operations = ['+', '-', '/', '*']

    for operation in operations:
        if eval(f'{first}{operation}{second}') == result:
            return operation

print(get_operation('2', 5, -3))
print(get_operation([3], 5, -3))
print(get_operation(88.8, 11.1, 8))
print(get_operation(2, 3, 5))
print()


# Напишите декоратор, который будет выводить имя запускаемой функции. Это задачка на самостоятельный поиск информации!
# Есть несколько разных способов это сделать, попытайтесь найти один из них.
# Не стесняйтесь гуглить и искать любую доступную информацию.


def decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Method [{func.__name__}] running now!')
        func(*args, **kwargs)
    return wrapper

@decorator
def chototam(lst):
    print(lst)

chototam([1,2,3,4,5])