# if elif else - цикл условий
# range(start, end, step)
# x = x*2   ===   x *= 2
# for i in nums - каждый элемент nums
# for i in range(len(nums)) - каждый индекс в nums
# while - пока условие истинно
# break - насильно выйти из цикла
# try except - подловить возникнувшую ошибку
# while else / for else - else срабатывает в случае, если цикл разорвался не со словом break
# try except else - else срабатывает, если не сработал except
# finally - выполняется в самом конце цикла
# continue - сразу перейти к следующей итерации

# separator.join(list) - перевести список в строку
# str.split(separator) - перевести строку в список


# Удалить всех волков из списка овец:
# sheep = ['овца', 'волк', 'волк', 'овца', 'овца', 'овца', 'волк']

# for i in range(sheep.count('волк')):
#     sheep.remove('волк')
#     print(sheep)

# while 'волк' in sheep:
#     sheep.remove('волк')
#     print(sheep)


# Выход из вложенных циклов:
# list_of_lists = [[1, 2], [3, 4], [5, 6]]
# for i in list_of_lists:
#     for j in i:
#         if j == 3:
#             break
#     else:
#         continue
#     break


# True OR False = True
# True AND False = False


# ДЗ:
# Вам будет дана строка и цифра n. Ваша задача – убрать все первые n букв алфавита из этой строки.
# Русский алфавит = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
# 'Привет!' 3 => 'Приет!'
# 'Ого, я тоже учу пайтон' 50 => ',    ' (удаляем всё, кроме специальных символов, если цифра больше, чем букв алфавита)
# 'АбраКадабра' 5 => 'рКр'
# 'Строка' -2 => 'Строка' (ничего не меняем, если цифра меньше единицы)

# Автобус ходит каждые 20 минут, начиная в 7 утра и заканчивая в 23 вечера. Чтобы дойти от дома до остановки,
# нужно 5 минут. Напишите программу, которая принимает нынешнее время и возвращает, через сколько минут нужно выйти,
# чтобы попасть на автобус.
# 7:15 => 0
# 9:00 => 15
# 21:50 => 5
# 1:00 => 355

# Дан список 0 и 1. Необходимо вывести наибольшее количество единиц, которые стоят друг за другом.
# [1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0] => 3
# [0, 0, 1, 1, 0, 1] => 2
# [0, 0, 0, 0, 0, 0, 0, 0, 0] => 0


#Вам будет дана строка и цифра n. Ваша задача – убрать все первые n букв алфавита из этой строки.
# Русский алфавит = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
# 'Привет!' 3 => 'Приет!'
# 'Ого, я тоже учу пайтон' 50 => ',    ' (удаляем всё, кроме специальных символов, если цифра больше, чем букв алфавита)
# 'АбраКадабра' 5 => 'рКр'
# 'Строка' -2 => 'Строка' (ничего не меняем, если цифра меньше единицы)


def string_cutter(string, num):
    letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    if num < 0:
        return string
    else:
        set_letters = letters if num > len(letters) else letters[:num]

        for letter in string:
            if letter.lower() in set_letters:
                string = string.replace(letter, '')
        return string

print('N1')
print(string_cutter('Привет!' ,3))
print(string_cutter('Ого, я тоже учу пайтон',50 ))
print(string_cutter('АбраКадабра', 5))
print(string_cutter('Строка' ,-2))
print()


# Автобус ходит каждые 20 минут, начиная в 7 утра и заканчивая в 23 вечера. Чтобы дойти от дома до остановки,
# нужно 5 минут. Напишите программу, которая принимает нынешнее время и возвращает, через сколько минут нужно выйти,
# чтобы попасть на автобус.
# 7:15 => 0
# 9:00 => 15
# 21:50 => 5
# 1:00 => 355


def time_manager(time_string: str):
    parrot = int(''.join(time_string.split(':')))
    schedule = [time for time in range(700, 2320, 20) if time%100 <= 40]

    if parrot < schedule[0]:
        return int((schedule[0] - parrot) - round((schedule[0] - parrot)/100) * 40 - 5)

    else:
        nearest_parrot = ''
        dif = 500

        for time in schedule:
            if abs(time - parrot) < dif and abs(time - parrot) >= 5 and time > parrot:
                nearest_parrot = time
                dif = abs(time - parrot)

                nearest_parrot = nearest_parrot if nearest_parrot - parrot >=45 or nearest_parrot - parrot <= 25 else schedule[schedule.index(nearest_parrot) + 1]
                return abs(nearest_parrot - parrot) - 5 if abs(nearest_parrot - parrot) < 45 else abs(nearest_parrot - parrot) - 45

print('N2')
print(time_manager("7:15"))
print(time_manager("9:00"))
print(time_manager("21:50"))
print(time_manager("1:00"))
print()


# Дан список 0 и 1. Необходимо вывести наибольшее количество единиц, которые стоят друг за другом.
# [1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0] => 3
# [0, 0, 1, 1, 0, 1] => 2
# [0, 0, 0, 0, 0, 0, 0, 0, 0] => 0


def sequence_counter(lst):
    current, max_sequence = 0, 0

    for element in lst:
        if element == 1:
            current+=1
            max_sequence = current if current > max_sequence else max_sequence
        else:
            current = 0
    return max_sequence

print('N3')
print(sequence_counter([1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0])) # => 3
print(sequence_counter([0, 0, 1, 1, 0, 1])) # => 2
print(sequence_counter([0, 0, 0, 0, 0, 0, 0, 0, 0])) # => 0
print()


# a = ['aaa', 'dddd', 'qweqw']
# # b = [len(st) for st in a]
# # print(b)
# #
# b = list(map(lambda x: len(str(x)), a))
# print(b)

#stairs(5, 1) => [5, 4, 3, 2, 1, 0]


def steps(num_step, step):
    list_1 = list(range(num_step,0,-step))
    list_1.append(0)

steps(49,8)


lst = [1,2,3,4,5,6,7,8,9]
lst_2 = list(filter(lambda x: x%2 ==0,lst))
print(lst_2)


def mul(*args):
    res = 1
    for i in args:
        res *=i
    return res


print(mul(1,2,3,4,7))