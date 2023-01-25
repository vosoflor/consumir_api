from criptoexchange.models import ConsultaCoinAPI, Exchange, ModelError
from config import apikey
import pytest

def test_consultaCoinAPI():
    listas = ConsultaCoinAPI()
    assert isinstance(listas, ConsultaCoinAPI)
    listas.getCurrency(apikey)
    assert len(listas.cryptoCurrency) == 16156
    assert len(listas.otherCurrency) == 223

def test_getexchangeOk():
    exchange = Exchange("ETC")
    assert exchange.rate is None
    assert exchange.time == None
    exchange.getExchange(apikey)
    assert exchange.rate != None
    assert isinstance(exchange.time, str)

def test_getexchangeNotOk():
    exchange = Exchange("WRFS")
    with pytest.raises(ModelError):
        exchange.getExchange(apikey)
