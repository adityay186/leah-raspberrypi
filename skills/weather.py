import requests

def get_weather(city):
    api_key = '182a87f539d9bca49af1ae23ac08e611'  # Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
    query = city['location']

    url = f'http://api.openweathermap.org/data/2.5/weather?q={query}&appid={api_key}&units=metric'
    response = requests.get(url)
    weather_data = response.json()

    city_name = weather_data['name']
    region = weather_data['sys']['country']
    temperature = weather_data['main']['temp']
    weather_description = weather_data['weather'][0]['description']

    result = f"In {city_name}, {region}, it's {temperature} degrees Celsius and {weather_description}."

    return result
