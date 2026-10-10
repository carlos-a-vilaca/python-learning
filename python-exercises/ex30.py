#Cria o jogo pedra, papel, tesoura.



import os 
from random import randint

print('''--- Calculadora ---
[ 1 ] – Pedra 
[ 2 ] – Papel
[ 3 ] – Tesoura''')

computador = randint(0, 3)
utilizador = int(input('Insira um número: '))


if utilizador == computador:
    print('Empate')
elif computador == 1 and utilizador == 3:
    print(f'O BOT ecolheu: {computador} Você Perdeu')
elif computador == 2 and utilizador == 1:
    print(f'O BOT ecolheu {computador} Você Perdeu')    
elif computador == 3 and utilizador == 2:
    print (f'O BOT ecolheu {computador} Você Perdeu')    
elif utilizador == 1 and computador == 3:
    print(f'O Voçê escolehu {utilizador} Vôce Ganhou')
elif utilizador == 2 and computador == 1:
    print(f'O Voçê escolheu {utilizador} Você Ganhou')    
elif utilizador == 3 and computador == 2:
    print (f'O Voçê escolheu {utilizador} Você Ganhou')    
