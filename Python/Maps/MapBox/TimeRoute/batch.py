import os
import requests
import json
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

MAPBOX_APIKEY = os.environ.get("MAPBOX_APIKEY") or "NONE"


# Substitua pelo seu token de acesso do Mapbox
access_token = MAPBOX_APIKEY

def batch_geocode(addresses, access_token):
    # URL da API de geocodificação em lote
    api_url = f'https://api.mapbox.com/geocoding/v5/mapbox.places-permanent/batch?access_token={access_token}'
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    
    # Formatar os endereços para o payload da requisição
    data = {
        'queries': [{'query': address} for address in addresses]
    }
    
    # Fazer a requisição POST
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.text}"

# Lista de endereços para geocodificação
addresses = [
    "1600 Pennsylvania Ave NW, Washington, DC 20500",
    "1 Infinite Loop, Cupertino, CA 95014",
    "350 5th Ave, New York, NY 10118"
]

result = batch_geocode(addresses, access_token)

# Processar e imprimir os resultados
if isinstance(result, dict) and 'results' in result:
    for i, res in enumerate(result['results']):
        if res['result']:
            coordinates = res['result'][0]['geometry']['coordinates']
            print(f"Endereço {i+1}: {addresses[i]}")
            print(f"Coordenadas: {coordinates[1]}, {coordinates[0]}")
        else:
            print(f"Endereço {i+1}: {addresses[i]}")
            print("Coordenadas: Não encontrado")
else:
    print(result)
