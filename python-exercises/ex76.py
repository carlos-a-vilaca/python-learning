'''Cria um programa que tenha uma função que converta a temperatura de Celsius para Fahrenheit.'''

def converter_temperatura(celcios):
    fahrenheit = (celcios * 9/5) + 32
    return fahrenheit

temperatura_em_celcios = converter_temperatura(25)
print(temperatura_em_celcios)