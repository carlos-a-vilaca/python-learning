'''Cria um programa que pergunte a quantidade de km percorridos por um carro alugado e quantidade de dias que foi alugado.
Apresente o total a pagar sabendo que o carro custa 60€/dia e 0.456€/km.
Nota: "Atenção aos números decimais!"'''

km_percorridos = float(input('Insira quantos km percorreu: '))
dias_alugado = int(input('Insira quantos dias foi alugado: '))
total = km_percorridos * 0.456 + dias_alugado * 60

print(total)
