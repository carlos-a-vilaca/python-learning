from pathlib import Path
from datetime import datetime

agora = datetime.now()

LOGS = Path(r'logs\synthetic_error.log')
OUTPUT = Path(r'logs\analisado.log')

with LOGS.open(mode='r', encoding='utf-8', errors='ignore') as file:
    with OUTPUT.open(mode='w', encoding='utf-8', errors='ignore') as outputfile:
        outputfile.write('--- SSL:WARN ---\n')
        outputfile.write('-------------------\n')
        outputfile.write('Nome: Ricardo Mourão\n')
        outputfile.write(f'Data: {agora}\n')
        outputfile.write('-------------------\n')
        outputfile.write('--- INICIO DOS RESULTADOS ---\n')

        for linha in file:
            if 'ssl:warn' in linha:
                outputfile.write(linha)

        outputfile.write('--- FIM DOS RESULTADOS ---')