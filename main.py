from flask import Flask
from flask import render_template, request
import requests

from urls import *

app = Flask(__name__)

params = {
    'api_key': API_KEY
}

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/lolearn")
def lolearn():
    response = requests.get(CHAMPIONS_API_URL).json()['data']
    
    return render_template('lolearn.html', champions=response)

@app.route("/lolearn/<name>")
def champion(name):
    print(name)
    FULL_URL = f'{CHAMPION_API_URL}/{name}.json'
    champion_data = requests.get(FULL_URL).json()['data'][f'{name}']

    return render_template('champion.html', champion=champion_data)
