import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
import os

load_dotenv()


class User:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        self.creds = Credentials.from_service_account_file("credentials.json", scopes=self.scopes)
        self.client = gspread.authorize(self.creds)
        self.sheet_id = os.getenv("sheet_id")
        self.workbook = self.client.open_by_key(self.sheet_id)
        self.users_sheet = self.workbook.worksheet("users")

    def create_user(self):
        print(
            "Welcome to Flight Club.\nWe find the best flight deals and email you.")

        self.first_name = input("What is your first name?\n")
        self.last_name = input("What is your last name?\n")

        condition = True
        self.email = ""

        while condition:
            self.email = input("What is your email?\n")
            email_validation = input("Type your email again.\n")
            if self.email == email_validation:
                condition = False
                print("You're in the club!")
                print("We're finding and sending the best flights to you. Check your email!")
            else:
                print("Emails don't match. Please try again.")

        data = self.get_users_data()
        self.set_users_data(user_data=data)

        # It was the same thing with the above code but with shetty api instead of Google sheet api.
        # shetty_endpoint = "https://api.sheety.co/256912354461546392c0a11ba8b95752/flightDeals/users"

        # user_data = {
        #     "user": {
        #         "firstName": first_name,
        #         "lastName": last_name,
        #         "email": email
        #     }
        # }
        #
        # response = requests.post(url=shetty_endpoint, json=user_data)
        # print(response.text)
        # print(response.json())

    def get_users_data(self):
        # It returns all users data from a Worksheet as a List of Lists
        return self.users_sheet.get_all_values()

    def set_users_data(self, user_data):
        user_data.append([self.first_name, self.last_name, self.email])
        values_to_update = [item for item in user_data[1:]]
        self.users_sheet.update(range_name='A2:C{}'.format(len(user_data)), values=values_to_update)
