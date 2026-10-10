'''Cria um programa onde o utilizador introduza 5 números numa lista.
Os valores devem ser inseridos já na posição correta, de forma crescente.
Não utilizar o método sort() .'''

import os 
os.system('cls')

lista = []


# ciclo que repete 5 vezes, para o utilizador inserir 5 números
for c in range(0, 5):
    numero = int(input('Insira um numero: '))
    # CASO 1: o número vai para o FIM da lista
    # -> c == 0: é o primeiro número, a lista está vazia, não há nada para comparar
    # -> numero > lista[-1]: o número é maior que o último elemento da lista,
    #    logo é o maior até agora e deve ficar no fim
    if c == 0 or numero > lista[-1]:
        lista.append(numero)#adiciona o número ao fim da lista 
        print('Adicionado no final da lista')
        # CASO 2: o número tem de ser inserido no MEIO (ou no início) da lista
    else:
        posicao = 0  # começa a procurar a partir da primeira posição (índice 0)

        #percorre a lista enquanto ainda houver posições por verificar
        while posicao < len(lista):
            # pergunta: o número que queremos inserir é menor ou igual
            # ao valor que já está guardado nesta posição?
            if numero <= lista[posicao]:
                # se sim, encontrámos o lugar certo!
                # insert() coloca o número aqui e empurra os restantes para a direita
                lista.insert(posicao, numero)
                print(f'O valor foi adicionado na posição {posicao}')
                break # já inserimos, não é preciso continuar a procurar
            posicao += 1    

print(f'Os numeros da lista são: {lista}')            

          
