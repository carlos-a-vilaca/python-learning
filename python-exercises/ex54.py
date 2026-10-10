'''Cria um programa que leia 4 valores e os guarde num tuplo.
No final indica:
a) Quantas vezes aparece o número 7
b) Em que posição foi digitado o número 5
c) Quais são os números pares
O programa deve informar quando não encontrar resultados.'''


import os 
os.system('cls')

tuplo = ()
encontrado = False
pares = ()

for i in range(4):
    valor = int(input('Insira o valor: '))
    tuplo += (valor,)
 

if 7 in tuplo:
    print(f'O sete aparece {tuplo.count(7)}')
else:
    print('Não tem número 7!') 

if 5 in tuplo:
    encontrado == True
    print(f'O númaro 5 foi encontrado na posição {tuplo.index(5)}')
else:
    encontrado == False
    print('Não foi encontrado o número 5')    

for valor in  tuplo:
    if valor % 2 == 0:
        pares += (valor,)

if pares:        
    print(f'Os números pares são {pares}')
else:
    print('Não foram encontrados números pares!')    
