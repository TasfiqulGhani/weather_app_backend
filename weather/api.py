import os

import aiohttp
from django.http import JsonResponse

from weather.helper import get_wind_direction, get_cache_data, set_cache_data

WEATHER_API_KEY = os.environ['WEATHER_API_KEY']  # Getting api key fromm secured env file


async def call_api(city):
    async with aiohttp.ClientSession() as session:
        async with session.get(
                'https://api.openweathermap.org/data/2.5/weather?units=metric&q=' + city + '&appid=' + WEATHER_API_KEY) as api_response:
            data = await api_response.json()
            if api_response.status == 200:

                response = JsonResponse(
                    {
                        "error": False,
                        "result": {
                            "place": data['name'],
                            "temp": data['main']['temp'],
                            "temp_min": data['main']['temp_min'],
                            "temp_max": data['main']['temp_max'],
                            "humidity": data['main']['humidity'],
                            "wind_speed": data['wind']['speed'],
                            "description": data['weather'][0]['description'],
                            "wind_dir": get_wind_direction(data['wind']['deg']),
                        },
                        "msg": "Success"
                    }, status=api_response.status
                )
                set_cache_data(city, response)
                return response
            else:
                return JsonResponse(
                    {
                        "error": True,
                        "result": None,
                        "msg": data['message']
                    }, status=api_response.status
                )


async def handle_user_request(city):
    data = get_cache_data(city)
    if data:
        return data
    return await call_api(city)


async def get_weather(request):
    city = request.GET.get('city')
    if city:
        return await handle_user_request(city)
    else:
        return JsonResponse(
            {
                "error": True,
                "result": None,
                "msg": "Please Enter City Name."
            }, status=200
        )
