import os
from pathlib import Path
from datetime import datetime

#escrever a assinatura 
def assinatura(caminho: Path, titulo:str):
    with caminho.open("w", encoding="utf-8", errors="ignore") as file:
        file.write(titulo)
        file.write("--- NOME: Carlos Vilaça ---\n")
        file.write(f"DATA: {datetime.now()}\n")
        file.write("--- INICIO DOS RESULTADOS ---\n")
        print(f"Documento {caminho} assinado com sucesso")
        input("Enter para continuar...")

#criar as pastas 
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

    with caminho.open("r", encoding="utf-8", errors="ignore") as file:
        for linha in file:
            if "jan" in linha[0:15].lower():
                tem_jan = True
            elif "feb" in linha[0:15].lower():
                tem_fev = True
            elif "mar" in linha[0:15].lower():
                tem_mar = True
            elif "apr" in linha[0:15].lower():
                tem_abr = True
            elif "jun" in linha[0:15].lower():
                tem_jun = True

            elif "jul" in linha[0:15].lower():
                tem_jul = True

            elif "aug" in linha[0:15].lower():
                tem_ago = True

            elif "sep" in linha[0:15].lower():
                tem_set = True

            elif "oct" in linha[0:15].lower():
                tem_out = True

            elif "nov" in linha[0:15].lower():
                tem_nov = True

            elif "dec" in linha[0:15].lower():
                tem_dez = True

    if tem_jan:
        os.makedirs("Jan", exist_ok=True)
        print("Pasta criada com sucesso.")

    if tem_fev:
        os.makedirs("Feb", exist_ok=True)
        print("Pasta criada com sucesso.")

    if tem_mar:
        os.makedirs("Mar", exist_ok=True)
        print("Pasta criada com sucesso")

    if tem_abr:
        os.makedirs("Abr", exist_ok=True)
        print("Pasta criada com sucesso")

    if tem_mai:
        os.makedirs("Mai", exist_ok=True)
        print("Pasta criada com sucesso")

    if tem_jun:
        os.makedirs("Jun", exist_ok=True)
        print("Pasta criada com sucesso")

    if tem_jul:
        os.makedirs("Jul", exist_ok=True)
        print("Pasta criada com sucesso")

    if tem_ago:
        os.makedirs("Ago", exist_ok=True)
        print("Pasta criada com sucesso")

    if tem_set:
        os.makedirs("Set", exist_ok=True)
        print("Pasta criada com sucesso")

    if tem_out:
        os.makedirs("Out", exist_ok=True)
        print("Pasta criada com sucesso")

    if tem_nov:
        os.makedirs("Nov", exist_ok=True)
        print("Pasta criada com sucesso")

    if tem_dez:
        os.makedirs("Dec", exist_ok=True)
        print("Pasta criada com sucesso.")


def estatisticas_gerais(logs: int, ssl: int, mpm: int, core: int, fatal: int, critical: int, caminho:Path):
    
    titulo = "--- Estatísticas Gerais ---\n"
    assinatura(caminho, titulo)

    with caminho.open("a", encoding="utf-8", errors="ignore") as file:
        file.write(f"Quantidade de logs: {logs}\n")
        file.write(f"Módulo SSL: {ssl}\n")
        file.write(f"Módulo CORE: {core}\n")    
        file.write(f"Módulo MPM: {mpm}\n")
        file.write(f"Quantidade fatal error: {fatal}\n")
        file.write(f"Quantidade de critical error: {critical}\n")
        file.write("--- FIM DA ANÁLISE ---")


def logs_modulos(caminho:Path):
    modulos = [
        "ssl:",
        "core:", 
        "mpm_winnt:",
        "FATAL ERROR", 
        "CRITICAL ERROR"
        
    ]

    meses = ["Dec", "Jan", "Feb"]

    for mes in meses: 
        qtd_logs = qtd_ssl = qtd_core = qtd_mpm = qtd_fatal = qtd_critical = 0

        ssl = []
        core = []
        mpm = []
        error_log = []

        with caminho.open("r", encoding="utf-8", errors="ignore") as file:
            for linha in file:

                if modulos[0] in linha:
                    ssl.append(linha)
                    qtd_ssl += 1 

                elif modulos[1] in linha:
                    core.append(linha)
                    qtd_core += 1 

                elif modulos[2] in linha:
                    qtd_mpm += 1 
                    mpm.append(linha)

                if modulos[3] in linha or modulos[4] in linha:
                    error_log.append(linha)

                    if modulos[3] in linha: 
                        qtd_fatal += 1
                    elif modulos[4] in linha:
                        qtd_critical += 1 

                qtd_logs += 1 

        mapa_contrucao_caminhos = "ssl", "core", "mpm_winnt", "error"

        for modulo in mapa_contrucao_caminhos:
            caminho_mes = rf"{mes}/{modulo.replace(":","")}.log"
            caminho_estatisticas = rf"{mes}/estatistica.log"

            assinatura(Path(caminho_mes), modulo)

            estatisticas_gerais(qtd_logs, qtd_ssl, qtd_core, qtd_mpm, qtd_fatal,qtd_fatal, Path(caminho_estatisticas))

            with Path(caminho_mes).open("a", encoding="utf-8", errors="ignore") as f:
                if modulo == "ssl":
                    for log in ssl:
                        f.write(log)
                    f.write("--- FIM DA ANÁLISE ---")
                elif modulo == "core":
                    for log in core:
                        f.write(log)
                    f.write("--- FIM DA ANÁLISE ---")
                elif modulo == "mpm_winnt":
                    for log in mpm:
                        f.write(log)
                    f.write("--- FIM DA ANÁLISE ---")
                elif modulo == "error":
                    for log in error_log:
                        f.write(log)
                    f.write("--- FIM DA ANÁLISE ---")
                else:
                    print(f"Não existe o mês {mes}")

            print(f"Log {mes}-{modulo} escrito com sucesso")


def main():
    IMPUT_FILE = Path(r"logs\synthetic_error-SNAPSHOT-2.log")
    criar_pastas_meses(IMPUT_FILE)
    logs_modulos(IMPUT_FILE)

    

    


if __name__ == "__main__":
    main()