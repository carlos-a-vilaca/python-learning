'''Desenvolve um programa que simule uma calculadora interativa.
Requisitos:
exibir um menu com várias opções
executar a funcionalidade escolhida
voltar ao menu após cada operação
usar tratamento de exceções para entradas inválidas
todas as funções num módulo bem estruturado e documentado'''

def Calculadora(n1,n2,operacao):
    if operacao == 1:
        return n1 + n2
    elif operacao == 2:
        return n1 - n2
    elif operacao == 3:
        return n1 * n2 
    elif operacao == 4:
        try: 
            return n1 / n2
        except ZeroDivisionError:
            return 'Erro: Não é possivel dividir por zero' 
  
def tabuada(n):
    lista_tabuada = []
    for i in range(1, 11):
        lista_tabuada.append(f'{i} x {n} = {i*n}')
    return lista_tabuada 
  
def numero_par_impar(n):
    if n % 2 == 0:
        return f'O {n} é par.'
    elif n % 2 == 1:
        return f'O {n} é ímpar.'        

def numeros_primos(n):
    primo = True 
    for i in range(2, n):
        if n % i == 0:
            primo = False
    return primo 

def faturial(n):
    contador = 1
    num_faturial = 1 
    while contador <= n:
        resultado = num_faturial * contador
        contador += 1
        num_faturial = resultado 
    return resultado      
        



while True:
    menu = ('--- Calculadora Interativa ---\n'
            ' 1-Calculadora\n '
            '2-Tabuada\n '
            '3-Par ou ímapar\n'
            ' 4-Números primos\n '
            '5-Factorial\n'
            ' 6-Sair')    
    
    print(menu)
    print()
    try:
        opcao = int(input('Insira a sua opção: ').strip())
    except ValueError:
        print('Erro: Insira o número conrrespondente a seguinte opção.')
    else:
    #opção 1 Calculadora 
        if opcao == 1:
            print(' 1-SOMAR\n',
                '2-SUBTRAÇÃO\n',
                '3-MULTIPLIACAÇÃO\n',
                '4-DIVISÃO')
            print()

            try:
                num1 = int(input('Insira o primeiro número: ').strip())
                num2 = int(input('Insira o segundo número: ').strip())
                opecao_calculadora = int(input('Insira a operação: ')) 
            except ValueError:
                print('Erro: O valor inserido não é um número inteiro.')
            else:    
                print(f'O resultado: {Calculadora(num1,num2,opecao_calculadora)}')
                
        #opcão tabuada
        elif opcao == 2:
            try: 
                numero_tabuada = int(input('Insira o número: ').strip())
            except ValueError:
                print('Erro: O valor inserido não é um número inteiro.')    

            else:
                for n in tabuada(numero_tabuada):
                    print(n)  

        #opção par ou ímpar    
        elif opcao == 3:
            try:
                n_par_impar = int(input('Insira o número: ').strip()) 
            except ValueError:
                print('Erro: O valor inserido não é um número inteiro.')
            else:
                print(numero_par_impar(n_par_impar))
        #opção números primos
        elif opcao == 4:
            try:
                numero_primo = int(input('Insira o número: ').strip())
            except ValueError:
                print('Erro: O valor inserido não é um número inteiro.') 
            else: 
                if numeros_primos(numero_primo) == True:
                    print(f'O número {numero_primo} é primo.')
                elif numeros_primos(numero_primo) == False:
                    print(f'O número {numero_primo} não é primo')    
        #opção factorial
        elif opcao == 5:
            try: 
                numero_faturial = int(input('Insira um número: ').strip())
            except ValueError:
                print('Erro: O valor inserido não é um número inteiro.')
            else:
                print(faturial(numero_faturial))    

        #opção sair
        elif opcao == 6:
            break
        else:
            print('Erro: Opeção inválida!') 







# def somar(n1, n2):
#     return n1 + n2

# num1 = int(input('Insira um número: '))
# num2 = int(input('Insira um número: '))

# print(somar(num1, num2u))