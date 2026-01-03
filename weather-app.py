import requests

def get_weather(api_key, location):
    url = f"https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather_data = {
            "location": data["name"],
            "description": data["weather"][0]["description"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather_data
    else:
        print(f"There was an error: {data['message']}")
        return None   

def main():
    with open("api_key.txt") as f:
        api_key = f.read().strip()

    location = input("Enter the city name or coordinates (latitude,longitude): ")
    weather_data = get_weather(api_key, location)

    if weather_data:
        print(f"Weather in {weather_data['location']}:")
        print(f"Description: {weather_data['description']}")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind Speed: {weather_data['wind_speed']} m/s")

if __name__ == "__main__":
    main()