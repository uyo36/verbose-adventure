import streamlit as st
import requests
from datetime import datetime

# --- CONFIG ---
API_KEY = "c4e37c7603120b4a7a7b00466033c83e"  # replace with secret in production

# --- FUNCTIONS ---
def get_weather(city_name):
    """Fetch current weather from OpenWeatherMap for a city in Nigeria."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"appid": API_KEY, "q": f"{city_name},NG", "units": "metric"}
    try:
        resp = requests.get(base_url, params=params, timeout=12)
        if resp.status_code == 200:
            d = resp.json()
            main = d.get("main", {})
            weather = (d.get("weather") or [{}])[0]
            wind = d.get("wind", {})
            return {
                "city": city_name,
                "condition": (weather.get("description") or "").capitalize(),
                "temperature": main.get("temp"),
                "feels_like": main.get("feels_like"),
                "humidity": main.get("humidity"),
                "pressure": main.get("pressure"),
                "wind_speed": wind.get("speed"),
                "raw": d
            }
        else:
            return {"error": f"OpenWeather error {resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}

# --- PAGE SETUP ---
st.set_page_config(page_title="Seplat Nigeria Weather Predictor", layout="centered")
st.title("Seplat Nigeria Weather Predictor")
st.caption("Search or select a Nigerian city to view current weather conditions. (Data from OpenWeatherMap)")

# --- CITIES LIST ---
cities_ng = [
    "Abakaliki","Abeokuta","Abuja","Ado-Ekiti","Akure","Asaba","Awka","Bauchi","Benin City",
    "Birnin Kebbi","Calabar","Damaturu","Dutse","Enugu","Gombe","Gusau","Ibadan","Ikeja",
    "Ilorin","Jalingo","Jos","Kaduna","Kano","Katsina","Lafia","Lagos","Lokoja",
    "Makurdi","Maiduguri","Minna","Oshogbo","Owerri","Port Harcourt","Sokoto","Umuahia",
    "Uyo","Yenagoa","Yola","Zaria","Ibeno"
]
cities_ng = sorted(set(cities_ng), key=lambda x: x.lower())

# --- SEARCHABLE SELECTBOX ---
# Streamlit's selectbox supports typing to jump/filter.
selected_city = st.selectbox("Search or select a city", options=cities_ng, index=cities_ng.index("Lagos"))

# --- ACTION ---
if st.button("Get Weather Report"):
    if not selected_city:
        st.warning("Please select a city first.")
    else:
        with st.spinner("Fetching weather..."):
            result = get_weather(selected_city)

        if "error" in result:
            st.error(result["error"])
        else:
            # Header info
            time_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
            st.subheader(f"Weather — {result['city']}")
            st.write(f"Condition: **{result['condition']}** • Updated: {time_str}")
            st.write("")  # spacing

            # Top row: temperature, humidity, wind
            tcol1, tcol2, tcol3 = st.columns(3)
            tcol1.metric(label="Temperature", value=f"{result['temperature']} °C", delta=f"Feels like {result['feels_like']} °C")
            tcol2.metric(label="Humidity", value=f"{result['humidity']} %")
            tcol3.metric(label="Wind Speed", value=f"{result['wind_speed']} m/s")

            # Bottom row: pressure and condition (large)
            bcol1, bcol2 = st.columns(2)
            bcol1.metric(label="Pressure", value=f"{result['pressure']} hPa")
            bcol2.write("### Condition")
            bcol2.write(f"**{result['condition']}**")

            # Optional: show raw JSON for debugging (collapsed)
            with st.expander("Raw API response (debug)"):
                st.json(result["raw"])

# Footer
st.write("---")
st.write("Powered by OpenWeatherMap API")
