from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'your_weather_API_key'  # Replace with your weather API key

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            response = requests.get(f'http://api.openweathermap.org/data/2.5/weather',
                                    params={'q': city, 'appid': API_KEY, 'units': 'metric'})
            weather = response.json()
    return render_template('index.html', weather=weather)

@app.route('/about')
def about():
    return render_template('about.html')


    
