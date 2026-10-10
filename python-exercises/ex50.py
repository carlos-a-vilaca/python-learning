'''Cria um programa que leia a idade e o sexo de várias pessoas. A cada pessoa registada pergunta se quer continuar. No final mostre:
a. Quantas pessoas têm mais de 25 anos
b. Quantos homens com menos 17 anos foram registados
c. Quantas mulheres foram registadas
d. Quantos menores de idade foram registados'''



import os 
os.system('cls')

pessoas_maiores_25 = 0
homens_menos_17 = 0
menores_de_idade = 0
mulheres = 0

while True:
    
    idade_da_pessoa = int(input('Insira a sua idade: ').strip())
    sexo_da_pessoa = input('Insira o seu sexo: ').lower().strip()
    continuar = input('Quer continuar (Sim/Não)? ').lower().strip()


    if idade_da_pessoa > 25:
        pessoas_maiores_25 += 1
    if sexo_da_pessoa == 'homem' and idade_da_pessoa < 17:
        homens_menos_17 += 1
    if sexo_da_pessoa == 'mulher':
        mulheres += 1 
    if idade_da_pessoa < 18:
        menores_de_idade += 1

    if continuar == 'sim':
        continue
    elif continuar == 'não' or continuar == 'nao':
        break
    
                
print(f'Tem {pessoas_maiores_25} pessoas com mais de 25 anos')
print(f'Tem {homens_menos_17} homens com menos de 17 anos')
print(f'Tem {mulheres} resgistadas')
print(f'Tem {menores_de_idade} menores de idade registados')
