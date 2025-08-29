# Python Weather Predictor

This is a simple Python script that uses the OpenWeatherMap API to fetch and display current weather data for a specified city. It's a great starting project for learning how to work with external APIs in Python.

Features
Fetches current temperature, humidity, pressure, and wind speed.

Provides a simple command-line interface for user input.

Includes error handling for API request issues.

Prerequisites
To run this script, you will need to have Python installed on your system, along with the requests library.

You can install the requests library using pip:

pip install requests

Getting an API Key
Go to the OpenWeatherMap website and sign up for a free account.

Once your account is created, navigate to the API keys tab on your profile page.

Copy your unique API key. Note: It may take a few minutes for your API key to become active.

Usage
Open the weather_predictor.py file.

Find the line api_key = 'YOUR_API_KEY' and replace 'YOUR_API_KEY' with the API key you obtained from OpenWeatherMap.

Save the file.

Run the script from your terminal:

python weather_predictor.py

When prompted, enter the name of the city you want to get the weather for.

How it Works
The script makes an HTTP GET request to the OpenWeatherMap API. It sends the city name and your API key as parameters in the request URL. The API then returns a JSON object containing the weather data. The script parses this JSON data to extract and display key weather information in a human-readable format.
