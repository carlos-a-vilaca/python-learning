'''Cria um programa que sorteie a ordem de jogada num jogo ao "atirar um dado ao ar".
Cada jogador terá um número aleatório associado dentro de um dicionário.
No final ordene o ranking para ver a ordem de jogada.'''
#importar 
import os
from time import sleep
from random import randint

os.system('cls')

# #variáveris dicionário 
# lista_de_jogadores = {}
# ranking = {}

# print('====== JOGO DO DADO ======')
# quantos_jogares = int(input('Insira quantos jogadores vão participar: '))

# #variáveis axiliar 
# numero_de_jogador = 1


# for jogo in range(quantos_jogares):
#     #registo do jogador 
#     lista_de_jogadores[f'jogador{numero_de_jogador}'] = randint(1, 6) 
#     numero_de_jogador += 1

# #resultados dos jogadores    
# for chave, valor in lista_de_jogadores.items():
#     print(f'O {chave} atirou o dado e teve {valor}')
#     sleep(1)

# print()

# #ranking 
# print('====== RANKING ======')
# #ordenar jogadores do maior valor para o valor menor 
# ranking = sorted(lista_de_jogadores.items(), key=lambda valor: valor[1], reverse=True)    
# classificacao_jogador = 1

# for k, v in ranking:
#     print(f'{classificacao_jogador}º --> {k} atirou o dado {v}')
#     classificacao_jogador += 1
#     sleep(1)





jogadores = {}

quantidade = int(input('Quantos jogadores vão participar? '))

for i in range(quantidade):
    nome = input(f'Nome do jogador {i + 1}:')
    numero = randint(1, quantidade)

    while numero in jogadores.values():
        numero = randint(1, quantidade)

    jogadores[nome] = numero

print('='* 40)
print('Resultado do lançamento do dado: ')


for nome in jogadores:
    print(f'{nome} --> {jogadores[nome]}')
print('=' * 40)

for numero in range(1, quantidade + 1):
    for nome in jogadores:
        if jogadores[nome] == numero:
            print(f'{numero}º - {nome}')







# adicionar_jogador = input('Adicionar jogador? (S/N) ').upper()        
 # if adicionar_jogador == 'S':
    #     print('JOGADOR ADICIONADO!')
    #     sleep(1)
    # else:
    #     print('GAME OVER')
    #     break
    # adicionar_jogador = input('Adicionar mais um jogador? (S/N) ').upper()
