'''Cria um programa que leia a velocidade de um veículo e simule um radar de velocidade.
Regras:
Velocidade > 80 km/h → Multado
Velocidade ≤ 80 km/h → Não multado
Multa: 100€ + 7€ por cada km/h acima de 80 km/h'''

velocidade_km = float(input('Isira a velucidade: '))
multa = 100 + 7 * (velocidade_km - 80)# calcula a velocidade inserida e tira 80 para calcular o resto que falta.

if velocidade_km > 80:
     print(f'Multado, a multa é de: {multa}')

elif velocidade_km <= 80:
     print('Não Multado')