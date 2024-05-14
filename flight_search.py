import requests
from dotenv import load_dotenv
import os

load_dotenv()


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.kiwi_search_endpoint = "https://api.tequila.kiwi.com/v2/search"
        self.kiwi_api = os.getenv("kiwi_api_key")
        self.kiwi_header = {'apikey': self.kiwi_api}

    def search(self, airport_codes: list, date_from, date_to):
        fly_to = ",".join(airport_codes)
        search_params = {
            # TODO: add a feature for searching flight for a couple of cities.
            # "fly_from": "KRK,STN,AMS"
            "fly_from": "KRK",
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "one_for_city": 1,

            "limit": 10
        }

        response = requests.get(self.kiwi_search_endpoint, params=search_params, headers=self.kiwi_header)
        return response.json()
