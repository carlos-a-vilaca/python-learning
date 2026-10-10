'''Cria um programa que gere palpites para o Euromilhões.
O programa deve:
perguntar quantas chaves serão geradas
sortear aleatoriamente 5 números de 1 a 50 (sem repetir) e 2 estrelas de 1 a 12 (sem repetir)
Cada sorteio deve ser guardado numa lista composta.'''

#perguntar quantas vezes serão geradas o limite de repitições é o número que o utilizador defenir 
#dentro de quantas chaves o utilizador defenir vai sortear 5 numeros e duas estrelas 
#cada sorteiro deve ser gurdado numa lista composta 

import os
import random
os.system('cls')



#chaves do euromilhões 
# chaves_euromilhoes = []


# quantas_chaves_geradas = int(input('Quantas chaves quer gerar?  '))

# #ciclo para gerar os números e estrelas 
# for chave in range(quantas_chaves_geradas):

#     #sortear os 5 números 
#     lista_de_numeros = []
#     for numero in range(1, 51):
#         #adiciona os números de 1 a 51 à lista de números 
#         lista_de_numeros.append(numero)     

#     #sortear duas estrelas 
#     lista_de_estrelas = []
#     for estrela in range(1, 13):
#         #adiciona cada estrela à lista de estrelas de 1 a 12
#         lista_de_estrelas.append(estrela)
#         #de um a 12 soteia os numeros da lista    

        
#     chaves_euromilhoes.append(sample(lista_de_numeros, 5))  
#     chaves_euromilhoes.append(sample(lista_de_estrelas, 2))

# num_de_chaves = 1

# for i in range(0, len(chaves_euromilhoes), 2):
#     print(f'Chave {num_de_chaves}')
#     num_de_chaves += 1
#     print('OS NÚMEROS -> ', end='')
#     for valores in chaves_euromilhoes[i]:
#             print(f'{valores}',end=' ')
#     print()        
#     print('AS ESTRELAS -> ', end='')        
#     for estrelas in chaves_euromilhoes[i+1]:
#          print(f'{estrelas}', end=' ')
#     print()        
    
   
        


# lista_de_numeros = []

# for numero in range(1, 51):
#     lista_de_numeros.append(numero)

# print(sample(lista_de_numeros, 5))

#correção 

quantas_chaves_geradas = int(input('Quantas chaves quer gerar?  '))

while quantas_chaves_geradas <= 0:
    quantas_chaves_geradas = int(input('Quantas chaves pretende gerar: '))     

todas_as_chaves = []

for i in range(quantas_chaves_geradas):
    numeros = []

    while len(numeros) < 5:
        numero = random.randint(1, 50)

        if numero not in numeros:
            numeros.append(numero)
    numeros.sort()

    estrelas = []
    while len(estrelas) < 2:
        estrela = random.randint(1, 12)

        if estrela not in estrelas:
            estrelas.append(estrela)        
    estrelas.sort()

chave = [numeros, estrelas]

todas_as_chaves.append(chave)



print('-'*40)

indice = 1 

for chave in todas_as_chaves:
    print(f'Chave {indice}: Números: {chave[0]} | Estrelas: {chave[1]}')
