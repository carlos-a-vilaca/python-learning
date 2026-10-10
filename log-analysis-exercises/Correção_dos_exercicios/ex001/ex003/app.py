from pathlib import Path
from datetime import datetime
import os

def assinatura(caminho: Path, titulo: str):
    with caminho.open('w', encoding='utf-8', errors='ignore') as file:
        file.write(titulo)
        file.write('NOME: Ricardo Mourão\n')
        file.write(f'DATA: {datetime.now()}\n')
        file.write('--- INICIO DOS RESULTADOS ---')
        print(f'Documento {caminho} assinado com sucesso.')
        input('Enter para continuar...')


def criar_pastas_meses(caminho: Path):

    tem_jan = False
    tem_fev = False
    tem_mar = False
    tem_abr = False
    tem_mai = False
    tem_jun = False
    tem_jul = False
    tem_ago = False
    tem_set = False
    tem_out = False
    tem_nov = False
    tem_dez = False


    with caminho.open('r', encoding='utf-8', errors='ignore') as file:
        for linha in file:
            if 'jan' in linha[0:15].lower():
                tem_jan = True
            elif 'feb' in linha[0:15].lower():
                tem_fev = True
            elif 'mar' in linha[0:15].lower():
                tem_mar = True
            elif 'apr' in linha[0:15].lower():
                tem_abr = True
            elif 'may' in linha[0:15].lower():
                tem_mai = True
            elif 'jun' in linha[0:15].lower():
                tem_jun = True
            elif 'jul' in linha[0:15].lower():
                tem_jul = True
            elif 'aug' in linha[0:15].lower():
                tem_ago = True
            elif 'sep' in linha[0:15].lower():
                tem_set = True
            elif 'oct' in linha[0:15].lower():
                tem_out = True
            elif 'nov' in linha[0:15].lower():
                tem_nov = True
            elif 'dec' in linha[0:15].lower():
                tem_dez = True


    if tem_jan:
        os.makedirs('Jan', exist_ok=True)
        print('Pasta Jan criada com sucesso.')
    if tem_fev:
        os.makedirs('Feb', exist_ok=True)
        print('Pasta Fev criada com sucesso.')

    if tem_mar:
        os.makedirs('Mar', exist_ok=True)
        print('Pasta Mar criada com sucesso.')

    if tem_abr:
        os.makedirs('Abr', exist_ok=True)
        print('Pasta Abr criada com sucesso.')

    if tem_mai:
        os.makedirs('Mai', exist_ok=True)
        print('Pasta Mai criada com sucesso.')

    if tem_jun:
        os.makedirs('Jun', exist_ok=True)
        print('Pasta Jun criada com sucesso.')

    if tem_jul:
        os.makedirs('Jul', exist_ok=True)
        print('Pasta Jul criada com sucesso.')

    if tem_ago:
        os.makedirs('Ago', exist_ok=True)
        print('Pasta Ago criada com sucesso.')

    if tem_set:
        os.makedirs('Set', exist_ok=True)
        print('Pasta Set criada com sucesso.')

    if tem_out:
        os.makedirs('Out', exist_ok=True)
        print('Pasta Out criada com sucesso.')

    if tem_nov:
        os.makedirs('Nov', exist_ok=True)
        print('Pasta Nov criada com sucesso.')

    if tem_dez:
        os.makedirs('Dec', exist_ok=True)
        print('Pasta Dez criada com sucesso.')


def estatisticas_gerais(logs: int, ssl: int, core: int, mpm: int, fatal: int, critical: int, caminho: Path):
    
    titulo = '--- Estatísticas Gerais ---\n'
    assinatura(caminho, titulo)

    with caminho.open('a', encoding='utf-8', errors='ignore') as file:
        file.write(f'Quantidade de logs: {logs}\n')
        file.write(f'Módulos SSL: {ssl}\n')
        file.write(f'Módulos CORE: {core}\n')
        file.write(f'Módulos MPM: {mpm}\n')
        file.write(f'Quantidade FATAL ERROR: {fatal}\n')
        file.write(f'Quantidade de CRITICAL ERROS: {critical}\n')
        file.write('--- FIM DA ANÁLISE ---')


def logs_modulos(caminho: Path):

    modulos = [
        'ssl:',
        'core:',
        'mpm_winnt:',
        'FATAL ERROR',
        'CRITICAL ERROR'
    ]

    meses = ['Dec', 'Jan', 'Feb']

    for mes in meses:
        qtd_logs = qtd_ssl = qtd_core = qtd_mpm = qtd_fatal = qtd_critical = 0

        ssl = []
        core = []
        mpm = []
        error_log = []

        with caminho.open('r', encoding='utf-8', errors='ignore') as file:
            for linha in file:
                if modulos[0] in linha:
                    ssl.append(linha)
                    qtd_ssl += 1

                elif modulos[1] in linha:
                    core.append(linha)
                    qtd_core += 1

                elif modulos[2] in linha:
                    mpm.append(linha)
                    qtd_mpm += 1

                if  modulos[3] in linha or modulos[4] in linha:
                    error_log.append(linha)

                    if modulos[3] in linha:
                        qtd_fatal += 1
                    elif modulos[4] in linha:
                        qtd_critical += 1

                qtd_logs += 1

        mapa_construcao_caminhos = 'ssl', 'core', 'mpm_winnt', 'error'

        for modulo in mapa_construcao_caminhos:
            caminho_mes = rf'{mes}/{modulo.replace(':', '')}.log'
            caminho_estatisticas = rf'{mes}/estatisticas.log'
            
            assinatura(Path(caminho_mes), modulo)

            estatisticas_gerais(qtd_logs, qtd_ssl, qtd_core, qtd_mpm, qtd_fatal, qtd_critical, Path(caminho_estatisticas))

            with Path(caminho_mes).open('a', encoding='utf-8', errors='ignore') as f:
                if modulo == 'ssl':
                    for log in ssl:
                        f.write(log)
                elif modulo == 'core':
                    for log in core:
                        f.write(log)
                elif modulo == 'mpm':
                    for log in mpm:
                        f.write(log)
                elif modulo == 'error':
                    for log in error_log:
                        f.write(log)
                else:
                    print(f'Não existe o mês {mes}')

            print(f'Log {mes}-{modulo} escrito com sucesso')


def main():
    INPUT_FILE = Path(r'logs\synthetic_error-SNAPSHOT-2.log')
    criar_pastas_meses(INPUT_FILE)
    logs_modulos(INPUT_FILE)

if __name__ ==  '__main__':
    main()