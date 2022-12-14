import os

import aiohttp
from rest_framework.decorators import api_view
from rest_framework.response import Response

from weather.helper import get_wind_direction, get_cache_data, set_cache_data

WEATHER_API_KEY = os.environ['WEATHER_API_KEY']  # Getting api key fromm secured env file


async def call_api(city, lang):
    async with aiohttp.ClientSession() as session:
        async with session.get(
                'https://api.openweathermap.org/data/2.5/weather?units=metric&q=' + city + '&appid=' + WEATHER_API_KEY + '&lang=' + lang) as api_response:
            data = await api_response.json()
            if api_response.status == 200:
                response = Response(
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
                            "wind_dir": get_wind_direction(data['wind']['deg'], lang),
                        },
                        "msg": "Success"
                    }, status=api_response.status
                )
                await set_cache_data(city, response)
                return response
            else:
                return Response(
                    {
                        "error": True,
                        "result": None,
                        "msg": data['message']
                    }, status=api_response.status
                )


async def handle_user_request(city, lang):
    data = get_cache_data(city + lang)
    if data:
        return data
    return await call_api(city, lang)


@api_view(['get'])
async def get_weather(request):
    """
    Parameters :
	--
	city: Write any city name here
	lang: You can choose en , de or fr .

    """

    city = request.GET.get('city')
    lang = request.GET.get('lang', 'en')

    if city:
        return await handle_user_request(city, lang)
    else:
        return Response(
            {
                "error": True,
                "result": None,
                "msg": "Please Enter City Name."
            }, status=200
        )
