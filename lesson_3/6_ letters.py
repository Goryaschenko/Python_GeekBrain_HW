"""
Задание6:
 Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
 но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().

Задание со *
Программа дожна работать через ord().
"""


def int_func(words):
    words = words.title()
    return words


# #### ОДНО СЛОВО ####
# # text = input("Введи слово: ")
# # print(int_func(text))
#
# #### НЕСКОЛЬКО СЛОВ ####
# text = list(map(str, input().split()))
# text = " ".join(text)
# print(int_func(text))


###Решение азадния со * ####

def ord_func(words):
    result = list()
    for word in words:
        first = ord(word[0])
        if first >= 97:
            first -= 32
        rep = chr(first)
        pre_result = rep + word[1:]
        result.append(pre_result)
    return " ".join(result)




text = list(map(str, input().split()))
print(ord_func(words=text))
