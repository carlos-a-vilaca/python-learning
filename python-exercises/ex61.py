'''Cria um programa que crie uma matriz 3x3 e a preencha com valores lidos do teclado.
No final, mostra a matriz no ecrã com a formatação adequada.'''

import os 
os.system('cls')

#criar a matriz
matriz = []

#leitura dos valores
for linha in range(3):
    linha = []
    for coluna in range(3):
        valor = int(input(f'Insira um valores [{linha}] [{coluna}]:'))
        linha.append(valor) 
 
