#Cria um programa que mostre os números pares entre 1 e 100.

for n in range(1, 101):
    if n % 2 == 0:
        print(f'Número par: {n}')