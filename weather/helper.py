def get_wind_direction(degree):
    val = int((degree / 22.5) + .5)
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    return directions[(val % 16)]
