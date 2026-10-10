'''Cria um programa que leia uma frase e mostre:
Quantas vezes aparece a letra "A"
A posição da primeira ocorrência
A posição da última ocorrência
Nota: Considera a frase sem distinguir maiúsculas de minúsculas.'''

frase = input('Insira uma frase: ')

print(frase.count('a'))
print(frase.find('a'))
print(frase.rfind('a'))