import requests
from utils import apikey

r = requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={apikey}')

if r.status_code != 200:
    raise Exception("Error en consulta de assets:{}".format(r.status_code))

lista_general = r.json()
lista_criptomonedas = []

for item in lista_general:
    if item["type_is_crypto"] == 1:
        lista_criptomonedas.append(item["asset_id"])

moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper()

while moneda_cripto != "" and moneda_cripto.isalpha():
    
    if moneda_cripto in lista_criptomonedas:
    
        r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={apikey}')
        resultado = r.json()

        if r.status_code == 200:
            print("{:,.2f} €".format(resultado["rate"]))
        else:
            print(resultado["error"])

    moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper()