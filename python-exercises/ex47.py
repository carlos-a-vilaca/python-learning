'''Cria um programa que leia várias notas introduzidas pelo utilizador. No final mostre quantas notas foram inseridas, qual a média, e
qual a maior e a menor nota.'''
import os 
os.system('cls')

#contador para as notas inseridas começa em 1 por causa de já inserir uma vez aqui em cima
notas_inserida = 1
#aqui vai guardar cada nota inserida e a cada ciclo vai mudar a nota mas primeiro vou inserir a primeira nota 
nota = float(input('Insira a nota: '))
#a soma das notas vai receber a nota do primeiro ciclo para depois somar com a nova nota dentro do ciclo 
soma_das_notas = nota 
#a maior nota vai recer uma nota para a comparar com a menor nota para guardar a maior nota 
maior_nota = nota 
# #o mesmo para a menor nota 
menor_nota = nota


#enquanto a condição for verdadeira faz isto 
while True:
    #sair para quando o utilizador escrever sair do ciclo 
    sair = (input('Escreva sair para para de inserir press "ENTER" para continuar: ').lower())
    if sair == 'sair':
        break
    #vai inserir as notas a cada loop
    nota = float(input('Insira a nota: '))
    #o contador vai aumentar cada vez que fizer um ciclo (a cada vez que o utilizador por um nota) 
    notas_inserida += 1 
    #soma das nota vai somar a nota que guardar mais a nova nota inserida 
    soma_das_notas += nota

    #No primeiro ciclo ele vai pegar a primeira nota que inseri la em cima e 
    #vai comparar com a nota inserida dentro do ciclo 
    #E se for maior vai guarda sempre a nota maior na variável maior_nota 
    if nota > maior_nota:
        maior_nota = nota 
    #aqui a mesma coisa so que se for menor vai guardar sempre o número menor     
    if nota < menor_nota:
        menor_nota = nota   
    #no final calculo a media que são as soma das notas a cada ciclo a dividir pelo número de notas inseridas     
    media = soma_das_notas / notas_inserida    


print(f'\nForam inseridas {notas_inserida} notas')
print('A média:', media)
print('A menor nota:', menor_nota)
print('A maior nota:', maior_nota)


