#Em desenvolvimento
'''
from flask import Flask, request, render_template
import os
from mapquest import MapQuest

api_key = os.getenv("MAPQUEST_API_KEY", "NONE")
start = 'Nilópolis, RJ'
end = 'São Gonçalo, RJ'
url = f"http://www.mapquestapi.com/directions/v2/route?key={api_key}&from={start}&to={end}"
mq = MapQuest(api_key)
route = mq.directions(start, end)

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
'''