import os
import dotenv as de
import requests as r

de.load_dotenv()

URL_API = os.getenv("URL_API")
API_KEY = os.getenv("API_KEY")

class Weather:
    def __init__(self, city: str) -> None:
        self.city = city
        self.url = f"{URL_API}?key={API_KEY}&q={self.city}&lang=pt" #&units=metric"

    def get_weather(self) -> dict:
        try:
            response = r.get(self.url)
            if response.status_code == 200:
                retorno = {"Local": response.json()["location"]["name"],
                            "Estado": response.json()["location"]["region"],
                            "País": response.json()["location"]["country"],
                            "Temperatura": response.json()["current"]["temp_c"],
                            "Umidade": response.json()["current"]["humidity"],
                            "Condição": response.json()["current"]["condition"]["text"]}

                return retorno
            else:
                return {"error": "Cidade não encontrada"}
        except r.exceptions.RequestException as e:
            return {"error": str(e)}

clima = Weather("London")
tempo = clima.get_weather()
if "error" in tempo:
    print(f"Erro: {tempo["error"]}")
else:
    print(f'''
            Local: {tempo["Local"]} - Estado: {tempo["Estado"]} - País: {tempo["País"]}
            Temperatura: {tempo["Temperatura"]}
            Umidade: {tempo["Umidade"]}
            Condição: {tempo["Condição"]}
        ''')