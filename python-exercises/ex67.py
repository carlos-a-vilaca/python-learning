'''Cria um programa que guarde o aproveitamento de um jogador de futebol: nome, jogos jogados e golos por jogo, tudo num
dicionário.

Calcula também a média de golos por jogo.'''
import os 
from time import sleep
os.system('cls')

# #dicionário 
# aproveitamento_do_jogador = {}

# #adicionar ao dicionários
# aproveitamento_do_jogador['nome'] = input('Digite o nome do jogador: ')
# aproveitamento_do_jogador['jogos_jogados'] = int(input('Quantos jogos jogados tem: '))

# #variável auxiliar para guardar todos os golos por jogo se não vão se perder a cada ciclo 
# lista_de_golos_pj = []
# registo_de_golos = 0

# #calcular a média de golos por jogo 
# for g in range(aproveitamento_do_jogador['jogos_jogados']):
#     aproveitamento_do_jogador['golos_por_jogo'] = int(input('Golos por jogo: '))

#     #adiciona os golos por jogo numa lista para não se perderem 
#     lista_de_golos_pj.append(aproveitamento_do_jogador['golos_por_jogo'])
#     registo_de_golos = registo_de_golos + aproveitamento_do_jogador['golos_por_jogo']


# #adicionar a lista de golos ao dicionário
# aproveitamento_do_jogador['golos_por_jogo'] = lista_de_golos_pj

# print('=================================')
# #imprimir o jogo e o golos por jogo de um jogador 
# for i in range(len(lista_de_golos_pj)):
#     #i mais um é o numero do indice mais um para não começar no 0 | cada índice vai ser um jogo  
#     #lista de jogos [i] vai me dar o que tem dentro de cada indice neste caso núemero de golos 
#     sleep(1)
#     print(f'jogo {i + 1} marcou --> {lista_de_golos_pj[i]}')

# print('=================================')
# #calcúlo da media de golos por jogo 
# media_golos_jogo = registo_de_golos / aproveitamento_do_jogador['jogos_jogados']

# print(f'A média de golos por jogo é {media_golos_jogo:.2}.')



# print(f'A média de golos por jogo é {media_golos_jogo}')

jogador = {}

jogador['nome'] = input('Digite o nome do jogador: ')
jogador['jogos'] = int(input('Quantos jogos jogados tem: '))

golos = []

for i in range(jogador['jogos']):
    quantidade = int(input(f'Golos marcados no {i + 1} jogo: '))
    golos.append(quantidade)

jogador['golos'] = golos 

#função sum soma todos os números de uma lista ou tuplo
jogador['total'] = sum(golos)
jogador['media'] = jogador['total'] / jogador['jogos']


print('=' * 30)
print(f'Nome: {jogador['nome']}')
print(f'Jogos disputados: {jogador['jogos']}')
print(f'Golos por jogo: {jogador['golos']}' )
print(f'Total de golos: {jogador['total']}')
print(f'Média de golos por jogo {jogador['media']:2f}')
print('='*30)

