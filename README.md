# Flight Deals Notifier

Flight Deals Notifier is a Python program developed using Object-Oriented Programming principles to notify users about the best flight deals via SMS and email.

## Features

- **Data Management:** Utilizes Google Sheets API for storing and retrieving city data and user information.
- **Flight Data Retrieval:** Integrates the Kiwi Tequila API to fetch airport codes for specified cities and search for flight deals.
- **Notifications:** Implements notification functionalities using Twilio for SMS and SMTP for email notifications.
- **User Registration:** Enables users to register for flight deal notifications, with user data stored in Google Sheets for future notifications.

## Usage

1. **User Registration:**
   - Users can register to receive notifications about the best flight deals.
2. **Automated Search and Notification:**
   - The program automatically searches for flight deals for the next six months and notifies registered users via SMS and email.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/flight-deals-notifier.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Create a `.env` file and add the necessary environment variables:

```
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_NUMBER=your_twilio_phone_number
MY_NUMBER=your_phone_number
MY_EMAIL=your_email
MY_PASSWORD=your_email_password
SHEET_ID=your_google_sheet_id
KIWI_API_KEY=your_kiwi_api_key
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements you'd like to make.
