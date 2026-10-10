'''Cria um programa que simule uma contagem regressiva para a passagem de ano, de 10 até 0, com 1 segundo de pausa entre eles.
Nota: Utiliza o módulo time com a função time.sleep(1) .'''

import time

for c in range(10, 0, -1):
    print(c)
    time.sleep(1)
    