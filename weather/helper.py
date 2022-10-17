from django.core.cache import cache

CACHE_TIME = 36000000
CACHE_ENABLE = True


def get_wind_direction(degree, lang):
    val = int((degree / 22.5) + .5)

    directions = ["North", "North-Northeast", "Northeast", "East-Northeast", "East", "East-Southeast",
                  "Southeast", "South-Southeast", "South", "South-Southwest", "Southwest", "West-Southwest", "West",
                  "West-Northwest",
                  "Northwest", "North-Northwest"]

    directions_de = ["Norden", "Nord-Nordosten", "Nordosten", "Osten-Nordosten", "Osten", "Osten-Südosten",
                     "Südosten", "Süd-Südosten", "Süden", "Süd-Südwesten", "Südwesten", "West-Südwesten", "Westen",
                     "West-Nordwest",
                     "Nordwesten", "Nord-Nordwesten"]

    directions_fr = ["Nord", "Nord-Nord-Est", "Nord-Est", "Est-Nord-Est", "Est", "Est-Sud-Est",
                     "Sud-Est", "Sud-Sud-Est", "Sud", "Sud-Sud-Ouest", "Sud-Ouest", "Ouest-Sud-Ouest", "Ouest",
                     "Ouest-Nord-Ouest",
                     "Nord-Ouest", "Nord-Nord-Ouest"]

    direction_languages = {
        'fr': directions_fr,
        'en': directions,
        'de': directions_de
    }
    return direction_languages[lang][(val % 16)]


def get_cache_data(key):
    if CACHE_ENABLE:
        return cache.get(key)
    else:
        return None


def set_cache_data(key, value):
    cache.set(key, value, CACHE_TIME)


def clear_cache():
    cache.clear()
