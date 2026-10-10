'''Cria um programa que leia vários números inteiros e que termine apenas quando o utilizador escrever a opção para parar. No final
mostre quantos números foram inseridos e qual a soma entre eles.'''
import os 
os.system('cls')

soma = 0
numeros_inseridos = 0

#enquanto a condição for verdeira (que gera um ciclo infinito) vai pedir números ao utilizador 
while True:
    numero = int(input('Insira um número: '))
    #a soma vai gurdar o valor que tem 0 mais o valor do número inserido para a proxima volta somar o valor guardado 
    #+ o valor novo inserido pelo utilizador 
    soma = soma + numero
    #cada vez que o utilizador inserir um numero vai aumentar no contador +1 
    #para depois imprimir o valor guardado desta variável 
    numeros_inseridos += 1 
    #uma mesagem para o utilizador escrever para parar o ciclo 
    print('Se quiser carregue "0" para parar')
    
    #se o utilizzador introduzir 0 no input número 
    #para o ciclo 
    if numero == 0:
        break
#e por fim imprimo o resultado guardado nas minhas variáveis     
print(f'Foram inseridos: {numeros_inseridos} números')
print(f'A soma dos números é: {soma}')

    