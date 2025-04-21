import os
import dotenv as de
from RestAPI import RestAPI

de.load_dotenv()

URL_API = os.getenv("URL_API_CNPJ")

class CNPJ:
    def __init__(self, cnpj: str) -> None:
        self.cnpj = cnpj.replace("-", "").replace(".", "").replace("/", "")
        self.url = f"{URL_API}{self.cnpj}"
    
    def get_CNPJ(self, keys: str = None) -> dict:
        api = RestAPI(self.url)
        return api.get_data(keys) if keys else api.get_data()

def obterCNPJ(cnpj: str, keys: str = None) -> dict:
    dados = CNPJ(cnpj=cnpj)
    print(dados.get_CNPJ())
    
obterCNPJ(cnpj="00.000.000/0001-91")