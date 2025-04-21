import requests as r

class RestAPI:
    def __init__(self, url: str, headers: dict = None) -> None:
        self.url = url
        self.headers = headers
    
    def getStructure(self, data: dict, paths: list):
        result = {}
        current = data
        if len(paths) > 0:
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
    
    def get_data(self, conteudo: str = None) -> dict:
        try:
            response = r.get(self.url, headers=self.headers,) if self.headers else r.get(self.url)
            if response.status_code == 200:
                retorno = response.json()
                return self.getStructure(retorno, conteudo) if conteudo else retorno
            else:
                return {f"error": {"status_code": response.status_code, "message": response.text}}
        except r.exceptions.RequestException as e:
            return {"error": str(e)}
    
    