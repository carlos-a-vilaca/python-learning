#Cria um programa que mostre a tabuada de um número introduzido pelo utilizador.

numero = int(input('Insira um número: '))

for n in range(0, 11):
    print(f'{numero} * {n} = {numero * n}')