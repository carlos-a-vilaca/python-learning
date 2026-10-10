'''Cria um programa que gere 5 números aleatórios dentro de um tuplo.
No final mostra:

os números gerados
o menor valor
o maior valor'''

import random
import os
os.system('cls')

tuplo = ()


for i in range(5):
    numero_aleatorio = random.randint(0, 100)
    tuplo += (numero_aleatorio,)

print(tuplo)  
print(f'O valor menor é {max(tuplo)}')
print(f'O valor menor é {min(tuplo)}')  