import os
import time
import Mini_Mercado
from datetime import datetime
os.system("cls")

produtos = [{"id": 1, "nome": "Leite", "preco": 0.89, "stock": 10},
            {"id": 2, "nome": "Pão", "preco": 0.25, "stock": 20},
            {"id": 3, "nome": "Arroz", "preco": 1.10, "stock": 15},
            {"id": 4, "nome": "Massa", "preco": 0.95, "stock": 12},
            {"id": 5, "nome": "Café", "preco": 3.20, "stock": 8},
            {"id": 6, "nome": "Feijão", "preco": 0.95, "stock": 30},
            {"id": 7, "nome": "Azeite", "preco": 3.20, "stock": 19},
            {"id": 8, "nome": "Manteiga", "preco": 2.30, "stock": 11},
            {"id": 9, "nome": "Sal", "preco": 0.90, "stock": 21},
            {"id": 10, "nome": "Chocolate", "preco":2.25, "stock": 15}]


#variáveis axiliares 
carrinho_de_compras = []


while True:
    #menu 
    print(Mini_Mercado.titulo("MINI-MERCADO"))
    Mini_Mercado.menu()
    print('='*46)
    #opção do menu
    try:
        opcao = int(input("O que deseja --> ")) 
        print()
        print()
    except ValueError:
        print("Erro: Só é a inteiro.")
    except KeyboardInterrupt:
        print("Erro: ")
    except NameError:
        print("Erro: ")
    #Ver catálugo  
    if opcao == 1:
        print("="*18, "CATÁLOGO", "="*18)
        catalugo = Mini_Mercado.ver_catalogo(produtos) 
        for linha in catalugo:
            print(linha) 
            time.sleep(1)
        print("="*46)           

    #Adicionar produto ao carrinho       
    elif opcao == 2:
        print(Mini_Mercado.titulo("ADICIONAR PRODUTO"))
        try:
            id_produto = int(input("ID do produto: "))  
            quantidade = int(input("Quantidade: "))
            print()
            print()
        except ValueError:
            print("Erro: O valor inserido não é (int) inteiro.")
        except KeyboardInterrupt:
            print("Erro: O interrupeção pelo utilizador")
        else:  
            carrinho_de_compras = Mini_Mercado.adicionar_ao_carrinho(produtos,carrinho_de_compras, id_produto, quantidade)         
            
    #ver carrinho de compras    
    elif opcao == 3:
        print(Mini_Mercado.titulo("VER CARRINHO DE COMPRAS"))
        Mini_Mercado.ver_carrinho(carrinho_de_compras)
          
    #talão de compra 
    elif opcao == 4:
        total = 0 
        for campo in carrinho_de_compras:
            total += campo["subtotal"]

        #  verifica se tem algo dentro de carrinho de compras  
        if len(carrinho_de_compras) == 0:
            print("Tem que adicionar produtos, Não tem produtos no carrinho para finalizar a compra.")
            print("Obrigado pela sua atenção!")
        else: 
            confirmar = input("Deseja confirmar a compra [S/N]: ").upper().strip() 
            print()
            print()
            total_com_desconto, desconto = Mini_Mercado.calcular_desconto(total)

            if confirmar == "S":
                print(Mini_Mercado.titulo("TALÃO DE COMPRA")) 
                print('-'*46)
                Mini_Mercado.imprimir_talao(carrinho_de_compras, total, total_com_desconto, desconto, datetime.now())
                # Ao fim de finalizar a compra limpa o carrinho de compras  
                carrinho_de_compras.clear()
            else:
                print('Compra cancelada!')      
                pass     

    elif opcao == 0:
        print("A SAIR...")
        print("MUITO OBRIGADO!")
        time.sleep(1)
        break  
    
    else:
        print("Opeção inválida!")