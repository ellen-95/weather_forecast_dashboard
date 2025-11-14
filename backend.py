import requests
from dotenv import load_dotenv
import os


load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_data(place,forecast_days=None):
    url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {"q": place, "appid": API_KEY, "units": "metric"}
    response = requests.get(url, params=params)
    data = response.json()
    filtered_data = data["list"]
    nr_values= 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo",forecast_days=3))