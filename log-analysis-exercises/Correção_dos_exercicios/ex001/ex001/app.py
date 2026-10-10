'''
A partir do ficheiro de logs (synthetic_error.log), crie um
novo ficheiro que contenha um cabeçalho e as linhas
onde aparece a mensagem de que o processo “parou
abruptamente”.
O cabeçalho do ficheiro deverá ter:
1- Titulo do documento ex: “--- Paragens Abruptas ---”
2- Assinatura com nome e data da criação.
3- Quantas vezes foi encontrado log procurado.
4- Os logs deverão estar entre:
--- INICIO DOS RESULTADOS ---
--- FIM DOS RESULTADOS ---
'''

from pathlib import Path
from datetime import datetime

TERMO = 'abruptly'
INPUT_LOG = Path(r'logs\synthetic_error.log')
OUTPUT_LOG = Path(r'logs\logs-analisados.log')

agora = datetime.now()
TITULO = '--- PARAGENS ABRUPTAS ---\n'
ASSINATURA = f'Nome: Ricardo Mourão\nDATA: {agora}\n'

with INPUT_LOG.open(mode='r', encoding='utf-8', errors='ignore') as file:
    with OUTPUT_LOG.open(mode='w', encoding='utf-8', errors='ignore') as output_file:
        output_file.write(TITULO)
        output_file.write(ASSINATURA)
        
        documento = file.readlines()
        qtd_erros = 0

        for linha in documento:
            if TERMO in linha:
                qtd_erros += 1

        output_file.write(f'Quantidade erros: {qtd_erros}\n')

        output_file.write('--- INICIO DOS RESULTADOS ---\n\n')

        for linha in documento:
            if TERMO in linha.lower():
                output_file.write(linha)

        output_file.write('\n--- FIM DOS RESULTADOS ---')

print('Analise feita com sucesso!')