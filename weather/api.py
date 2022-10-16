import os

import aiohttp
from django.http import JsonResponse

from weather.helper import get_wind_direction

WEATHER_API_KEY = os.environ['WEATHER_API_KEY']  # Getting api key fromm secured env file


async def get_weather(request):
    city = request.GET.get('city')
    if city:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    'https://api.openweathermap.org/data/2.5/weather?units=metric&q=' + city + '&appid=' + WEATHER_API_KEY) as response:
                data = await response.json()
                if response.status == 200:
                    return JsonResponse(
                        {
                            "error": False,
                            "result": {
                                "place": data['name'],
                                "temp": data['main']['temp'],
                                "temp_min": data['main']['temp_min'],
                                "temp_max": data['main']['temp_max'],
                                "humidity": data['main']['humidity'],
                                "wind_speed": data['wind']['speed'],
                                "wind_dir": get_wind_direction(data['wind']['deg']),
                            },
                            "msg": "Success"
                        }, status=response.status
                    )
                else:
                    return JsonResponse(
                        {
                            "error": True,
                            "result": None,
                            "msg": data['message']
                        }, status=response.status
                    )

    else:
        return JsonResponse(
            {
                "error": True,
                "result": None,
                "msg": "Please Enter City Name."
            }, status=200
        )
