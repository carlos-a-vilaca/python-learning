'''Cria o jogo da adivinha v1.0. O computador "pensa" num número de 0 a 7 e o utilizador deve adivinhar.
1. Gerar um número aleatório entre 0 e 7
2. Pedir ao utilizador para adivinhar
3. Comparar e mostrar se ganhou ou perdeu

from random import randint
numero_secreto = randint(0, 7)'''
import os 
from random import randint
os.system('cls')
print('--Jogo da adivinha v1.0.--')

computador = randint(0, 7)
utilizador = int(input('Isira um número de 0 a 7: '))

if utilizador == computador:
    print('Você Ganhou')
else: 
    print ('Você Perdeu')