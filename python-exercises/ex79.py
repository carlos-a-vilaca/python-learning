'''Cria uma função que funcione como input() , mas que faça a validação para aceitar apenas um valor numérico.'''

def imput_numerico(frase):
    valor = input(frase)
    if not valor.isdigit():
        print('Só é aceite apenas um valor numérico!')

    

frase_validação = imput_numerico('Insira um número: ')


