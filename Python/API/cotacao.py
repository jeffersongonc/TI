import os
import dotenv as de
from RestAPI import RestAPI

de.load_dotenv()

URL_API = os.getenv("URL_API_COTACAO")

class Cotacao:
    def __init__(self, moeda: str, data: str) -> None:
        self.moeda = moeda
        self.data = data
        self.url = f"{URL_API}?@codigoMoeda='{self.moeda}'&@dataCotacao='{self.data}'&$format=json&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao,tipoBoletim"
    
    def get_cotacao(self, keys: str) -> dict:
        api = RestAPI(self.url)
        return api.get_data(keys)

def obterCotacao(moeda: str, data: str, keys: str) -> dict:
    cotacao = Cotacao(moeda=moeda, data=data)
    print(cotacao.get_cotacao(keys))
    
obterCotacao(moeda="EUR", data="04-17-2025", 
           keys=["value"])