'''Cria um programa que tenha uma função que receba um número inteiro e mostre a tabuada desse número.'''

def tabuada(num):
    lista_num_tabuada = []
    for t in range(1, 11):
        resultado = f'{num} x {t} = {num * t}'
        lista_num_tabuada.append(resultado)  
    return lista_num_tabuada

for linha in tabuada(5):
    print(linha)

