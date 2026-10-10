#Cria um programa que leia a idade de 10 pessoas. No final mostre qual foi a maior idade lida e a menor.

import os 
os.system('cls')

maior_de_idade = 0 
menor_de_idade = 0  

for i in range(1, 11):
    idade = int(input('Insira a sua idade: ').strip())
    #aqui quando o i estar no um as variáveis vão receber as idades 
    #para depois comparar e imprimir a idade maior e a menor  
    if i == 1:
        maior_de_idade = idade 
        menor_de_idade = idade
          
    else:
        idade > maior_de_idade
        maior_de_idade = idade 
     
    if idade < menor_de_idade:
        menor_de_idade = idade 

print(f'A idade maior: {maior_de_idade}') 
print(f'A idade menor: {menor_de_idade}')                       



# maior = 0
# menor = 0
# # um ciclo de 1 até 10 para pedir 10 idades aos utilizadores 
# for i in range(1, 11):
#     idade = int(input('Insira a sua idade: ').strip())

# #se o i for igual a um guarda idade no maior ou no menor
#     if i == 1:
#         maior = idade 
#         menor = idade 

# #se não idade maior que a idade é maior que a idade que está em maior guarda a idade 
#     else:
    
#         idade > maior
#         maior = idade
# #se ao contrario guada na idade menor 
#     if idade < menor:
#         menor = idade  

# # depois é so escrever a idade nas variáveis maior e na menor 
# print(f'Maior de idade: {maior}') 
# print(f'Menor de idade: {menor}') 