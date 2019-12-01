import requests, random, datetime

def get_cities(key):
    response = requests.get(f'https://www.metaweather.com/api/location/search/?query={key}')

    # If the response was successful, no Exception will be raised
    response.raise_for_status()

    cities = [ it['title'] for it in response.json() ] 

    return str(cities)