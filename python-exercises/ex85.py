'''Cria um código em Python que teste se o site do IEFP está acessível.
Requisitos:
usar o módulo requests (instalar com pip install requests )
verificar se o site responde e o código de status HTTP
tratar exceções:
ConnectionError → sem ligação à internet
Timeout → site não responde a tempo
RequestException → erro genérico de rede
apresentar mensagem clara sobre o estado do site
Códigos HTTP:
200-299 → sucesso
300-399 → redirecionamento
400-499 → erro do cliente
500-599 → erro do servidor'''

import requests 


   

def testar_site(url):
    try: 
        resposta = requests.get(url, timeout=5)
    except requests.exceptions.ConnectionError:
        print('Não há ligação ou o site não existe.') 
    except requests.exceptions.Timeout:
        print('O site demorou demasiado tempo a responder.')
    except requests.exceptions.RequestException:
        print('Ocorreu um erro genérico de rede')
    else:
        if 200 <= resposta.status_code <= 299:
            print('Sucesso')
        elif 300 <= resposta.status_code <= 399:
            print('Redirecionamento')
        elif 400 <= resposta.status_code <= 499:
            print('Erro do cliente')
        else: 
            print('Erro do servidor')    


testar_site('https://iefp.pt/')