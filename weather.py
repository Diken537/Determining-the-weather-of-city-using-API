import requests

def get_coordinates(city):

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        print("Status Code:", response.status_code)

        data = response.json()

        # Debugging: See what API returns
        print("API Response:", data)

        if response.status_code == 200:

            results = data.get("results")

            if results:

                location = results[0]

                latitude = location["latitude"]
                longitude = location["longitude"]
                country = location["country"]

                return latitude, longitude, country

            else:
                print("City not found!")
                return None

        else:
            print("API request failed!")
            return None

    except requests.exceptions.RequestException as e:
        print("Connection error:", e)
        return None
    
def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "apparent_temperature",
            "wind_speed_10m",
            "weather_code"
        ]
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data["current"]
    else:
        print("unable to fetch weather information")
        return None
    
def get_weather_description(code):

    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        51: "Light drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        95: "Thunderstorm"
}

    return weather_codes.get(code, "Unknown weather")

def display_weather(city, country, weather):
    print("\n================================")
    print("       WEATHER INFORMATION")
    print("================================")
    
    print(f"Location: {city}, {country}")
    print(f"Temperature: {weather['temperature_2m']}")
    print(f"Location: {city}, {country}")

    print(f"Temperature: {weather['temperature_2m']}°C")

    print(f"Feels Like: {weather['apparent_temperature']}°C")

    print(f"Humidity: {weather['relative_humidity_2m']}%")

    print(f"Wind Speed: {weather['wind_speed_10m']} km/h")

    description = get_weather_description(weather["weather_code"])

    print(f"Weather: {description}")

    print("================================")
    
def main():
    print("================================")
    print("       WEATHER APPLICATION")
    print("================================")
    
    city = input("Enter city name: ")
    location = get_coordinates(city)
    
    if location is None:
        return
    
    latitude, longitude, country = location
    weather = get_weather(latitude, longitude)
    
    if weather is None:
        return
    
    display_weather(city, country, weather)
    
    
if __name__ == "__main__":
    main()
