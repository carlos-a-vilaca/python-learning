'''Cria um programa que leia o ano de nascimento de 7 pessoas e mostre quantas são maiores de idade e quantas não são.'''

import os 
os.system('cls')

#aqui tem a variável que define o ano 
ano_atual = 2026
#duas variáveis para contar quais são maiores de idade ou não
contador_maior = 0
contador_menor = 0

#o programa vai gerar um ciclo 7 vezes a pedir o ano de nascimento a 7 pessoas 
for d in range(7):
    ano_de_nascimento = int(input('Insira o seu ano de nascimento: '))
    #a variável idade vai receber o ano que o utilizador inseriu menos o ano que eu defini 
    #que depois vai dar a idade dele 
    idade = ano_atual - ano_de_nascimento
    #vou fazer comparações para ver se é maior de idade se sim aumentar o contador para +1
    if idade >= 18:  
        contador_maior = contador_maior + 1  
    #se a idade for menor a 18 o contador de menores vai aumentar +1    
    elif idade < 18:      
        contador_menor = contador_menor + 1
#vai imprimir os contadores 
print(f'Tem {contador_maior} pessoas maiores de idade.')
print(f'Tem {contador_menor} pessoas menores de idade.')