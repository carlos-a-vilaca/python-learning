# CAMINHO ABSOLUTO
#"C:\Users\ricar\OneDrive\Formação\IEFP\26.0464 - Técnicoa Especialista em Cibersegurança (SFP PortoPresencial)\01480Ri - Analisar evidências de ataques cibernéticos\1-manipulacao-ficheiros\1-escrita.py"


# CAMINHO RELATIVO
# 1-escrita.py

# MANIPULAÇÃO DE FICHEIROS
# 1º LUGAR -> ESPECIFICO O CAMINHO DO FICHEIRO
# 2º LUGAR -> CRIO UMA VARIAVEL QUE REPRESENTA ESSE FICHEIRO

# IMPORTAÇÃO DA BIBLIOTECA PARA DAR FUNCIONALIDADES À VARIÁVEL QUE REPRESENTA O CAMINHO
from pathlib import Path
# DEFINIR O CAMINHO DO FICHEIRO
LOGS = Path(r'logs\teste.log')
# MODOS DE ABERTURA
# 1 - w - Write / Escrita
# 2 - a - Append / Acrescenta
# 3 - r - Read / Leitura
with LOGS.open(mode='w', encoding='utf-8', errors='ignore') as ficheiro:
    frase = input('Digite uma frase: ')
    ficheiro.write(frase)
print('Ficheiro escrito com sucesso.')