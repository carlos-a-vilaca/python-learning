import time
from datetime import datetime

agora = datetime.now()

def menu():
    '''
        Apresenta o menu principal da aplicação.

    Permite ao utilizador escolher entre:
    - Consultar o catálogo
    - Adicionar produtos ao carrinho
    - Visualizar o carrinho
    - Finalizar a compra
    - Sair da aplicação
    
    '''
    print("1. Ver catálugo\n"
        "2. Adicionar produto ao carrinho\n"
        "3. Ver carrinho\n"
        "4. Finalizar compra\n"
        "0. Sair")  

def titulo(texto, largura=46):
    '''
    Gera um título formatado e centrado.

    Parâmetros:
        texto (str): Texto a apresentar no título.
        largura (int): Largura total da linha.

    Retorna:
        str: Título centrado e preenchido com '='.
    '''
    return f" {texto} ".center(largura, "=")     
 
def ver_catalogo(produtos):
    '''
    Gera uma representação formatada do catálogo.

    Percorre todos os produtos existentes e cria
    uma lista de strings contendo:

    - ID do produto
    - Nome
    - Preço
    - Stock disponível

    Parâmetros:
        produtos (list): Lista de produtos.

    Retorna:
        list: Lista formatada para apresentação.
    
    '''
    catalogo = []    
    for produto in produtos:
        catalogo.append(f"ID:{produto["id"]:<2} Nome:{produto["nome"]:<20} Preço: {produto["preco"]:>3.2f}€  Stock:{produto["stock"]:>4}")
    return catalogo

def adicionar_ao_carrinho(produtos, carrinho, id, quantidade): 
    '''
        Adiciona um produto ao carrinho de compras.

    Verifica:
    - Se o ID existe.
    - Se existe stock suficiente.

    Caso a operação seja válida:
    - Atualiza o stock.
    - Calcula o subtotal.
    - Adiciona o produto ao carrinho.

    Retorna:
        list: Carrinho atualizado.
    
    '''

    for produto in produtos:
        if id == produto["id"]:
            if quantidade <= produto["stock"]:
                produto["stock"] = produto["stock"] - quantidade
                subtotal = produto["preco"] * quantidade
                carrinho.append({"id": produto["id"],
                                        "nome": produto["nome"],
                                        "preco": produto["preco"],
                                        "quantidade": quantidade,
                                        "subtotal": subtotal})
                        
                print(f"Adicionou {quantidade} unidades de {produto["nome"]}")
                print(f"O stock restante: {produto["stock"]}")
                print()
            else:
                print("Não existe stock suficiente.")  
    return carrinho     

def calcular_desconto(subtotal):
    '''
    Calcula o desconto aplicado à compra.

    Regras:
    - Até 10€: sem desconto.
    - Entre 10€ e 30€: 5%.
    - Superior a 30€: 10%.

    Parâmetros:
        subtotal (float): Valor da compra antes do desconto.

    Retorna:
        tuple:
            total (float) - valor final.
            desconto (float) - valor descontado.
    '''
    if subtotal <= 10:
        desconto = 0 
    elif subtotal <= 30:
        desconto = subtotal * 0.05
    else:
        desconto = subtotal * 0.10
    total = subtotal - desconto 

    return total, desconto

def ver_carrinho(carrinho):
            '''
            Apresenta o conteúdo do carrinho.

            Se o carrinho estiver vazio, informa o utilizador.

            Caso existam produtos:
            - Mostra cada produto.
            - Mostra quantidades.
            - Mostra subtotais.
            - Calcula e apresenta o valor total da compra.
            '''
            total = 0
            if len(carrinho) == 0:
                print("O seu carrinho está vazio!")  
            else:
                for campo in carrinho:
                    total += campo["subtotal"]
                    print(f"{campo["nome"]:<19} x {campo["quantidade"]:>2} Subtutal: {campo["subtotal"]:10.2f}€") 
                    time.sleep(1)
            print()
            print(f"Total: {total:.2f}")


def imprimir_talao(carrinho, total, total_com_desconto, desconto, agora):
    '''
    Gera e apresenta o talão final da compra.

    O talão inclui:
    - Lista de produtos comprados.
    - Quantidades.
    - Subtotais.
    - Valor total.
    - Desconto aplicado.
    - Total a pagar.
    - Data e hora da compra.

    Parâmetros:
        carrinho (list): Produtos adquiridos.
        total (float): Valor antes do desconto.
        total_com_desconto (float): Valor final.
        desconto (float): Desconto aplicado.
        agora (datetime): Data e hora da compra.
    
    '''
    for produto in carrinho:
        linha = (f"{produto["nome"]:<25} x {produto["quantidade"]:>5} {produto["subtotal"]:10.2f}€")
        print(linha)
        time.sleep(1)

    print("-"*46)

    print(f"{"Subtutal":<25}{total:>20.2f}€")
    print(f"{"Desconto":<25}{desconto:>20.2f}€")
    print(f"{"TOTAL A PAGAR:":<25} {total_com_desconto:>19.2f}€")

    print()
    print(f"Data: {agora.strftime("%d/%m/%Y  %H:%M")}")
    print("="*46)
    print()
    print()
    print("Obrigado pela sua visita!") 

