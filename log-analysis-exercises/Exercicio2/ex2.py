from pathlib import Path
from datetime import datetime

'''
LOGS = Path(r"logs\synthetic_error.log")
OUTPUT = Path(r"logs\analise_modulos.txt")
FATAL_ERROR = Path(r"logs\resultado_fatal_error.log")

modulos = ["ssl:warn", "core:warn", "mpm_winnt:warm", "mpm_winnt:notice", "mpm_winnt:crit", "core:notice"]

contadores = {
    "ssl:warn":0,
    "core:warn":0,
    "mpm_winnt:warm":0,
    "mpm_winnt:notice":0,
    "mpm_winnt:crit":0,
    "core:notice":0
}

fatal_error = False
data_hora = datetime.now()
lista_fatal_error = []

with LOGS.open("r", encoding="utf-8", errors="ignore") as file:
    with OUTPUT.open("w", encoding="utf-8", errors="ignore") as output:
        #contadores 
        total_de_linha = 0 
        contador_fatal_error = 0
        
        for linha in file:
            total_de_linha += 1 
            if "FATAL ERROR" in linha:
                contador_fatal_error +=1
                fatal_error = True 
                lista_fatal_error.append(linha)
            for modulo in modulos:
                if modulo in linha:
                    contadores[modulo] += 1
        
        
        output.write("----- SEPARAÇÃO POR MÓDULOS -----\n")
        output.write("-----------------------------\n")
        output.write("------- Carlos Vilaça ------\n")
        output.write(f"DATA: {data_hora}\n")
        output.write("-----------------------------\n")

        for chave, valor in contadores.items():
            output.write(f"{chave}: {valor} \n")

        output.write(f"----------------------------\n")
        output.write(f"Existe algum FATAL ERROR: {fatal_error}\n")
        output.write(f"Quatidade FATAL ERROR: {contador_fatal_error}\n")
        output.write(f"Quantidade de linhas analisadas: {total_de_linha}\n")
        output.write("---- FIM DOS RESULTADOS ----")


with FATAL_ERROR.open("w", encoding="utf-8", errors="ignore") as ficheiro:

    ficheiro.write("----- FATAL ERROR -----\n")
    ficheiro.write("-----------------------------\n")
    ficheiro.write("------- Carlos Vilaça ------\n")
    ficheiro.write(f"Quantidade de logs: {len(lista_fatal_error)} \n")
    ficheiro.write(f"DATA: {data_hora}\n")
    ficheiro.write("----- LOGS -----\n")
    for linha in lista_fatal_error:
        ficheiro.write(linha)
    ficheiro.write("---- FIM DOS RESULTADOS ----")

'''

modulos = ["ssl:warn", "core:warn", "mpm_winnt:warm", "mpm_winnt:notice", "mpm_winnt:crit", "core:notice"]

NOME_DATA = f"NOME: Carlos Vilaça \nDATA: {datetime.now()}\n"
IMPUT_LOGS = Path("logs\synthetic_error.log")

c_ssl_warn = []
c_core_warn = []
c_mpm_winnt_warn = []
c_mpm_winnt_notice = []
c_mpm_winnt_crit = []
c_core_notice = []
fatal_errors = []

with IMPUT_LOGS.open("r", encoding="utf-8", errors="ignore") as file:
    documento_logs = file.readlines()

for linha in documento_logs:
    
    

    if "ssl:warn" in linha:
        c_ssl_warn.append(linha)

    if "core:warn" in linha:
        c_core_warn.append(linha) 

    if "mpm_winnt:warn" in linha:
        c_mpm_winnt_warn.append(linha)

    if "mpm_winnt:notice" in linha:
        c_mpm_winnt_notice.append(linha)

    if "mpm_winnt:crit" in linha:
        c_mpm_winnt_crit.append(linha)

    if "core:notice" in linha:
        c_core_notice.append(linha)

    if "FATAL ERROR" in linha:
        fatal_errors.append(linha)

    total_linhas = len(documento_logs)    

with Path(r"logs\ssl_warn.log").open("w", encoding="utf-8", errors="ignore") as file_ssl_warn:
    file_ssl_warn.write("--- SSL: WARN ---\n")
    file_ssl_warn.write(NOME_DATA)
    file_ssl_warn.write(f"Total de linhas: {len(c_ssl_warn)}\n")
    file_ssl_warn.write("--- INICIO DA ANÁLISE ---\n")
    file_ssl_warn.writelines(c_ssl_warn)
    file_ssl_warn.write("\n--- FIM DA ANÁLISE ---")
   

with Path(r"logs\core_warn.log").open("w", encoding="utf-8", errors="ignore") as file_core_warn:
    file_core_warn.write("--- CORE:WARN ---\n")
    file_core_warn.write(NOME_DATA)
    file_core_warn.write(f"Total de linhas: {len(c_core_warn)}\n")
    file_core_warn.write("--- INICIO DA ANÁLISE ---\n")
    file_core_warn.writelines(c_core_warn)
    file_core_warn.write("\n--- FIM DA ANÁLISE ---")


    
with Path(r"logs\c_mpm_winnt_warn.log").open("w", encoding="utf-8", errors="ignore") as file_mpm_winnt_warn:
    file_mpm_winnt_warn.write("--- MPM_WINNT:WARN ---\n")
    file_mpm_winnt_warn.write(NOME_DATA)
    file_mpm_winnt_warn.write(f"Total de linhas: {len(c_mpm_winnt_warn)}\n")
    file_mpm_winnt_warn.write("--- INICIO DA ANÁLISE ---\n")
    file_mpm_winnt_warn.writelines(c_mpm_winnt_warn)
    file_mpm_winnt_warn.write("\n--- FIM DA ANÁLISE ---")


with Path(r"logs\c_mpm_winnt_notice.log").open("w", encoding="utf-8", errors="ignore") as file_c_mpm_winnt_notice:
    file_c_mpm_winnt_notice.write("--- MPM_WINNT:NOTICE ---\n")
    file_c_mpm_winnt_notice.write(NOME_DATA)
    file_c_mpm_winnt_notice.write(f"Total de linhas: {len(c_mpm_winnt_notice)}\n")
    file_c_mpm_winnt_notice.write("--- INICIO DA ANÁLISE ---\n")
    file_c_mpm_winnt_notice.writelines(c_mpm_winnt_notice)
    file_c_mpm_winnt_notice.write("\n--- FIM DA ANÁLISE ---")
   

with Path(r"logs\c_mpm_winnt_crit.log").open("w", encoding="utf-8", errors="ignore") as file_c_mpm_winnt_crit:
    file_c_mpm_winnt_crit.write("--- MPM_WINNT:CRIT ---\n")
    file_c_mpm_winnt_crit.write(NOME_DATA)
    file_c_mpm_winnt_crit.write(f"Total de linhas: {len(c_mpm_winnt_crit)}\n")
    file_c_mpm_winnt_crit.write("--- INICIO DA ANÁLISE ---\n")
    file_c_mpm_winnt_crit.writelines(c_mpm_winnt_crit)
    file_c_mpm_winnt_crit.write("\n--- FIM DA ANÁLISE ---")
   


with Path(r"logs\c_core_notice.log").open("w", encoding="utf-8", errors="ignore") as file_c_core_notice:
    file_c_core_notice.write("--- CORE:NOTICE ---\n")
    file_c_core_notice.write(NOME_DATA)
    file_c_core_notice.write(f"Total de linhas: {len(c_core_notice)}\n")
    file_c_core_notice.write("--- INICIO DA ANÁLISE ---\n")
    file_c_core_notice.writelines(c_core_notice)
    file_c_core_notice.write("\n--- FIM DA ANÁLISE ---")

with Path(r"logs\fatal_error.log").open("w", encoding="utf-8", errors="ignore") as file_fatal_error:
    file_fatal_error.write("--- FATAL ERROR ---\n")
    file_fatal_error.write(f"{NOME_DATA}\n")
    file_fatal_error.write(f"Total de linhas: {len(fatal_errors)}\n")
    file_fatal_error.write("--- INICIO DA ANÁLISE ---\n")
    file_fatal_error.writelines(fatal_errors)
    file_fatal_error.write("\n--- FIM DA ANÁLISE ---")


with Path(r"logs\estatistica.txt").open("w", encoding="utf-8", errors="ignore") as file_estatistica:
    file_estatistica.write("--- Estatistica ---\n")    
    file_estatistica.write(f"{NOME_DATA}\n")
    file_estatistica.write("--- INICIO DA ANÁLISE ---\n")
    file_estatistica.write(f"ssl:warn: {len(c_ssl_warn)} linhas\n")
    file_estatistica.write(f"core:warn: {len(c_core_warn)} linhas\n")
    file_estatistica.write(f"mpm_winnt:warn: {len(c_mpm_winnt_warn)} linhas\n")
    file_estatistica.write(f"mpm_winnt:notice: {len(c_mpm_winnt_notice)} linhas\n")
    file_estatistica.write(f"mpm_winnt:crit: {len(c_mpm_winnt_crit)} linhas\n")
    file_estatistica.write(f"core:notice: {len(c_core_notice)} linhas\n")
    file_estatistica.write(f"Total de linhas: {total_linhas} linhas\n")
    file_estatistica.write("--- FIM DA ANÁLISE ---\n")