'''Melhora o exercício 61, exibindo no final:
a) A soma de todos os valores pares
b) A soma dos valores da segunda coluna
c) O maior valor da terceira linha'''

import os 
os.system('cls')
#criar a matriz
matriz = []


#variáveis auxiliares 
soma_pares = 0
soma_segunda_linha = 0  
maior_terceira_linha = None


for linha in range(3):
    linha = []
    for coluna in range(3):
        valor = int(input(f'Insira um valores [{linha}] [{coluna}]:'))
        linha.append(valor)
        #a)soma dos pares 
        if valor % 2 == 0:
            soma_pares += valor
        #b)a soma da segunda coluna
        if coluna == 1:
            soma_segunda_linha += valor
    matriz.append(linha)

#maior da terceira coluna
maior_terceira_linha = max(matriz[2])    

#mostrar a matriz
print('\nMatriz 3x3')
for linha in matriz:
    for valor in linha:
        print(f"{valor:4}", end='')
    print() 

#resultados 
print(f'A soma de todos os valores pares {soma_pares}')
print(f'A soma dos valores da segunda coluna {soma_segunda_linha}')
print(f'O maior valor da terceira linha {maior_terceira_linha}')             
 


