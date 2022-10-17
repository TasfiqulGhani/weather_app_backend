from django.core.cache import cache

CACHE_TIME = 36000000
CACHE_ENABLE = True


def get_wind_direction(degree):
    val = int((degree / 22.5) + .5)
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    return directions[(val % 16)]


def get_cache_data(key):
    if CACHE_ENABLE:
        return cache.get(key)
    else:
        return None


def set_cache_data(key, value):
    cache.set(key, value, CACHE_TIME)


def clear_cache():
    cache.clear()
