# 🌦 Seplat Weather Predictor

Seplat Weather Predictor is a simple yet powerful web app built with **Streamlit** that provides real-time weather updates for all 36 states in Nigeria (including FCT Abuja).  
It also supports **global city searches** while keeping a quick-access dropdown for Nigerian states.  
The app fetches live weather data from the **OpenWeatherMap API** and presents it in a clean, card-based layout with company branding.  

---

## 📖 Features
- Real-time weather data for **all Nigerian states**  
- **Searchable dropdown menu** for Nigerian states  
- **Global support** → type any city name worldwide to get weather data  
- Displays **temperature, feels-like temperature, humidity, wind speed, air pressure, and overall condition**  
- Clean and responsive **card layout design** with branding/logo support  
- Powered by **Streamlit Cloud** for deployment  

---

## 📊 Example Response

Here’s what you can expect when checking the weather for **Lagos**:

- **Temperature**: 29°C (Feels like 32°C)  
- **Humidity**: 78%  
- **Wind Speed**: 3.5 m/s  
- **Pressure**: 1013 hPa  
- **Condition**: Cloudy  

---

## 🚀 Deployment Instructions (Streamlit Cloud)

Follow these steps to deploy your app on **Streamlit Cloud**:

1. Push your project files (`app.py`, `requirements.txt`, and your logo if used) to a GitHub repository.  
2. Go to [Streamlit Cloud](https://share.streamlit.io/).  
3. Log in with your GitHub account.  
4. Click **New app**, select your repository, and choose `app.py` as the entry file.  
5. Streamlit Cloud will automatically install dependencies from `requirements.txt`.  
6. Once deployed, you’ll get a **public link** to share your app.  

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    A[User] -->|Selects Nigerian State or Searches City| B[Streamlit UI]
    B -->|Fetches Data Request| C[OpenWeatherMap API]
    C -->|Returns JSON Response| B
    B -->|Processes & Formats Data| D[Weather Data Processor]
    D -->|Displays Results in Cards & Metrics| E[Weather Report Output]
