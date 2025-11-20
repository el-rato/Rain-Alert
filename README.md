# Rain Alert App 🌧️

A Python application that checks weather forecasts and sends SMS alerts when rain is expected.

## Features
- Fetches weather data from OpenWeatherMap API
- Checks forecast for the next 12 hours
- Sends SMS alerts via Twilio when rain is detected
- Uses environment variables for secure credential management

## Prerequisites
- Python 3.6+
- OpenWeatherMap API key
- Twilio account with phone number

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/rain-alert-app.git
cd rain-alert-app
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:
```
OWM_API_KEY=your_openweathermap_api_key
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
RECIPIENT_PHONE_NUMBER=your_phone_number
```
## Usage

Run the script:
```bash
python main.py
```

To run automatically, set up a cron job (Linux/Mac) or Task Scheduler (Windows).

## License
MIT License
```

## 3. `requirements.txt` file
Create a file named `requirements.txt`:
```
requests==2.31.0
twilio==8.10.0
python-dotenv==1.0.0
```

## 4. `.env.example` file (optional but recommended)
Create a file named `.env.example`:
```
OWM_API_KEY=your_openweathermap_api_key_here
TWILIO_ACCOUNT_SID=your_twilio_account_sid_here
TWILIO_AUTH_TOKEN=your_twilio_auth_token_here
TWILIO_PHONE_NUMBER=+1234567890
RECIPIENT_PHONE_NUMBER=+1234567890
```
