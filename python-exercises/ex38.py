#Cria um programa que leia uma frase qualquer e diga se é um palíndromo, desconsiderando os espaços.
#Ex: Anotaram a data da maratona
import os 
os.system('cls')
frase = input('Insira uma frase: ').lower()
frase = frase.replace(' ', '')
#aqui ja digo que a palavra é palíndromo 
palindromo = True 

#frase = 'osso'

#o for percorre o índice da frase, um a um
for i in range(len(frase)):
      #frase [i] a contar do inicio(primeiro índice)
      #frase[len(frase)-1-i] para contar do fim 
      #e comparo se o primeiro indice ou letra é diferente da última 
      if frase[i] != frase[len(frase)-1-i]:
         #se for diferenete vai mudar a variável que estava a verdadeira para false 
         palindromo = False
#a palavra quando entrar no ciclo e ver que é verdadeira vai dar True e vai printar a mensagem 
#se não for vai para o else
if palindromo == True:
    print('É palíndromo')
else:
    print('Não é')     


#print(frase[::-1])
#print(frase)
#-3-2-1
# o s o 
# 0 1 2
