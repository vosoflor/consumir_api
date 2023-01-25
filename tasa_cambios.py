import requests
from config import apikey

moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper()

# Ejercicio 4: Cómo controlo que si el input está vacío no se realice consulta
while moneda_cripto != "" and moneda_cripto.isalpha():

    r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={apikey}')

    #print(r.status_code) # Código 200 significa correcto
    #print(r.text)

    resultado = r.json() # guarda el resultado del json como diccionario en python

    # Ejercicio 1: Capturar resultados correctos
    if r.status_code == 200:
        # Ejercicio 3: cómo formatear el valor rate incluyendo , para miles . para decimales y €
        print("{:,.2f} €".format(resultado["rate"])) # se utiliza clave del diccionario creado para la tasa de cambio de la cripto seleccionada
    # Ejercicio 2: Capturar errores
    else:
        print(resultado["error"]) # clave del diccionario creado para el error obtenido
    
    moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper()
