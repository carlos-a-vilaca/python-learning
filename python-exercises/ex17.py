#Cria um programa que peça o ano de nascimento do utilizador e o ano atual e que calcule a idade do utilizador.

ano_de_nascimento = int(input('Insira o seu ano de nascimento: '))
ano_atual = int(input('Insira o ano atual: '))
idade_utilizador = ano_atual - ano_de_nascimento

print(idade_utilizador)