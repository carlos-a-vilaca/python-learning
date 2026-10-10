'''Cria um programa que:
peça ao utilizador o nome, a idade e a cidade onde mora
apresente uma frase com todos os dados introduzidos
Ex: "Olá, o meu nome é António, tenho 32 anos e sou do Porto."
Nota: Todos os dados introduzidos devem ser tratados apenas como texto.'''

nome = input('Insira seu nome: ')
idade = int(input('Isira a sua idade: '))
cidade = input('Insira a sua cidade: ')

print (f'Olá, o seu nome é {nome}, tenho {idade} anos e sou do {cidade}.')