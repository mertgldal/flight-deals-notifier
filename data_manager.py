# import requests
import datetime as dt
import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
import os

load_dotenv()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        self.creds = Credentials.from_service_account_file("credentials.json", scopes=self.scopes)
        self.client = gspread.authorize(self.creds)
        self.sheet_id = os.getenv("sheet_id")
        self.workbook = self.client.open_by_key(self.sheet_id)
        self.prices_sheet = self.workbook.worksheet("prices")
        self.users_sheet = self.workbook.worksheet("users")
        # self.shetty_endpoint = "https://api.sheety.co/256912354461546392c0a11ba8b95752/flightDeals/prices"
        # self.headers = {'Content-Type': 'application/json'}

    def get_cities(self):
        data = self.prices_sheet.get_all_records()
        cities = [item['City'] for item in data]

        return cities

        # It was the same thing with above code but with shetty api instead of Google sheets api.
        # shetty_api_response = requests.get(url=self.shetty_endpoint, headers=self.headers)
        # cities = [item['city'] for item in shetty_api_response.json()['prices']]
        #
        # return cities

    def set_airport_codes(self, airport_codes=None):
        if airport_codes is None:
            airport_codes = ['CDG', 'BER', 'NRT',
                             'SYD', 'IST', 'KUL',
                             'JFK', 'SFO', 'CPT',
                             'KRK', 'KTW', 'GDN',
                             'ZRH', 'DPS']

        # Generate values_to_update list based on airport_codes
        values_to_update = [[code] for code in airport_codes]

        # Update the prices_sheet with the generated values_to_update
        self.prices_sheet.update(range_name='B2:B{}'.format(len(airport_codes) + 1), values=values_to_update)

    # It was the same thing with above code but with shetty api instead of Google sheets api.
    #      [requests.put(url=f"{self.shetty_endpoint}/{index + 2}", json={"price": {"iataCode": code}},
    #                    headers=self.headers) for index, code in enumerate(airport_codes)]

    def check_lowest_price(self, search_data):

        data = self.prices_sheet.get_all_records()
        lowest_prices = {item['City']: item['Lowest Price'] for item in data}

        # It was the same thing with above code but with shetty api instead of Google sheets api.
        # response = requests.get(url=self.shetty_endpoint, headers=self.headers)
        # data = response.json()
        # lowest_prices = {item['city']: item['lowestPrice'] for item in data['prices']}
        send_sms = []

        for flight in search_data['data']:
            city = flight['cityTo']
            if city in lowest_prices:
                if flight['price'] < lowest_prices[city]:
                    # Parse the string into a datetime object
                    departure_time = dt.datetime.strptime(flight['local_departure'], '%Y-%m-%dT%H:%M:%S.%fZ')
                    # Format the datetime object as desired
                    formatted_departure_time = departure_time.strftime('%Y-%m-%d %H:%M')
                    sms_context = {
                        "city_from": flight["cityFrom"],
                        "city_code_from": flight["cityCodeFrom"],
                        "city_to": flight["cityTo"],
                        "city_code_to": flight["cityCodeTo"],
                        "departure_time": formatted_departure_time,
                        "flight_price": flight['price']
                    }
                    send_sms.append(sms_context)

        return send_sms

    def get_email_addresses(self):
        data = self.users_sheet.get_all_records()
        emails = [item['Email'] for item in data]
        return emails
