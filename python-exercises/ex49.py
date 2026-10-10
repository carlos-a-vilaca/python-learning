'''Cria o jogo par ou ímpar. O jogo só será interrompido quando o jogador perder e deverá exibir o total de vitórias consecutivas.'''
import os 
os.system('cls')
import random 

print('\n--JOGO PARA OU IMPAR--')

contador = 0 #conta as vitórias consecutivas




while True:
    #o computador escolhe um número aleatório entre 1 e 10
    computador = random.randint(1, 10)
    jogador = int(input('Insira um número: '))
    aposta = input('Escolha "PAR" ou "IMPAR": ').lower()
    soma = computador + jogador

    # vê se a soma é par (resto da divisão por 2 é 0) ou ímpar
    if soma % 2 == 0:
        resultado = 'par'
    
    else:
        resultado = 'impar' 
    print(f'O computador escolheu {computador}. A soma foi {soma}, ou seja, {resultado}.')   

    # compara a aposta do jogador com o resultado real
    if aposta == resultado:
        contador += 1 
        
    else:
        print(f'\nGAME OVER')
        break

print(f'\n Tens o total de vitórias consecutivas de {contador}')        


   


        