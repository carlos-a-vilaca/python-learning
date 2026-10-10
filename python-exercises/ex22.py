'''Cria um programa que leia o primeiro e último nome de uma pessoa e exiba:
Mensagem de confirmação: "Olá nome, o seu registo está completo."
Email: "O seu email é primeira_letra_do_nome.apelido.edu@empresa.pt"

Ex email:
Alfredo Xavier
a.xavier.edu@empresa.pt'''

primeiro_nome = input('Insira o primeiro nome: ')
segundo_nome = input('Insira o segundo nome: ')

print(f'Olá {primeiro_nome.capitalize()}{segundo_nome.capitalize()}, o seu registo está completo.')
print(f'O seu email {primeiro_nome[0]}.{segundo_nome.lower()}.edu@empresa.pt')