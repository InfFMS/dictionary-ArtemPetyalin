# Даны два словаря. Напишите программу, которая объединит эти словари. 
# Если ключи встречаются в обоих исходных словарях, значения, 
# которые хранятся по этим ключам складываются.
# Пример:

# Первый словарь: {'a': 100, 'b': 200, 'c':300}
# Второй словарь: {'a': 300, 'b': 200, 'd':400}
# Результат: {'a': 400, 'b': 400, 'd': 400, 'c': 300}

d1 = {input(f'key {i + 1} '):int(input(f'value {i + 1} ')) for i in range(int(input('length 1 ')))}
d2 = {input(f'key {j + 1} '):int(input(f'value {j + 1} ')) for j in range(int(input('length 2 ')))}
keys3 = []
values3 = []
d3 = {}
a = list(d1.keys())
b = list(d2.keys())
tse = list(d1.values())
d = list(d2.values())
b1 = b[:]
a1 = a[:]
tse1 = tse[:]
d1 = d[:]

for i in range(len(a)):

    for j in range(len(b)):
        print(i, j)

        if a[i] == b[j]:
            keys3.append(a[i])
            values3.append(tse[i] + d[j])
            a1.remove(a[i])
            b1.remove(b[j])
            tse1.remove(tse[i])
            d1.remove(d[j])

keys3 = keys3 + a1 + b1
values3 = values3 + tse1 + d1

for i in range(len(keys3)):
    d3[keys3[i]] = values3[i]

print(d3)



