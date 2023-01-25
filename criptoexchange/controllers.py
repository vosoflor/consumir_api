from criptoexchange.models import *
from config import apikey
from criptoexchange.views import *

class CryptoExchangeController():

    def executeProgram(self):

        allCurrencies = ConsultaCoinAPI()
        allCurrencies.getCurrency(apikey)

        printCurrencyQuantity(allCurrencies)

        cryptoCurrency = insertCurrency()

        while cryptoCurrency != "" and cryptoCurrency.isalpha():
            if cryptoCurrency in allCurrencies.cryptoCurrency:
                currencyExchange = Exchange(cryptoCurrency)
                try:
                    currencyExchange.getExchange(apikey)
                    printExchangeRate(currencyExchange)
                except ModelError as error:
                    printError(error)

            cryptoCurrency = insertCurrency()