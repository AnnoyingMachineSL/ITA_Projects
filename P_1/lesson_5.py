import re


# re.findall(pattern, string, flags) - найти все совпадения в строке
# re.search() - найти совпадения в строке
# re.search().group() - возвращает совпадение
# re.search().span() - возвращает промежуток совпадения
# re.search().string - возвращает изначальную строку
# re.split() - разредить строку на список
# re.sub(pattern, new_string, string, flags) - заменить все pattern на new_string

# re.I - ignore case

# string = 'a,bABCc_de.123.ab*c'
# print(re.findall('[a-zA-Z]', string))

# кот(?=собака) - positive lookahead
# кот(?!собака) - negative lookahead
# (?<=кот)собака - positive lookbehind
# (?<!кот)собака - negative lookbehind


# ДЗ:
# Напишите функцию, которая берёт предложение, и сокращает каждое слово в котором больше трёх букв.
# В слове находится первая гласная после третьего символа, и все буквы после неё заменяются на точку.
# Например “Hello! I love dogs .” превратится в “Hell.! I lov. dogs.”


# Напишите проверку телефонных номеров. Вам будет дана любая строка, сохранятся должен первый плюс и все цифры.
# Если получившаяся строка соответствует шаблону /\+\d{10, 12}/, то выведите её, если нет, то выведите ошибку



#Напишите функцию, которая берёт предложение, и сокращает каждое слово в котором больше трёх букв.
# В слове находится первая гласная после третьего символа, и все буквы после неё заменяются на точку.
# Например “Hello! I love dogs .” превратится в “Hell.! I lov. dogs.”


import string
def abbreviation_words(stg: str) -> str:
    letters = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    words_list = [word for word in stg.split(' ') if word not in string.punctuation]
    ans = []

    for word in words_list:
        if len(word) > 3:
            try:
                word = word[:3] + word[3:][:word[3:].index(re.search(f'{letters}', word[3:]).group()) +1] + '.'
            except AttributeError:
                word = word[:3] + '.'
        ans.append(word)
    return ' '.join(ans)

print(abbreviation_words('Hello! I love dogs .'))



# Напишите проверку телефонных номеров. Вам будет дана любая строка, сохранятся должен первый плюс и все цифры.
# Если получившаяся строка соответствует шаблону /\+\d{10, 12}/, то выведите её, если нет, то выведите ошибку


#sad+qwe+37llk5_sdasd29ooppppef361-79sada-44

def phone_number(stg: str)-> str:
    pattern = '[+][0-9]{10,12}'
    ans = '+' + re.sub('[^0-9]|[a-z]]', '', stg)
    return(ans) if re.match(pattern, ans) != None else "Can't find a phone number!"



print(phone_number('sad+qwe+37llk5_sdasd29ooppppef361-79sada-44'))