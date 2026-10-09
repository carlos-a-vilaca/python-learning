def calculadora(n1,n2,operacao):
    """
    Faz todas as operações consuante a escolha do 
    utilizador
    
    Parâmetros:
    n1(int) e n2(int) os dois números de cada operação
    operação (int) cada número conrresponde a cada opeção do menu
    
    Devolve:
    O resultado da operação escolhida
    """
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
    """
    Calcula a tabuada de um número 

    Parâmetros:
        n(int): o número a calcular a tabuada 
    
    Devolve: 
        a lista com todos os calculos da tabuada numa lista
    """
    lista_tabuada = []
    for i in range(1, 11):
        lista_tabuada.append(f'{i} x {n} = {i*n}')
    return lista_tabuada 
  
def numero_par_impar(n):
    """
    Verifica se o número é par ou ímpar 

    Parâmetros: 
        n(inteiro): o número a verificar 
    
    Devolve:
        Uma mensagem a indicar se o número é par ou não

    """
    if n % 2 == 0:
        return f'O {n} é par.'
    elif n % 2 == 1:
        return f'O {n} é ímpar.'        

def numeros_primos(n):
    """
    Verifica se o número é primo ou não 
    
    Parâmetros:
        n(inteiro): o número a verificar

    Devolve:
        Se o número for vai devolver verdadeiro
        Se não vai devolver falso
    
    """
    primo = True 
    for i in range(2, n):
        if n % i == 0:
            primo = False
    return primo 

def faturial(n):
    """
    Vai calcular o valor faturial do número

    Parâmetro: 
        n(inteiro): número a calcular 
    
    Devolve:
        O resultado do faturial desse número
    """
    contador = 1
    num_fatorial = 1 
    while contador <= n:
        resultado = num_fatorial * contador
        contador += 1
        num_fatorial = resultado 
    return resultado      
        