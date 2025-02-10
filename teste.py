import requests

api_url= 'http://127.0.0.1:5000/clientes/'

def filtrar_clientes(api_url):
    try:
        estado = input('Digite o estado que deseja filtrar (ex: MG): ').strip().upper()
        response = requests.get(api_url)

        if response.status_code == 200:
            clientes = response.json()
            clientes_filtrados = []
            for cliente in clientes:
                if cliente['estado'] == estado:
                    clientes_filtrados.append(cliente)
        
            if clientes_filtrados:
                print(f"Cliente encontrado no estado '{estado}':\n")
                for cliente in clientes_filtrados:
                    print(f"ID : {cliente['id']}, Nome: {cliente['nome']}, Estado: {cliente['estado']}, Endereco : {cliente['endereco']}")
            else:
                print(f"\nNão foi encontrado cliente no estado '{estado}'")
        else:
            print(f"Erro ao acessar a API: {response.status_code}")
    except Exception as e:
        print(f"Erro: {e}")

filtrar_clientes(api_url)