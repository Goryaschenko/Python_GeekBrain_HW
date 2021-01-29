"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4


Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

# Используйте Альфа версию модуля. Стандартная не работает с конца 2020г
# pip install googletrans==3.1.0a0

from googletrans import Translator

translator = Translator()

with open("4.1_translate.txt", "r", encoding='utf-8') as f:
    contents = f.read()
    result = translator.translate(contents, dest='ru')
    print(result.text)

with open("4.2_translate.txt", "w", encoding='utf-8') as f:
    f.write(result.text)
