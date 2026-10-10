#Cria um programa que leia um número inteiro e diga se ele é ou não um número primo.
import os 
os.system('cls')#Limpa o ecrã da consola

#pede um número ao utilizador
numero = int(input('Insira um número: '))
#aqui assumo que o número é primo 
#só vai mudar para False se o meu loop ver que o numero não tem divisor 
primo = True 

#aqui testei todos os números entre 2 e numero -1 
#não pus a testar pelo 1 nem pelo próprio numero, porque esses
#dividem sempre qualquer número
#(tentei das primeiras vezes mas reparei que não me estava a ajudar em nada)
for i in range(2, numero):
    if numero % i == 0:
#se o resto da divisão é 0, encrontrámos um divisor 
#logo o número tem mais divisores além de 1 e ele próprio       
       primo = False
#não é primo

#depois do loop terminar tem esta uma comparação 
#para ver o que aconteceu a variável primo
#se nunca encontrar divisor a variável não vai mudar 
if primo == False:
    print('Não é número primo') 
else:
    print('É número primo')           