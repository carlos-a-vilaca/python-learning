'''Cria um programa que peça ao utilizador dois números e divida o primeiro pelo segundo.
Utiliza o tratamento de exceções para:
casos em que o segundo número é zero
quando a entrada não é um número válido
O programa deve apresentar mensagens claras, permitir nova tentativa e mostrar o resultado quando bem-sucedido.'''
import os
os.system('cls')

while True: 
    try:
        num1 = int(input('Insira o primeiro número: '))
        num2 = int(input('Insira o segundo núemero: '))
        resultado = num1 / num2

    except ValueError:
        print(f'Erro: Só aceita valores inteiros.')
        continue

    except ZeroDivisionError:
        print('Erro: Divisão por zero.')
    else: 
        print(f'O resultado: {resultado}')

    opcao = input('Continuar? [S/N] ').strip().upper()         
     
    if opcao == 'N':
        break

