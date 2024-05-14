import requests
from dotenv import load_dotenv
import os

load_dotenv()


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.kiwi_locations_endpoint = "https://api.tequila.kiwi.com/locations/query"
        self.kiwi_api = os.getenv("kiwi_api_key")
        self.kiwi_header = {'apikey': self.kiwi_api}

    def get_airport_codes(self, cities=None):
        if cities is None:
            cities = ['Paris', 'Berlin', 'Tokyo', 'Sydney',
                      'Istanbul', 'Kuala Lumpur', 'New York',
                      'San Francisco', 'Cape Town', 'Krakow',
                      'Katowice', 'Gdansk', 'Zurich', 'Bali']
        responses = [requests.get(url=self.kiwi_locations_endpoint,
                                  params={"term": city, "locale": "en-US", "location_types": "airport", },
                                  headers=self.kiwi_header
                                  )
                     for city in cities
                     ]
        airport_codes = [item.json()["locations"][0]["id"] for item in responses]

        return airport_codes
