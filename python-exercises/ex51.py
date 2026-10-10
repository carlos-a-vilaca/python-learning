#Cria um programa que leia um número entre 0 e 20 introduzido pelo utilizador e mostre o número por extenso.

numero = ("um", "dois","três", "quatro","cinco", "seis","sete", "oito",
            "nove", "dez","onze", "doze","treze", "quatorze","quinze", "dezasseis",
            "dezasete", "dezoito","dezanove", "vinte")



utilizador_numero = int(input('Insira um número entre 0 e 20: '))

print(f'O numero que escolheu foi', numero[utilizador_numero - 1])