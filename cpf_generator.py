from random import randint
import os

os.system('cls')
n = int(input('Quantos CPFs gostaria de gerar? '))
print('-'*30)
for c in range(n):
    nove_d = ''
    soma_d1 = soma_d2 = d1 = d2 = 0

    cont = 10
    for i in range(9):
        nove_d += str(randint(0,9))
    for j in nove_d:
        soma_d1 += int(j) * cont
        cont -= 1
    if soma_d1 % 11 == 0 or soma_d1 % 11 == 1:
        d1 = 0
    else:
        d1 = 11 - (soma_d1 % 11)
    nove_d += str(d1)

    cont = 11
    for v in nove_d:        
        soma_d2 += int(v) * cont
        cont -= 1
    if soma_d2 % 11 == 0 or soma_d2 % 11 == 1:
        d2 = 0
    else:
        d2 = 11 - (soma_d2 % 11)
    nove_d += str(d2)

    print(f'{nove_d[:9]}-{nove_d[9:]}')