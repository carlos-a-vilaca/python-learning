'''Cria um programa que leia vários números e os guarde numa lista.
Cria duas listas adicionais:

uma com os números pares
outra com os números ímpares
No final mostra todas as listas.'''
import os 
os.system('cls')

#duas listas uma para guadar os númaros pares e ímpares 
numeros_pares = []
numeros_impares = []

#enquanto for verdade vai fazer o que tem dentro 
while True:
    #o utilizador vai inserir um número 
    #em seguida vou avaliar se esse número é par se for vou dar
    #append na lista de pares e o mesmo para a lista de impares 
    numero = int(input('Insira um número: '))
    if numero % 2 == 0:
        numeros_pares.append(numero)
        print('Número par adicionado a lista')
    elif numero % 2 == 1:
        numeros_impares.append(numero)
        print('Números ímpar adicionado a lista')  
    #vou criar uma variável para o utlizador quiser parar de inserir números nas listas
    continuar = input('Quer continuar a inserir números (S/N) -->  ').upper()      
    #se escrever não vai parar o ciclo e vai escrever as listas 
    if continuar == 'N':
        print('Fim do programa')
        break


print(f'A lista de números pares inseridos: {numeros_pares}')
print(f'A lista de números ímpares inseridos: {numeros_impares}')    

