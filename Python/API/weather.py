import os
import dotenv as de
from RestAPI import RestAPI

de.load_dotenv()

URL_API = os.getenv("URL_API_WEATHER")
API_KEY = os.getenv("API_WEATHER_KEY")

class Weather:
    def __init__(self, city: str) -> None:
        self.city = city
        self.url = f"{URL_API}?key={API_KEY}&q={self.city}&lang=pt"

    def get_weather(self, keys: str) -> dict:
        api = RestAPI(self.url)
        return api.get_data(keys)

def obterClima(cidade: str, keys: str) -> dict:
    clima = Weather(cidade)
    print(clima.get_weather(keys))
    
obterClima(cidade="Nilopolis", 
           keys=["location.name",
                 "location.region",
                 "location.country",
                 "current.temp_c",
                 "current.condition.text",
                 "current.humidity"])