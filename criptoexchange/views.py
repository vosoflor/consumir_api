def insertCurrency():
    cryptoCurrency = input("Ingrese una criptomoneda conocida: ").upper()
    return cryptoCurrency

def printCurrencyQuantity(allCurrencies):
    print(f'''Digital currencies are: {len(allCurrencies.cryptoCurrency)}\nNon digital currencies are: {len(allCurrencies.otherCurrency)}''')

def printExchangeRate(currencyExchange):
    print("{:,.2f} €".format(currencyExchange.rate))

def printError(error):
    print(error)