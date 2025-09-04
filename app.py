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

# 🏷️ Custom Banner Header
st.markdown(
    """
    <div style="background-color:#1E90FF;padding:15px;border-radius:10px;">
        <h1 style="color:white;text-align:center;">Seplat Nigeria Weather Predictor</h1>
        <p style="color:white;text-align:center;">Check real-time weather for safe travel across Nigerian states</p>
    </div>
    """,
    unsafe_allow_html=True
)

# 📍 All Nigerian States (36 + FCT)
nigerian_states = [
    "Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue",
    "Borno", "Cross River", "Delta", "Ebonyi", "Edo", "Ekiti", "Enugu", "Gombe",
    "Imo", "Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi", "Kogi", "Kwara",
    "Lagos", "Nasarawa", "Niger", "Ogun", "Ondo", "Osun", "Oyo", "Plateau",
    "Rivers", "Sokoto", "Taraba", "Yobe", "Zamfara", "FCT Abuja"
]

# 📌 Searchable Dropdown
selected_state = st.selectbox(
    "Select or search a Nigerian state:",
    sorted(nigerian_states),
    index=sorted(nigerian_states).index("Lagos")  # default Lagos
)

# 🚀 Show Weather
if st.button("Get Weather Report"):
    result = get_weather(selected_state)
    if "error" in result:
        st.error(result["error"])
    else:
        st.markdown(f"### ✅ Weather Report for {result['city']}")
        st.success(f"🌤️ {result['weather']}")

        # 🔹 Display metrics in a clean grid
        col1, col2, col3 = st.columns(3)
        col1.metric("Temperature 🌡️", f"{result['temperature']}°C", f"Feels like {result['feels_like']}°C")
        col2.metric("Humidity 💧", f"{result['humidity']}%")
        col3.metric("Wind Speed 💨", f"{result['wind_speed']} m/s")

        col4, col5 = st.columns(2)
        col4.metric("Pressure 🔽", f"{result['pressure']} hPa")
        col5.metric("Condition 🌤️", result['weather'])

# Footer
st.markdown("<hr><p style='text-align: center; color: gray;'>Powered by OpenWeatherMap API 🌍</p>", unsafe_allow_html=True)
