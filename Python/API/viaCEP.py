import os
import dotenv as de
from RestAPI import RestAPI

de.load_dotenv()

URL_API = os.getenv("URL_API_CEP")

class CEP:
    def __init__(self, cep: str) -> None:
        self.cep = str.replace(cep, "-", "").replace(".", "")
        self.url = f"{URL_API}{self.cep}/json/"

    def get_adrress(self, keys: str) -> dict:
        api = RestAPI(self.url)
        return api.get_data(keys)

def obterEndereco(cep: str, keys: str) -> dict:
    endereco = CEP(cep)
    print(endereco.get_adrress(keys))
    
obterEndereco(cep="01001000", 
           keys=["cep",
                 "logradouro",
                 "complemento",
                 "unidade",
                 "bairro",
                 "localidade",
                 "uf",
                 "estado",
                 "regiao",
                 "ibge",
                 "gia",
                 "ddd",
                 "siafi"])