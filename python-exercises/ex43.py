'''Cria um programa que leia 3 valores e mostre o menu:

[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA'''

import os 
os.system('cls')

opcao = 0

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite um valor: '))
valor3 = int(input('Digite um valor: '))


while opcao != 5:
    print('\n[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA\n')

    opcao = int(input('Insira a sua opção: ').strip())

    if opcao == 1:
        print('SOMAR')
        soma = valor1 + valor2 + valor3
        print(f'A soma é: {soma}')
    elif opcao == 2:
        print('MULTIPLICAR')
        multiplicar = valor1 * valor2 * valor3
        
        #uma comparação para ver se os valores são maiores que os outros e se for guarda o valor em numero_maior 
    elif opcao == 3: 
        print('MAIOR')
        numero_maior = 0 

        if valor1 > valor2 and valor1 > valor3 :
                numero_maior = valor1 
        elif valor2 > valor1 and valor2 > valor3:
                numero_maior = valor2
        elif valor3 > valor1 and valor3 > valor3:
                numero_maior = valor3        
        print(f'O valor maior é: {numero_maior}')            

    elif opcao == 4:               
        print('NOVOS NÚMEROS')
        valor1 = int(input('Digite um valor: '))
        valor2 = int(input('Digite um valor: '))
        valor3 = int(input('Digite um valor: '))
        
    else:
        print('SAIR DO PROGRAMA')