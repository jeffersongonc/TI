import os
import requests
import json
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

MAPBOX_APIKEY = os.environ.get("MAPBOX_APIKEY") or "NONE"

# Substitua pelo seu token de acesso do Mapbox
access_token = MAPBOX_APIKEY

def get_distances_matrix(origins, destinations, access_token):
    # Formate a URL da API Matrix do Mapbox
    coordinates = ";".join([f"{lon},{lat}" for lon, lat in origins + destinations])
    #api_url = f"https://api.mapbox.com/directions-matrix/v1/mapbox/walking/{coordinates}?access_token={access_token}"
    #print(api_url)    
    # Calcule os índices de origem e destino
    sources = ";".join(map(str, range(len(origins))))
    destinations_indices = ";".join(map(str, range(len(origins), len(origins) + len(destinations))))
    
    # Adicione os índices aos parâmetros da URL
    #api_url += f"&sources={sources}&destinations={destinations_indices}"
    api_url = f"https://api.mapbox.com/directions-matrix/v1/mapbox/walking/{coordinates}?annotations=distance&sources={sources}&destinations={destinations_indices}&access_token={access_token}"
#    print(api_url)
    response = requests.get(api_url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.text}"

# Coordenadas da origem (longitude, latitude)
origins = [(-43.17986,-22.92186)]  # Exemplo: Hospital Glória D'Or

# Coordenadas dos destinos (longitude, latitude)
destinations = [
    (-43.22089,-22.90589),  # Exemplo: Hospital Quinta D'Dor - 6,4
    (-43.23238,-22.91334),  # Exemplo: Hospital Badim - 7,8
    (-43.19048,-22.96261)   # Exemplo: Hospital Copa D'Or - 6,6
]

result = get_distances_matrix(origins, destinations, access_token)

#print(result['destinations'])
#for i, destination in enumerate(result['destinations']):
#        print(f"Origem: {result['sources'][0]['name']} - Destino: {destination['name']} - Distância em metros: {result['distances'][0][i]}")


if isinstance(result, dict) and 'distances' in result:
    distances = result['distances'][0]  # Distâncias da primeira origem para todos os destinos
    for i, distance in enumerate(distances):
        print(f"Distância para destino {i+1}: {distance} metros")
else:
    print(result)
