'''Cria um programa que simule uma conversa, apresentando no ecrã mensagens como:

Olá, eu sou um BOT, como te chamas?
Dou-te as boas vindas "nome"
Que idade tens?
Fantástico, já tens "idade" anos. És de onde?
Uau, "cidade"?? Nunca visitei!

Nota: Este exercício tem como objetivo'''

nome = input('Olá, eu sou um BOT, como te chamas? ')
print(f'Dou-te as boas vindas {nome}')
idade = int(input('Que idade tens? '))
cidade = input(f'Fantástico, já tens {idade} anos. És de onde? ')
print(f'Uau, {cidade}?? Nunca visitei!')