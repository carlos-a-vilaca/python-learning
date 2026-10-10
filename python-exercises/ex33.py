#Cria um programa que leia 5 números inteiros e mostre a soma desses números.

soma = 0 

for i in range(5):
    numero = int(input('Insira um número: '))
    soma = numero + soma # A soma recebe o numero do utilizador + a soma neste caso 0 e guada o valor na soma para o proximo loop.
print('Soma total:', soma)