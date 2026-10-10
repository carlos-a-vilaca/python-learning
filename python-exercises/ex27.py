'''Cria um programa que leia dois números inteiros e compare-os:
O primeiro número é maior
O segundo número é maior
Os números são iguais'''

numero1 = int(input('Insira primeiro número: '))
numero2 = int(input('Insira segundo número: '))

if numero1 > numero2:
    print(f'O número {numero1} é maior')
elif numero1 < numero2:
    print(f'O número {numero2} é maior') 
else:
    print('Os número são iguais')  