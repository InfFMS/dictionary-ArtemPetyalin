# Представьте, что вы шпионы)
# Придумайте шифр, в котором буквы заменяются на какие-то символы
# и реализуйте шифроватор и дешифроватор
from typing import List

sypher = {'a':'^', 'b': ')', 'c': '@', 'd':'_', 'e':','}
desypher = {a:b for b, a in sypher.items()}

a = int(input('1 or 2? '))


if a == 1:      #шифроватор
    l = ''

    for i in input():

        for j in list(sypher.keys()):

            if i == j:
                l += sypher[j]


else:
    l = ''

    for i in input():

        for j in list(desypher.keys()):

            if i == j:
                l += desypher[j]



print(l)




