from criptoexchange.models import ConsultaCoinAPI
from config import apikey

def test_consultaCoinAPI():
    listas = ConsultaCoinAPI()
    assert isinstance(listas, ConsultaCoinAPI)
    listas.getCurrency(apikey)
    assert len(listas.cryptoCurrecy) == 16156
    assert len(listas.otherCurrency) == 223