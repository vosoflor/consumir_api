from criptoexchange.models import *
from config import apikey

allCurrencies = ConsultaCoinAPI()
allCurrencies.getCurrency(apikey)

print(f"Digital currencies are: {len(allCurrencies.cryptoCurrency)}\n\
    Non digital currencies are: {len(allCurrencies.otherCurrency)}")

cryptoCurrency = input("Ingrese una criptomoneda conocida: ").upper()

while cryptoCurrency != "" and cryptoCurrency.isalpha():
    if cryptoCurrency in allCurrencies.cryptoCurrency:
        currencyExchange = Exchange(cryptoCurrency)
        try:
            currencyExchange.getExchange(apikey)
            print("{:,.2f} €".format(currencyExchange.rate))
        except ModelError as error:
            print(error)

    cryptoCurrency = input("Ingrese una criptomoneda conocida: ").upper()
