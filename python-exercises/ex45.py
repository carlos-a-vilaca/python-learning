#Cria um programa que leia um número N inteiro qualquer e mostre os N primeiros elementos de uma sequência de Fibonacci.
import os
os.system('cls')


# Pede ao utilizador quantos termos quer ver e converte o texto introduzido para inteiro
n = int(input('Quantos termos da sequência queres ver? ').strip())

# Se o número introduzido for menor ou igual a 0, não faz sentido (não há termos para mostrar)
if n <= 0:
    print('Inserir um número inteiro positivo')

# Caso o utilizador só queira ver 1 termo
elif n == 1:
    # O primeiro termo da sequência de Fibonacci é sempre 0
    print('0')

# Para todos os outros casos (n >= 2)
else:
     # t1 e t2 guardam os dois primeiros termos da sequência (0 e 1)
    t1 = 0
    t2 = 1 
    # Mostra logo os dois primeiros termos, sem mudar de linha (end='')
    print(f'{t1} -> {t2}', end='')
    # count regista quantos termos já foram mostrados (já mostrámos 2: t1 e t2)
    count = 2 

     # Repete enquanto não tivermos mostrado os n termos pedidos
    while count < n:
         # Calcula o próximo termo somando os dois anteriores
        t3 = t1 + t2 
         # Mostra o novo termo, continuando na mesma linha
        print(f' --> {t3}', end='')

        # "Desliza" a janela: t1 passa a ser o antigo t2, t2 passa a ser o novo termo
        t1 = t2
        t2 = t3
         # Incrementa o contador, porque acabámos de mostrar mais um termo
        count += 1 
    print(' --> FIM')        