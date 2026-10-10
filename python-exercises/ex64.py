'''Cria um programa que leia o nome e a média de um aluno, calculando a sua situação, tudo dentro de um dicionário.
No final mostre todo o conteúdo do dicionário.

Média >= 9,5 → Aprovado
Média < 9,5 → Reprovado'''

#dicionário 
aluno_media = {}

for aluno in range(1):
    aluno_media["nome"] = input('Insira o nome do aluno: ')
    aluno_media["media"] = float(input('Insira a média do aluno: '))

# print(aluno_media['nome'], aluno_media['média'])

if aluno_media['media'] >= 9.5:
    print('Aprovado')
else:
    aluno_media['media'] <= 9.5
    print('Reprovado')  

print(aluno_media)