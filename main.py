# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

import datetime as dt
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
from user import User

today = dt.datetime.today()
tomorrow = today + dt.timedelta(days=1)
tomorrow = tomorrow.strftime("%d/%m/%Y")
six_months_later = today + dt.timedelta(days=180)
six_months_later = six_months_later.strftime("%d/%m/%Y")

dm = DataManager()
fd = FlightData()
fs = FlightSearch()
nm = NotificationManager()
us = User()


city_list = dm.get_cities()
airport_codes = fd.get_airport_codes(cities=city_list)

dm.set_airport_codes(airport_codes=airport_codes)

search_data = fs.search(airport_codes=airport_codes, date_from=tomorrow, date_to=six_months_later)

message_list = dm.check_lowest_price(search_data=search_data)

nm.send_message(sms_context=message_list)

email_addresses = dm.get_email_addresses()

nm.send_email(mail_context=message_list, mail_list=email_addresses)
