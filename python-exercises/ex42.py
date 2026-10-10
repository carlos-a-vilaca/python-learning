'''Cria o jogo da adivinha v2.0. O computador "pensa" num número de 0 a 10 e o utilizador tenta adivinhar até acertar. No final mostre
quantas tentativas foram necessárias.

import random
numero_secreto = random.randint(0, 10)'''

import os 
import random

os.system('cls')

print('--- JOGO DE ADIVINHA v2.0. ---\n')

adivinha = random.randint(0, 10)
utilizador = int(input('Insira um número: '))
contador = 0


#enquanto o numero do utilizador for diferente o computador vai
#pedir para inserir outra vez, depois aumenta no contador +1 para depois imprimir o valor de tentativas foram necessárias
while adivinha != utilizador:
     utilizador = int(input('Insira um número: '))
     
     contador += 1

print(f'O número secreto era: {adivinha}')
print(f'Foram necessárias {contador} tentativas')  


