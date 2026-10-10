from datetime import datetime
from pathlib import Path

NOME_DATA = f'NOME: Ricardo Mourão\nDATA: {datetime.now()}\n'
INPUT_LOGS = Path('logs\synthetic_error.log')

c_ssl_warn = []
c_core_warn = []
c_mpm_winnt_warn = []
c_mpm_winnt_notice = []
c_mpm_winnt_crit = []
c_core_notice = []
fatal_errors = []
total_linhas = 0

with INPUT_LOGS.open('r', encoding='utf-8', errors='ignore') as file:
    documento_logs = file.readlines()

for linha in documento_logs:
    total_linhas += 1
    low = linha.lower()

    if '[ssl:warn]' in low:
        c_ssl_warn.append(low)

    if '[core:warn]' in low:
        c_core_warn.append(low)

    if '[mpm_winnt:warn]' in low:
        c_mpm_winnt_warn.append(low)

    if '[mpm_winnt:notice]' in low:
        c_mpm_winnt_notice.append(low)

    if '[mpm_winnt:crit]' in low:
        c_mpm_winnt_crit.append(low)

    if '[core:notice]' in low:
        c_core_notice.append(low)

    if 'fatal error' in low:
        fatal_errors.append(low)

    total_linhas = len(documento_logs)


with Path(r'ssl_warn.log').open('w', encoding='utf-8', errors='ignore') as file_ssl_warn:
    file_ssl_warn.write('--- SSL:WARN ---\n')
    file_ssl_warn.write(NOME_DATA)
    file_ssl_warn.write(f'--- INICIO DA ANÁLISE ---\n')
    file_ssl_warn.writelines(c_ssl_warn)
    file_ssl_warn.write(f'--- FIM DA ANÁLISE ---')


with Path(r'core_warn.log').open('w', encoding='utf-8', errors='ignore') as file_core_warn:
    file_core_warn.write('--- CORE:WARN ---\n')
    file_core_warn.write(NOME_DATA)
    file_core_warn.write(f'--- INICIO DA ANÁLISE ---\n')
    file_core_warn.writelines(c_core_warn)
    file_core_warn.write(f'--- FIM DA ANÁLISE ---')


with Path(r'mpm_winnt_warn.log').open('w', encoding='utf-8', errors='ignore') as file_mpm_winnt_warn:
    file_mpm_winnt_warn.write('--- MPM:WINNT_WARN ---\n')
    file_mpm_winnt_warn.write(NOME_DATA)
    file_mpm_winnt_warn.write(f'--- INICIO DA ANÁLISE ---\n')
    file_mpm_winnt_warn.writelines(c_mpm_winnt_warn)
    file_mpm_winnt_warn.write(f'--- FIM DA ANÁLISE ---')


with Path(r'mpm_winnt_notice.log').open('w', encoding='utf-8', errors='ignore') as file_mpm_winnt_notice:
    file_mpm_winnt_notice.write('--- MPM:WINNT_NOTICE ---\n')
    file_mpm_winnt_notice.write(NOME_DATA)
    file_mpm_winnt_notice.write(f'--- INICIO DA ANÁLISE ---\n')
    file_mpm_winnt_notice.writelines(c_mpm_winnt_notice)
    file_mpm_winnt_notice.write(f'--- FIM DA ANÁLISE ---')


with Path(r'mpm_winnt_crit.log').open('w', encoding='utf-8', errors='ignore') as file_mpm_winnt_crit:
    file_mpm_winnt_crit.write('--- MPM:WINNT_CRIT ---\n')
    file_mpm_winnt_crit.write(NOME_DATA)
    file_mpm_winnt_crit.write(f'--- INICIO DA ANÁLISE ---\n')
    file_mpm_winnt_crit.writelines(c_mpm_winnt_crit)
    file_mpm_winnt_crit.write(f'--- FIM DA ANÁLISE ---')

with Path(r'core_notice.log').open('w', encoding='utf-8', errors='ignore') as file_core_notice:
    file_core_notice.write('--- CORE:NOTICE ---\n')
    file_core_notice.write(NOME_DATA)
    file_core_notice.write(f'--- INICIO DA ANÁLISE ---\n')
    file_core_notice.writelines(c_core_notice)
    file_core_notice.write(f'--- FIM DA ANÁLISE ---')


with Path(r'fatal_error.log').open('w', encoding='utf-8', errors='ignore') as file_fatal:
    file_fatal.write('--- FATAL ERRORS ---\n')
    file_fatal.write(NOME_DATA)
    file_fatal.write(f'--- INICIO DA ANÁLISE ---\n')
    file_fatal.writelines(fatal_errors)
    file_fatal.write(f'--- FIM DA ANÁLISE ---')

with Path(r'estatisticas.txt').open('w', encoding='utf-8', errors='ignore') as file:
    file.write('--- ESTATÍSTICAS ---\n')
    file.write(NOME_DATA)

    file.write(f'\n[ssl:warn]: {len(c_ssl_warn)}')
    file.write(f'\n[core:warn]: {len(c_core_warn)}')
    file.write(f'\n[mpm_winnt:warn]: {len(c_mpm_winnt_warn)}')
    file.write(f'\n[mpm_winnt:notice]: {len(c_mpm_winnt_notice)}')
    file.write(f'\n[mpm_winnt:crit]: {len(c_mpm_winnt_crit)}')
    file.write(f'\n[core:notice]: {len(c_core_notice)}')
    file.write(f'\n[fatal error]: {len(fatal_errors)}')
    file.write(f'\nTotal linhas: {total_linhas}')


print('FINITO')