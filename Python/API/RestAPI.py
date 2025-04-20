import requests as r

class RestAPI:
    def __init__(self, url: str) -> None:
        self.url = url
    
    def getStructure(self, data: dict, paths: list):
        result = {}
        for path in paths:
            keys = path.split(".")
            current = data
            for key in keys:
                if isinstance(current, dict) and key in current:
                    current = current[key]
                else:
                    current = f"[Erro: Caminho '{path}' não encontrado no retorno da API]"
                    break
            result[keys[-1]] = current
        return result
    
    def get_data(self, conteudo: str) -> dict:
        try:
            response = r.get(self.url)
            if response.status_code == 200:
                retorno = response.json()
                return self.getStructure(retorno, conteudo)
            else:
                return {"error": "Cidade não encontrada"}
        except r.exceptions.RequestException as e:
            return {"error": str(e)}