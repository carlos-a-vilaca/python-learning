from pathlib import Path
from datetime import datetime
'''
LOGS = Path(r"logs\synthetic_error.log")
OUTPUT = Path(r"logs\analise.log ")

data_hora = datetime.now()


with LOGS.open("r", encoding="utf-8", errors="ignore") as file:
    with OUTPUT.open("w", encoding="utf-8", errors="ignore") as output:
        output.write("=== Paragens Abruptas =======\n")
        output.write("===== Carlos Vilaça =========\n")
        output.write(f"DATA: {data_hora}\n")
        output.write("=============================\n")
        contador_de_logs = 0 
        for linha in file:
            if "exited abruptly" in linha:
                output.write(linha)
                contador_de_logs += 1 

        output.write(f"Quantidade de logs: {contador_de_logs}\n")
        output.write("=== FIM DOS RESULTADOS ===")'''

#Correção 

TERMO = "abruptly"
IMPUT_LOG = Path(f"logs\synthetic_error.log")
OUTPUT_LOG = Path(r"logs\logs_analisados.log")

agora = datetime.now()

TITULO = "--- PARAGENS ABRUPTAS ---\n"
ASSINATURA = f"Nome: Carlos Vilaça \nData: {agora}\n"


with IMPUT_LOG.open("r", encoding="utf-8", errors="ignore") as file:
    with OUTPUT_LOG.open("w", encoding="utf-8", errors="ignore") as output_file:
        output_file.write(TITULO)
        output_file.write(ASSINATURA)
        output_file.write("--- INICIO DOS RESULTADOS ---\n")
        
        documento = file.readlines()
        qtd_erros = 0
        for linha in documento:
            if TERMO in linha:
                qtd_erros += 1 

        output_file.write(f"Quantidade de linhas: {qtd_erros}\n")
    
        for linha in documento:
            if TERMO in linha.lower():
                output_file.write(linha)


        output_file.write("\n--- FIM DOS RESULTADOS ---")

print("analise com sucesso")