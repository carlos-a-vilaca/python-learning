'''Cria um programa que tenha um tuplo com nomes de jogos e os seus preços em sequência.
No final, mostra uma listagem organizada em formato de tabela.'''

jogos = ('Forza', 50.25, 'GTA 6', 100.00, 'Call Of Dutty', 80.00, 'Minicraft', 20.00)


print('--------------------------------------------')
print('JOGOS                                  PREÇO')
print('--------------------------------------------')
for i in range(0, len(jogos), 2):
    print(f'{jogos[i]:30}{jogos[i + 1]:14}')
print('--------------------------------------------')

# nome = 'Forza'
# preco = 80.00

# print(f'{nome:30}{preco:30}')