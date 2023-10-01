import requests
import sys

def fetch_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error: Unable to fetch data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    return None

def dividir_data(data_string):
    try:
        partes = data_string.split('/')
        dia = int(partes[0])
        mes = int(partes[1])
        ano = int(partes[2])
        return dia, mes, ano
    except ValueError:
        print("Error: Data invalida ou string")
        return None, None, None

def imprimir(json_data):
    dados = []
    for item in json_data:
        data_completa = item["data"]
        dia,mes,ano = dividir_data(data_completa)
        valor = item["valor"]
        dados.append({"data": data_completa,"dia": dia,"mes": mes,"ano": ano, "valor": float(valor)})
    for item in dados:
        print(f"Data: {item['data']}, Dia: {item['dia']}, Mes: {item['mes']}, Ano: {item['ano']}, Valor: {item['valor']}")


url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10841/dados?formato=json"
json_data = fetch_data(url)

if json_data is None:
    sys.exit("Não encontrou informações.")

imprimir(json_data)

