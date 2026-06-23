import requests


def get_coordinates(city):
    """
    Fetch latitude, longitude and country information
    for the given city using Open-Meteo Geocoding API.
    """

    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"

    response = requests.get(url)
    data = response.json()

    if "results" not in data:
        return None

    result = data["results"][0]

    return {
        "country": result["country"],
        "latitude": result["latitude"],
        "longitude": result["longitude"]
    }


def get_weather(latitude, longitude):
    """
    Fetch weather information using latitude and longitude.
    """

    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=temperature_2m,"
        f"wind_speed_10m,"
        f"relative_humidity_2m,"
        f"weather_code"
    )

    response = requests.get(weather_url)
    weather_data = response.json()

    weather_codes = {
        0: "Clear Sky",
        1: "Mainly Clear",
        2: "Partly Cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing Rime Fog",
        51: "Light Drizzle",
        53: "Moderate Drizzle",
        55: "Dense Drizzle",
        61: "Slight Rain",
        63: "Moderate Rain",
        65: "Heavy Rain"
    }

    current = weather_data["current"]

    return {
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "wind_speed": current["wind_speed_10m"],
        "condition": weather_codes.get(
            current["weather_code"],
            "Unknown"
        )
    }


def display_weather(city, country, weather):
    """
    Display weather information neatly.
    """

    print("\nWeather Information")
    print("-------------------")
    print(f"City: {city}")
    print(f"Country: {country}")
    print(f"Temperature: {weather['temperature']} °C")
    print(f"Condition: {weather['condition']}")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Wind Speed: {weather['wind_speed']} km/h")


def main():
    city = input("Enter city name: ")

    location = get_coordinates(city)

    if location is None:
        print("City not found. Please enter a valid city name.")
        return

    weather = get_weather(
        location["latitude"],
        location["longitude"]
    )

    display_weather(
        city,
        location["country"],
        weather
    )


main()