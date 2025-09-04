import os
import streamlit as st
import requests

# Retrieve API key from Streamlit secrets (preferred) or environment variable (local testing)
if "API_KEY" in st.secrets:
    API_KEY = st.secrets["API_KEY"]
else:
    API_KEY = os.environ.get("OPENWEATHER_API_KEY", "")

if not API_KEY:
    st.warning("OpenWeather API key not found. Locally, set environment variable OPENWEATHER_API_KEY. "
               "On Streamlit Cloud, add API_KEY in Secrets. The app will still load but API calls will fail.")

def get_weather(city_query: str):
    """Fetch current weather from OpenWeather for a city in Nigeria."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"appid": API_KEY, "q": f"{city_query},NG", "units": "metric"}
    try:
        resp = requests.get(base_url, params=params, timeout=15)
        if resp.status_code == 200:
            d = resp.json()
            main = d.get("main", {})
            weather = (d.get("weather") or [{}])[0]
            wind = d.get("wind", {})
            return {
                "city": city_query,
                "condition": (weather.get("description") or "").capitalize(),
                "temperature": main.get("temp"),
                "feels_like": main.get("feels_like"),
                "humidity": main.get("humidity"),
                "pressure": main.get("pressure"),
                "wind_speed": wind.get("speed"),
            }
        else:
            # Return server message with code for easier debugging
            return {"error": f"OpenWeather error {resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}

# UI setup
st.set_page_config(page_title="Seplat Nigeria Weather Predictor", layout="centered")

st.markdown(
    """
    <div style="text-align:center; padding:18px; background:#1e90ff; color:#fff; 
                border-radius:12px; font-weight:600;">
        <span style="font-size:30px; line-height:1;">Seplat Nigeria Weather Predictor</span>
        <div style="font-size:14px; margin-top:6px; opacity:0.95;">
            Type or choose a Nigerian city to view current conditions.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
st.write("")

# Nigerian cities list (capitals + add Ibeno). Add more if you want.
cities_ng = [
    "Abakaliki","Abeokuta","Abuja","Ado-Ekiti","Akure","Asaba","Awka","Bauchi","Benin City",
    "Birnin Kebbi","Calabar","Damaturu","Dutse","Ebonyi","Enugu","Gombe","Gusau","Ibadan",
    "Ikeja","Ilorin","Jalingo","Jos","Kaduna","Kano","Katsina","Lafia","Lagos","Lokoja",
    "Makurdi","Maiduguri","Minna","Oshogbo","Owerri","Port Harcourt","Sokoto","Umuahia",
    "Uyo","Yenagoa","Yola","Zaria","Ibeno"
]
cities_ng = sorted(set(cities_ng), key=lambda x: x.lower())

# Single searchable selectbox
selected_city = st.selectbox("City", cities_ng, index=0)

st.divider()

if selected_city:
    with st.spinner(f"Fetching weather for {selected_city}..."):
        result = get_weather(selected_city)

    if "error" in result:
        st.error(result["error"])
    else:
        st.subheader(f"Weather in {result['city']}")
        st.caption(result["condition"] or "")

        # Top metrics
        top = st.columns(3)
        with top[0]:
            st.metric("Temperature", f"{result['temperature']}°C", f"Feels like {result['feels_like']}°C")
        with top[1]:
            st.metric("Humidity", f"{result['humidity']}%")
        with top[2]:
            st.metric("Wind Speed", f"{result['wind_speed']} m/s")

        bottom = st.columns(2)
        with bottom[0]:
            st.metric("Pressure", f"{result['pressure']} hPa")
        with bottom[1]:
            st.metric("Condition", result["condition"] or "")

st.markdown(
    """
    <hr style='opacity:.3'>
    <div style='text-align:center; color:gray;'>
        Powered by OpenWeatherMap API
    </div>
    """,
    unsafe_allow_html=True,
)
