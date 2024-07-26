import requests

API_KEY = 'co96aehr01qodgqqtug0co96aehr01qodgqqtugg'
BASE_URL = 'https://finnhub.io/api/v1/forex/candle'

def get_forex_data(symbol, resolution, from_time, to_time):
    params = {
        'symbol': symbol,
        'resolution': resolution,
        'from': from_time,
        'to': to_time,
        'token': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data
