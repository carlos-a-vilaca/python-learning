'''Escreva um
algoritmo que leia uma lista com 10 posições de números inteiros. Em seguida, leia um novo valor do utilizador e verifique se este
valor se encontra na lista. Faça um menu (usando um dicionário a mapear
a opção do utilizador à função correspondente) com as três hipóteses seguintes:

a. Encontrar a última posição

b. Encontrar a primeira posição

c. Encontrar todas as posições — devolvendo-as como um tuplo de posições

i. Se estiver, informe a última posição onde esse elemento se encontra na
lista. Caso o elemento não esteja na lista, apresente a mensagem "O número
não se encontra na lista".

ii. Se estiver, informe a primeira posição onde esse elemento se encontra na
lista. Caso o elemento não esteja na lista, apresente a mensagem "O número
não se encontra na lista".

iii. Se estiver, informe todas as posições onde esse elemento se encontra na
lista. Caso o elemento não esteja na lista, apresente a mensagem "O número
não se encontra na lista".'''

import os 
os.system('cls')

lista_de_10n = []

todas_as_posicoes = []
primeira_posicao = None 
ultima_pocicao = None
n = 1

   #introduz 10 numeros inteiros
for i in range(10):
    numero = int(input(f'Insira o {n}º número: '))
    lista_de_10n.append(numero)
    n += 1

numero_utilizador = int(input('Insira o número que quer procurar: '))

if numero_utilizador not in (lista_de_10n):
        print('O número não se encontra na lista!')
while True:
    menu = {
        'a':'Encontrar a ultima_posicao',
        'b':'Encontrar a primeira_posicao',
        'c':'Encontrar a todas_pocicoes',
        'd':'Sair'
    }

    for o in menu:
        print(f'{o}. {menu[o]}')
    print()
    opcao = input('Insira a opção que deseja: ').lower()

    for n in range(len(lista_de_10n)):
        if lista_de_10n[n] == numero_utilizador:
            ultima_pocicao = n
            #adiciona todas as posições que encontra o número
            todas_as_posicoes.append(n) 
            if primeira_posicao == None:
                primeira_posicao = n

    if opcao == 'a':#imprime a última posição 
        print(f'A ultima posição {ultima_pocicao}')
            
    elif opcao == 'b':#imprime a primeira posição 
        print(f'A primeira posição {primeira_posicao}')


    elif opcao == 'c':#imprime todas posições do valor 
        for u in todas_as_posicoes:        
            print(f'O número do utilizador foi encontrado na posição {u}')

    elif opcao == 'd':
        break
    else:
        print('Opeção inválida!')