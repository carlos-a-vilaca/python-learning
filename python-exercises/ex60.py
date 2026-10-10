'''Cria um programa onde o utilizador possa introduzir uma expressão matemática com parênteses.
O programa deve indicar se os parênteses estão corretos ou não.

((a+b)-c(c/d) → errado
((a+b)-c(c/d)) → correto'''


import os
os.system('cls')


expressao = input('Insira a expressão: ')
lista_da_expressao = []

# percorre a expressão, símbolo a símbolo (carácter a carácter)
for simbolo in expressao:
    #se  encontrár um parêntese a abrir -> guardar na lista 
    if simbolo == '(':
        lista_da_expressao.append('(')
     #se encontrár um parêntese a fechar    
    elif simbolo == ')':
        #adicinar a lista 
        #logo a seguir verificas se o tamanho é > 0
        if len(lista_da_expressao) > 0:
            lista_da_expressao.pop()# e removes o último elemento
        else:
            lista_da_expressao.append(')') 
            break 

## no fim, se a lista estiver vazia, assume-se que está tudo bem fechado
if len(lista_da_expressao) == 0:
    print('A sua expressão está correta')
else:
    print('A sua expressão está errada')               

