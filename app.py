from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your actual API key
API_KEY = 'f11795494d42d4ef0902d261209e3e8c'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            response = requests.get(BASE_URL, params={
                'q': city,
                'appid': API_KEY,
                'units': 'metric'
            })
            if response.status_code == 200:
                weather_data = response.json()
            else:
                weather_data = {'message': 'City not found'}
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
