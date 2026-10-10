'''Cria um programa onde o utilizador possa introduzir vários números e guardá-los numa lista.
Se o número já existir na lista, não deve ser adicionado.
No final, mostra todos os valores por ordem decrescente.'''

import os 
os.system('cls')


lista = []

while True:
    numero = int(input('Insira um númaro que quer guardar na lista: '))
    if numero not in lista:
        lista.append(numero)
        print('Número adicionado!')
    else: 
        print('O Número já existe na lista')

    continuar = input('Deseja guardar mais algum número (S/N): ').upper()

    if continuar == 'N':
        break

lista.sort(reverse=True)
print(f'Os números gurdados por  ordem decrecente: {lista}')

