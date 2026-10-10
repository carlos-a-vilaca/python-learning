'''Tabuada V2.0 — Cria um programa que mostre a tabuada de vários números inseridos pelo utilizador. O programa deverá ser
interrompido quando o número inserido for negativo ou 0.'''


import os 
os.system('cls')

print('--- Tabuada V2.0 ---')

while True:
    numero = int(input('Insira um número: '))
    if numero < 0 or numero == 0:
        break     

    for n in range(1, 11):
        print(f'{n} * {numero} = {numero * n}') 

      
