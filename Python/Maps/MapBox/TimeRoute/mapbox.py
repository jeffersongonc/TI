#https://docs.mapbox.com/api/navigation/directions/
#&snapping_include_closures=true -> para ajustar tráfego em estradas fechadas em tempo real
import os
import requests
import json
from datetime import datetime
import time
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

MAPBOX_APIKEY = os.environ.get("MAPBOX_APIKEY") or "NONE"
unidades = {"Unidades":[
            {"Unidade": "Hospital Barra D´Or", "Latitude": "-22.98314", "Longitude": "-43.36709"},
            {"Unidade": "Hospital Copa D´Or", "Latitude": "-22.96507", "Longitude": "-43.19044"},
            {"Unidade": "Hospital Rios D´Or", "Latitude": "-22.93646", "Longitude": "-43.33058"}]}

raiz = f'https://api.mapbox.com'
api = f'/directions'
versao = f'/v5'
profile = f'/mapbox/driving-traffic/'
origin = f'-43.22086,-22.90744;'#Quinta D'Or
alternatives = f'alternatives=true'
geometries = f'&geometries=geojson'
language = f'&language=pt-BR'
overview = f'&overview=simplified'
steps = f'&steps=false'

dt_now = datetime.now().strftime("%Y-%m-%dT%H:%M")
depart_at = f'&depart_at='+dt_now
access_token = f'&access_token={MAPBOX_APIKEY}'

for j in range(3):
    destination = unidades["Unidades"][j]["Longitude"] + ',' + unidades["Unidades"][j]["Latitude"] + '?'
    url = f''+raiz+api+versao+profile+origin+destination+alternatives+geometries+language+overview+steps+depart_at+access_token
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        for i in range(1):
            print(f'', unidades["Unidades"][j]["Unidade"], i+1, 'a rota - Tempo:', time.strftime("%H:%M:%S", time.gmtime(dados['routes'][i]['duration'])),
                   '| Distância', (dados['routes'][i]['distance']/1000.0), "Km - Coordenada:", destination)
    else:
        print(f"Error {response.status_code}: {response.reason}")