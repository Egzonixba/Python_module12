# 1
import requests

def get_random_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        joke_data = response.json()
        return joke_data["value"]
    else:
        return "Failed to fetch Chuck Norris joke"

if __name__ == "__main__":
    random_joke = get_random_chuck_norris_joke()
    print("Chuck Norris Joke:")
    print(random_joke)



# 2

import requests

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        weather_data = response.json()
        description = weather_data['weather'][0]['description']
        temperature_kelvin = weather_data['main']['temp']
        temperature_celsius = kelvin_to_celsius(temperature_kelvin)
        return description, temperature_celsius
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None, None

if __name__ == "__main__":
    api_key = "90065583a7d9a8826448fd90d16465b7"
    city_name = input("Enter the name of a municipality: ")

    description, temperature = get_weather(api_key, city_name)

    if description is not None and temperature is not None:
        print(f"Weather in {city_name}: {description.capitalize()}")
        print(f"Temperature: {temperature:.2f}°C")
    else:
        print(f"Failed to fetch weather information for {city_name}")