import requests

class ConsultaCoinAPI:

    def __init__(self):
        self.currencyList = []
        self.cryptoCurrency = []
        self.otherCurrency = []
    
    def getCurrency(self, apikey):
        r = requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={apikey}')
        if r.status_code != 200:
            raise Exception("Error en consulta de assets:{}".format(r.status_code))        
        self.currencyList = r.json()
        for item in self.currencyList:
            if item["type_is_crypto"] == 1:
                self.cryptoCurrency.append(item["asset_id"])
            else:
                self.otherCurrency.append(item["asset_id"])

class Exchange:

    def __init__(self, currency) -> None:
        self.currency = currency
        self.rate = None
        self.time = None

    def getExchange(self, apikey):
        r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{currency}/EUR?apikey={apikey}')
        resultado = r.json()        
        if r.status_code == 200:
            self.rate = resultado["rate"]
            return self.rate
        else:
            return resultado["error"]