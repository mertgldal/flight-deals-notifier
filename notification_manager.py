from twilio.rest import Client
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.twilio_account_sid = os.getenv('twilio_account_sid')
        self.twilio_auth_token = os.getenv('twilio_auth_token')
        self.twilio_number = os.getenv('twilio_number')
        self.my_number = os.getenv('my_number')
        self.my_email = os.getenv('my_email')
        self.my_password = os.getenv('my_password')

    def send_message(self, sms_context):
        client = Client(self.twilio_account_sid, self.twilio_auth_token)

        for message_context in sms_context:
            message_body = (f"Only €{message_context['flight_price']} to fly from {message_context['city_from']}-"
                            f"{message_context['city_code_from']} to {message_context['city_to']}-"
                            f"{message_context['city_code_to']} at {message_context['departure_time']} ")
            message = client.messages.create(
                from_=self.twilio_number,
                body=message_body,
                to=self.my_number
            )
            print(message.status)

    def send_email(self, mail_context, mail_list):
        try:
            with smtplib.SMTP("smtp.gmail.com", timeout=10, port=587) as connection:
                connection.starttls()
                connection.login(user=self.my_email, password=self.my_password)
                for mail in mail_list:
                    for message_context in mail_context:
                        message_body = (f"Subject: Flight Deals\n\nOnly €{message_context['flight_price']} to fly from "
                                        f"{message_context['city_from']}-{message_context['city_code_from']} to "
                                        f"{message_context['city_to']}-{message_context['city_code_to']} at "
                                        f"{message_context['departure_time']}")

                        connection.sendmail(from_addr=self.my_email,
                                            to_addrs=mail,
                                            msg=message_body.encode('utf-8')
                                            )
        except smtplib.SMTPException as e:
            print(e)
            print("Something wrong with your SMTP server")
