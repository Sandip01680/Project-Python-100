from flask import Flask, render_template_string, request, jsonify
import requests
from datetime import datetime
import json

app = Flask(__name__)

# API Configuration
API_KEY = "YOUR_API_KEY_HERE"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather App</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            background: white;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 500px;
            width: 100%;
        }
        
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
            font-size: 2.5em;
        }
        
        .search-box {
            display: flex;
            gap: 10px;
            margin-bottom: 30px;
        }
        
        input[type="text"] {
            flex: 1;
            padding: 15px;
            border: 2px solid #ddd;
            border-radius: 10px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        
        input[type="text"]:focus {
            outline: none;
            border-color: #667eea;
        }
        
        button {
            padding: 15px 30px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            cursor: pointer;
            transition: background 0.3s;
        }
        
        button:hover {
            background: #5568d3;
        }
        
        .weather-info {
            text-align: center;
            display: none;
        }
        
        .weather-info.show {
            display: block;
            animation: fadeIn 0.5s;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .location {
            font-size: 2em;
            color: #333;
            margin-bottom: 10px;
        }
        
        .temperature {
            font-size: 4em;
            color: #667eea;
            font-weight: bold;
            margin: 20px 0;
        }
        
        .description {
            font-size: 1.5em;
            color: #666;
            margin-bottom: 30px;
            text-transform: capitalize;
        }
        
        .details {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-top: 30px;
        }
        
        .detail-item {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 10px;
        }
        
        .detail-label {
            font-size: 0.9em;
            color: #666;
            margin-bottom: 5px;
        }
        
        .detail-value {
            font-size: 1.3em;
            color: #333;
            font-weight: bold;
        }
        
        .error {
            background: #fee;
            color: #c33;
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
            display: none;
        }
        
        .error.show {
            display: block;
        }
        
        .loading {
            text-align: center;
            color: #667eea;
            display: none;
            margin-top: 20px;
        }
        
        .loading.show {
            display: block;
        }
        
        .save-btn {
            margin-top: 20px;
            width: 100%;
            background: #27ae60;
        }
        
        .save-btn:hover {
            background: #229954;
        }
        
        .timestamp {
            text-align: center;
            color: #999;
            font-size: 0.9em;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌤️ Weather App</h1>
        
        <div class="search-box">
            <input type="text" id="cityInput" placeholder="Enter city name..." 
                   onkeypress="if(event.key==='Enter') searchWeather()">
            <button onclick="searchWeather()">Search</button>
        </div>
        
        <div class="loading" id="loading">
            <p>Loading weather data...</p>
        </div>
        
        <div class="error" id="error"></div>
        
        <div class="weather-info" id="weatherInfo">
            <div class="location" id="location"></div>
            <div class="temperature" id="temperature"></div>
            <div class="description" id="description"></div>
            
            <div class="details">
                <div class="detail-item">
                    <div class="detail-label">💧 Humidity</div>
                    <div class="detail-value" id="humidity"></div>
                </div>
                <div class="detail-item">
                    <div class="detail-label">💨 Wind Speed</div>
                    <div class="detail-value" id="wind"></div>
                </div>
                <div class="detail-item">
                    <div class="detail-label">🎚️ Pressure</div>
                    <div class="detail-value" id="pressure"></div>
                </div>
                <div class="detail-item">
                    <div class="detail-label">🌡️ Feels Like</div>
                    <div class="detail-value" id="feelsLike"></div>
                </div>
            </div>
            
            <div class="timestamp" id="timestamp"></div>
            <button class="save-btn" onclick="saveWeatherData()">Save Weather Data</button>
        </div>
    </div>
    
    <script>
        let currentWeatherData = null;
        
        async function searchWeather() {
            const city = document.getElementById('cityInput').value.trim();
            
            if (!city) {
                showError('Please enter a city name!');
                return;
            }
            
            showLoading();
            hideError();
            hideWeatherInfo();
            
            try {
                const response = await fetch(`/api/weather?city=${encodeURIComponent(city)}`);
                const data = await response.json();
                
                if (data.error) {
                    showError(data.error);
                } else {
                    currentWeatherData = data;
                    displayWeather(data);
                }
            } catch (error) {
                showError('Failed to fetch weather data. Please try again.');
            } finally {
                hideLoading();
            }
        }
        
        function displayWeather(data) {
            document.getElementById('location').textContent = `${data.name}, ${data.sys.country}`;
            document.getElementById('temperature').textContent = `${data.main.temp.toFixed(1)}°C`;
            document.getElementById('description').textContent = data.weather[0].description;
            document.getElementById('humidity').textContent = `${data.main.humidity}%`;
            document.getElementById('wind').textContent = `${data.wind.speed} m/s`;
            document.getElementById('pressure').textContent = `${data.main.pressure} hPa`;
            document.getElementById('feelsLike').textContent = `${data.main.feels_like.toFixed(1)}°C`;
            
            const now = new Date();
            document.getElementById('timestamp').textContent = 
                `Updated: ${now.toLocaleString()}`;
            
            showWeatherInfo();
        }
        
        async function saveWeatherData() {
            if (!currentWeatherData) return;
            
            try {
                const response = await fetch('/api/save', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(currentWeatherData)
                });
                
                const result = await response.json();
                
                if (result.success) {
                    alert(`Weather data saved to ${result.filename}`);
                } else {
                    alert('Failed to save weather data');
                }
            } catch (error) {
                alert('Error saving weather data');
            }
        }
        
        function showLoading() {
            document.getElementById('loading').classList.add('show');
        }
        
        function hideLoading() {
            document.getElementById('loading').classList.remove('show');
        }
        
        function showError(message) {
            const errorDiv = document.getElementById('error');
            errorDiv.textContent = message;
            errorDiv.classList.add('show');
        }
        
        function hideError() {
            document.getElementById('error').classList.remove('show');
        }
        
        function showWeatherInfo() {
            document.getElementById('weatherInfo').classList.add('show');
        }
        
        function hideWeatherInfo() {
            document.getElementById('weatherInfo').classList.remove('show');
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/weather')
def get_weather():
    city = request.args.get('city', '')
    
    if not city:
        return jsonify({'error': 'City name is required'}), 400
    
    if API_KEY == "YOUR_API_KEY_HERE":
        return jsonify({'error': 'Please configure your API key'}), 500
    
    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        
        response = requests.get(BASE_URL, params=params, timeout=10)
        
        if response.status_code == 200:
            return jsonify(response.json())
        elif response.status_code == 404:
            return jsonify({'error': f'City "{city}" not found'}), 404
        elif response.status_code == 401:
            return jsonify({'error': 'Invalid API key'}), 401
        else:
            return jsonify({'error': f'Error: {response.status_code}'}), response.status_code
            
    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Connection error. Check your internet.'}), 500
    except requests.exceptions.Timeout:
        return jsonify({'error': 'Request timed out'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/save', methods=['POST'])
def save_weather():
    try:
        data = request.json
        filename = f"weather_{data['name']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        
        return jsonify({'success': True, 'filename': filename})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    print("🌤️  Weather App starting...")
    print("📍 Open your browser and go to: http://127.0.0.1:5000")
    print("⌨️  Press Ctrl+C to stop the server")
    app.run(debug=True, port=5000)