# Создайте программу-переводчик, которая хранит перевод
#  слов с русского языка на английский.
# После запуска программа выводит список слов в словаре 
# и предлагает пользователю ввести слово для перевода. 
# Если введенного слова нет в словаре выводится сообщение "нет такого слова".
# Используйте словари для словаря:)

d = {'привет': 'hello', 'пока': 'goodbye', 'вода': 'water', 'пожалуйста': 'please'}
d1 = {a:b for b, a in d.items()}
a = input('Insert 1 for eng. Insert 2 for ru ')

if a == 1:
    word = input()

    for i in list(d.keys()):

        if word == i:
            print(d[i])
            break

        if i == list(d.keys())[-1]:
            print('Нет такого слова')


else:
    word = input()

    for i in list(d.keys()):

        if word == i:
            print(d1[i])
            break

        if i == list(d1.keys())[-1]:
            print('Нет такого слова')