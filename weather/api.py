import os

import aiohttp
from django.http import JsonResponse

WEATHER_API_KEY = os.environ['WEATHER_API_KEY']  # Getting api key fromm secured env file


async def get_weather(session, url):
    async with session.get(url) as res:
        weather_data = await res.json()
        return weather_data


async def get_weather(request):
    async with aiohttp.ClientSession() as session:
        async with session.get(
                'https://api.openweathermap.org/data/2.5/weather?q=Dhaka&appid=' + WEATHER_API_KEY) as response:
            return JsonResponse(await response.json())
