'''Cria um programa que leia 5 notas de um aluno e calcule a sua média.
>=9.5 passou
>8 e < 9.5 em recuperação
<8 reprova'''

nota1 = float(input('Insira uma nota: '))
nota2 = float(input('Insira uma nota: '))
nota3 = float(input('Insira uma nota: '))
nota4 = float(input('Insira uma nota: '))
nota5 = float(input('Insira uma nota: '))
media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

if media >= 9.5:
    print('Passou')
elif media > 8 and media < 9.5:
    print('Em Recuperação')
elif media < 8:
    print('Reprova')

    