import os
import calculadora
os.system('cls')


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
        opcao = int(input('Insira a sua opção: '))
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
                num1 = int(input('Insira o primeiro número: '))
                num2 = int(input('Insira o segundo número: '))
                opecao_calculadora = int(input('Insira a operação: ')) 
            except ValueError:
                print('Erro: O valor inserido não é um número inteiro.')
            else:    
                print(f'O resultado é {calculadora.calculadora(num1,num2,opecao_calculadora)}')
                
        #opcão tabuada
        elif opcao == 2:
            try: 
                numero_tabuada = int(input('Insira o número: '))
            except ValueError:
                print('Erro: O valor inserido não é um número inteiro.')    

            else:
                for n in calculadora.tabuada(numero_tabuada):
                    print(n)  

        #opção par ou ímpar    
        elif opcao == 3:
            try:
                n_par_impar = int(input('Insira o número: ')) 
            except ValueError:
                print('Erro: O valor inserido não é um número inteiro.')
            else:
                print(calculadora.numero_par_impar(n_par_impar))
        #opção números primos
        elif opcao == 4:
            try:
                numero = int(input('Insira o número: '))
            except ValueError:
                print('Erro: O valor inserido não é um número inteiro.') 
            else: 
                if calculadora.numeros_primos(numero) == True:
                    print(f'O número {numero} é primo.')
                elif calculadora.numeros_primos(numero) == False:
                    print(f'O número {numero} não é primo')    
        #opção factorial
        elif opcao == 5:
            try: 
                numero_fatorial = int(input('Insira um número: '))
            except ValueError:
                print('Erro: O valor inserido não é um número inteiro.')
            else:
                print(calculadora.faturial(numero_fatorial))    

        #opção sair
        elif opcao == 6:
            break
        else:
            print('Erro: Opção inválida!') 