import os

import aiohttp
from django.http import JsonResponse

from weather.helper import get_wind_direction

WEATHER_API_KEY = os.environ['WEATHER_API_KEY']  # Getting api key fromm secured env file


async def get_weather(request):
    city = request.GET.get('city')
    async with aiohttp.ClientSession() as session:
        async with session.get(
                'https://api.openweathermap.org/data/2.5/weather?units=metric&q=' + city + '&appid=' + WEATHER_API_KEY) as response:
            data = await response.json()
            return JsonResponse({
                "city": data['name'],
                "temp": data['main']['temp'],
                "temp_min": data['main']['temp_min'],
                "temp_max": data['main']['temp_max'],
                "humidity": data['main']['humidity'],
                "wind_speed": data['wind']['speed'],
                "wind_dir": get_wind_direction(data['wind']['deg']),
            })
