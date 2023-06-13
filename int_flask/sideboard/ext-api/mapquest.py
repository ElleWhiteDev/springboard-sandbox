import requests
from secrets import MAPQUEST_API_KEY

response = requests.get('https://www.mapquestapi.com/geocoding/v1/address',
                        params={'key': MAPQUEST_API_KEY, 'location': '123 Main st'})
