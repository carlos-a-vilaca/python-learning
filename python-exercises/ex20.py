'''Cria um programa que leia o nome completo de uma pessoa e mostre:
Nome em maiúsculas
Nome em minúsculas
Quantidade de letras (não contando os espaços)
Quantas letras tem o primeiro nome'''


nome = input('Insira seu nome: ')
espaço = nome.find(' ')# Uma variável para encontrar o espaço 


print(nome.upper())#Letras grandes
print(nome.lower())#Letras pequenas 
print(len(nome.replace(' ', '')))# Onde tem espaço ele troca para sem espaço 
print(len(nome[0:espaço]))# conta nome do indice 0 até ao espaço que é a variável que criei 