#Cria um programa que leia um número qualquer e que mostre o seu fatorial.
import os 
os.system('cls')

contador = 1
numero = int(input('Insira um número: '))
faturial = 1

#enquanto o contador for menor ou igual ao número ele vai correr tipo de 0 até 5 até a condição estar falsa 
#depois a variável faturial recebe o numero do contador * o numero guardado no faturial 
# soma +1 no contador para no proximo ciclo ter +1 para fazer 1*2, 2*3, 6*4, 24*5 
#e o ciclo termina proque o contador já é igual a 5 (contador <=5 numero)

while contador <= numero:
      faturial = faturial * contador 
      resultado = faturial * contador 
      print(f'O número faturial é: {faturial} * {contador} = {resultado}')
      # print(f'O número faturial é: {numero_g} * {numero_g} = {contador}')
      contador += 1 


print(f'Fim')




