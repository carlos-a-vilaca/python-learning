'''Cria um programa que leia 5 números e os guarde numa lista.
No final mostra:

o maior valor e a sua posição
o menor valor e a sua posição'''
import os 
os.system('cls')


lista = []

# numeros = (int(input('Insira o 1º núemero: ')),
#             int(input('Insira o 2º núemero: ')),
#             int(input('Insira o 3º núemero: ')),
#             int(input('Insira o 4º núemero: ')),
#             int(input('Insira o 5º núemero: ')))


for i in range(5):
    numero = int(input('Insia um número: '))
    lista.append(numero)

# for n in lista:
#     numero_maior = lista[0]
#     numero_menor = lista[0]
#     if numero >= numero_maior:
#         numero_maior = numero
#     elif numero <= numero_menor:
#         numero_menor = numero
#     else: 
#         print('Não é válido')

print(lista)        
print(f'O maior valor é {max(lista)} e a sua posição {lista.index(max(lista))}')
print(f'O menor valor é {min(lista)} e a sua posição {lista.index(min(lista))}')            


'''lista_numeros = []


for n in range(6):
    numero = int(input('Insira o número que quer gurdar na lista: '))
    lista_numeros.append(numero)


print(lista_numeros)
print(f'O valor maior é {max(lista_numeros)} e a sua posição {lista_numeros.index(max(lista_numeros))}')
print(f'O número menor é {min(lista_numeros)} e a sua posição {lista_numeros.index(min(lista_numeros))}')'''