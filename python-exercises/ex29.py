'''Cria o seguinte menu e executa a ação correspondente:

--- Calculadora ---
[ 1 ] – Tabuada
[ 2 ] – Calculadora
[ 3 ] – Números Pares
[ 4 ] – Sair'''
import os 
os.system('cls')


print('''--- Calculadora ---
[ 1 ] – Tabuada
[ 2 ] – Calculadora
[ 3 ] – Números Pares
[ 4 ] – Sair''')
opcao = int(input('Insira a sua opção: '))


if opcao == 1:
    print ('--- Tabuada ---')
    numero_tabuada = int(input('Insira um número: '))

    print(f'{numero_tabuada} * 1 = {numero_tabuada * 1}')
    print(f'{numero_tabuada} * 2 = {numero_tabuada * 2}')
    print(f'{numero_tabuada} * 3 = {numero_tabuada * 3}')
    print(f'{numero_tabuada} * 4 = {numero_tabuada * 4}')
    print(f'{numero_tabuada} * 5 = {numero_tabuada * 5}')
    print(f'{numero_tabuada} * 6 = {numero_tabuada * 6}')
    print(f'{numero_tabuada} * 7 = {numero_tabuada * 7}')
    print(f'{numero_tabuada} * 8 = {numero_tabuada * 8}')
    print(f'{numero_tabuada} * 9 = {numero_tabuada * 9}')
    print(f'{numero_tabuada} * 10 = {numero_tabuada * 10}')

if opcao == 2:
    print('--- Calculadora ---')

    numero1 = int(input('Insira um número: '))
    numero2 = int(input('Insira um número: '))
    operador = input('Insira um oprador: ')

    if operador == '+':
        print(numero1 + numero2)
    elif operador == '-':
        print(numero1 - numero2)
    elif operador == '*':
        print(numero1 * numero2) 
    elif operador == '%':
        print(numero1 % numero2)       
    elif numero1 == 0 or numero2 == 0:
        print ('Erro não é possível dividir por: 0')   
    else:
        print(numero1 / numero2)       

if opcao == 3:
    print('-- Números Pares --')
    numeros_pares = int(input('Insira um número: '))

    if numeros_pares % 2 == 0:
        print('Número Par')
    else:
        print('Não é número par')    

if opcao == 4:
    os.system('cls')










