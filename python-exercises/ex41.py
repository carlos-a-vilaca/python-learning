'''Cria um programa que faça 3 perguntas ao utilizador e apenas aceite como resposta "V" ou "F". Caso esteja errado, peça para repetir
até ter um valor correto.'''



import os 
os.system('cls')

resposta1 = ''
while resposta1 != 'V' and resposta1 != 'F':
    resposta1 = input('1. O sol é uma estrela? (V/F): ').strip().upper
    if resposta1 != 'V' and resposta1 != 'F':
        print('Resposta inválida! Digita apenas "V" ou "F".\n')



resposta2 = ''
while resposta2 != 'V' and resposta2 != 'F':
    resposta2 = input('1. A água ferve a 58 graus ao nivel do mar? (V/F): ').strip().upper
    if resposta2 != 'V' and resposta2 != 'F':
        print('Resposta inválida! Digita apenas "V" ou "F".\n')

resposta3 = ''
while resposta3 != 'V' and resposta3 != 'F':
    resposta3 = input('3. Python é uma linguagem de programação? (V/F): ').strip().upper
    if resposta3 != 'V' and resposta3 != 'F':
        print('Resposta inválida! Digita apenas "V" ou "F".\n')


print('---Respostas Registadas ---')
print('Pergunta 1:', resposta1)
print('Pergunta 2:', resposta2)
print('Pergunta 2:', resposta3)
