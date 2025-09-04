import streamlit as st
import requests

# ✅ Your OpenWeather API key
API_KEY = "c4e37c7603120b4a7a7b00466033c83e"

# 🌍 Function to fetch weather
def get_weather(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={API_KEY}&q={city_name}&units=metric"

    try:
        response = requests.get(complete_url)
        if response.status_code == 200:
            data = response.json()
            main_data = data.get('main')
            weather_data = data.get('weather')[0]
            wind_data = data.get('wind')

            return {
                "city": city_name.capitalize(),
                "weather": weather_data.get('description').capitalize(),
                "temperature": main_data.get('temp'),
                "feels_like": main_data.get('feels_like'),
                "humidity": main_data.get('humidity'),
                "pressure": main_data.get('pressure'),
                "wind_speed": wind_data.get('speed')
            }
        else:
            return {"error": f"Error fetching data: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

# 🎨 Page Config
st.set_page_config(page_title="Seplat Weather Predictor", page_icon="🌦", layout="centered")

# 🏷️ Title
st.title("Seplat Nigeria Weather Predictor")
st.write("Check real-time weather for safe travel across Nigerian states.")

# 📍 All Nigerian States (36 + FCT)
nigerian_states = [
    "Abia", "Adamawa",
