
'''Cria um programa que guarde o aproveitamento de um jogador de futebol: nome, jogos jogados e golos por jogo, tudo num
dicionário.

Calcula também a média de golos por jogo.'''

'''Melhora o exercício 67 para que permita a entrada de vários jogadores.
Define um sistema de visualização que permita ao utilizador procurar pelos resultados de um jogador específico.'''
'''
#variável auxiliar para guardar todos os golos por jogo se não vão se perder a cada ciclo 
lista_ad_jogadores = []


#ciclo para adicionar vários jogadores e vários a lista de jogos jogados 
#adicionar ao dicionários
while True:
    #lista que vai adicionar os jogadores ao meu dicionário 
    jogador = {}
    lista_de_golos_pj = []
    registo_de_golos = 0
    aproveitamento_do_jogador = {}


    jogador['nome'] = input('Digite o nome do jogador: ')
    jogador['jogos_jogados'] = int(input('Quantos jogos jogados tem: '))

    #calcular a média de golos por jogo 
    for g in range(jogador['jogos_jogados']):
        jogador['golos_por_jogo'] = int(input('Golos por jogo: '))
        #adiciona os golos por jogo numa lista para não se perderem 
        lista_de_golos_pj.append(jogador['golos_por_jogo'])
        registo_de_golos = registo_de_golos + jogador['golos_por_jogo']

    lista_ad_jogadores.append(jogador)

    entrada_dos_jogadores = input('Deseja da entrada de mais algum jogador (S/N): ').upper().strip()

    #adicionar a lista de golos ao dicionário
    aproveitamento_do_jogador['golos_por_jogo'] = lista_de_golos_pj

    
    if entrada_dos_jogadores == 'S':
        print('Adicione mais jogadores..')
     
        
    else:
        print('Encerrou a entrada de jogadores a escrever os resultados...')
        break


#imprimir o jogo e o golos por jogo de um jogador 
print('=================================')
for i in range(len(lista_de_golos_pj)):
    #i mais um é o numero do indice mais um para não começar no 0 | cada índice vai ser um jogo  
    #lista de jogos [i] vai me dar o que tem dentro de cada indice neste caso núemero de golos 
    print(f'jogo {i + 1} marcou --> {lista_de_golos_pj[i]}')

#calcúlo da media de golos por jogo 
print('=================================')
media_golos_jogo = registo_de_golos / jogador['jogos_jogados']
print(f'A média de golos por jogo é {media_golos_jogo}.')'''
import os 
os.system('cls')


jogadores = []

while True:
    jogador = {}

    jogador['nome'] = input('Digite o nome do jogador: ')
    jogador['jogos'] = int(input('Quantos jogos jogados tem: '))

    golos = []

    for i in range(jogador['jogos']):
        quantidade = int(input(f'Golos marcados no {i + 1} jogo: '))
        golos.append(quantidade)

    jogador['golos'] = golos 
    jogador['total'] = sum(golos)
    jogador['media'] = jogador['total'] / jogador['jogos']

    jogadores.append(jogador)

    resposta = input('Pretende adicionar outro jogador? (S/N)').upper().strip()

    while resposta not in('S', 'N'):
         resposta = input('Resposta inválida! Introduza S ou N: ').strip().upper() 

    if resposta == 'N':
     break
  
print('=' * 45)
print(f'{'Nº':<4}{'Nome':<20}{'Jogos':<8}{'Total':<8}{'Média':<8}')

numero = 1 

for jogador in jogadores:
    print(f'{numero:<4}{jogador['nome']:<20}{jogador['jogos']:<8}{jogador['total']:<8}{jogador['media']:.2f}')
    numero +=1

print('='*45)

while True:
    escolha = int(input('Mostar dados dos jogador (0 termina)?'))
    if escolha == 0:
        break 
    if escolha >= 1 and escolha <= len(jogadores):
        jogador = jogadores[escolha - 1]

        print('-'*45)
        print(f'Nome: {jogador['nome']}')
        print(f'Jogos: {jogador['jogos']}')
        print(f'Golos por jogo: {jogador[golos]}')

        jogo = 1 
        for golos in jogador['golos']:
            print(f'No jogo {jogo} marcou {golos} golos.')
        jogo += 1
        print(f'Total de golos: {jogador['total']}')
        print(f'Média de golos: {jogador['media']}')

    else:
        print('Jogador inexistente!')

print('Programa termina')