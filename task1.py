# Напишите программу, которая получает на вход две строки, и формирует из них словарь. 
# Ключами служат слова из первой строки, значениями – целые числа из второй.
# Пример ввода
# яблоки сливы груши персики манго киви апельсины
# 34 56 23 89 55 32 11
list1 = input().split()
list2 = input().split()
d = {}

for i in range(len(list1)):
    d[str(list1[i])] = str(list2[i])
    
print(d)