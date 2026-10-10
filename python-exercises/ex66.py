'''Cria um simulador de crédito habitação simples que solicite nome, ano de nascimento, rendimentos mensais, despesas mensais,
montante do crédito e prazo em anos, guardando tudo num dicionário.
Calcule e acrescente ao dicionário: a idade, o remanescente após despesas, o valor mensal do crédito e se o crédito foi aprovado
(sempre que o remanescente seja superior ao valor mensal do crédito em 33%).'''

import os 
#importar a data 
from datetime import datetime
os.system('cls')

#dicionário
cliente = {}

#variável axiliar para receber o ano atual 
ano_atual = datetime.now().year 

#recolha de dados para adicionar ao dicionário 
cliente["Nome"] = input('Digite o seu nome: ')
cliente["Ano_de_nascimento"] = int(input('Digite seu ano de nascimento: '))
cliente["Rendimentos"] = float(input('Digite os seu rendimentos mensais: '))
cliente["Despesas"] = float(input('Digite as suas despesas: '))
cliente["Montante_do_credito"] = float(input('Digite o montante do crédito que deseja: '))
cliente["Prazo_em_anos"] = int(input('O prazo em anos: '))

#variável intermédia
prazo_em_meses = cliente["Prazo_em_anos"] * 12

#acrescentar ao dicionário 
cliente["Idade"] = ano_atual - cliente['Ano_de_nascimento'] 
cliente["Remanescente_apos_despesas"] = cliente["Rendimentos"] - cliente["Despesas"]
cliente["Valor_mensal"] = cliente['Montante_do_credito'] / prazo_em_meses




#aprovação do crédito 
calcular_33_por_cento = cliente["Valor_mensal"] * 0.33
valor_mensal_necessario = cliente["Valor_mensal"] - calcular_33_por_cento

if cliente['Remanescente_apos_despesas'] >= cliente['Valor_mensal'] * 1.33:
    cliente ['Aprovacao'] = 'Sim'

else:
    cliente['Aprovacao'] = 'Não'

print('-' * 50)
print('Dados do cliente')
print('-' * 50)

for chave in cliente:
    print(f'{chave}: {cliente[chave]}')