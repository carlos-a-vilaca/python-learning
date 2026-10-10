'''Cria um programa que leia o nome, sexo e idade de várias pessoas, guardando cada dado num dicionário e todos os dicionários
numa lista.

No final mostre:
a) Quantas pessoas foram registadas x
b) Qual a média de idades x 
c) Quantas mulheres foram registadas x
d) Quantos homens com idade acima da média foram registados'''
import os
os.system('cls')

#variáveis 
lista_de_pessoas = []
pessoas_registadas = 0
mulheres_registadas = 0
soma_idades = 0
homens_acima_media = 0

while True:
    pessoas = {}
    pessoas['nome'] = input('Insira o nome da pessoa: ').capitalize()
    pessoas['sexo'] = input('O seu sexo (M/F): ').upper().strip()

    if pessoas['sexo'] != 'M' and pessoas['sexo'] != 'F' :
            pessoas['sexo'] = input('Resposta inválida! Introduza M ou F: ')
    
    pessoas['idade'] = int(input('Insira a idade: '))
    pessoas_registadas += 1
    soma_idades = soma_idades + pessoas['idade']


    #mulheres registadas 
    if pessoas['sexo'] == 'F':
        mulheres_registadas += 1 
    #homens registados     
  
    #adiciona o dicionário à lista 
    lista_de_pessoas.append(pessoas)
    # print(lista_de_pessoas)

    #pedir se quer adicionar mais pessoas
    adicionar_pessoas = input('Pretende adicionar mais pessoas (S/N): ').upper().strip()

    while adicionar_pessoas not in('S', 'N'):
        adicionar_pessoas = input('Resposta inválida! Introduza S ou N: ').strip().upper()

    if adicionar_pessoas == 'N':
        break 

#média de idades // para dar número inteiro 
media_idades = soma_idades // pessoas_registadas

for homens in range(len(lista_de_pessoas)):
    print(lista_de_pessoas[homens])

                
print('='*40)

print(f'Total de pessoas registadas: {pessoas_registadas}')
print(f'A média de idades das pessoas registadas é {media_idades}')
print(f'Total de mulheres registadas: {mulheres_registadas}')
print(f'Total de homens com idade a cima da média: {homens_acima_media}')