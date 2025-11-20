# Rain Alert App 🌧️

Hey! So I built this little Python app that basically texts me when it's going to rain. No more getting caught without an umbrella!

## What does it do?

Pretty simple actually:
- Checks the weather forecast using OpenWeatherMap
- Looks at the next 12 hours 
- If rain is coming, it sends me a text via Twilio
- All my API keys are safely stored in environment variables (learned that the hard way!)

## What you'll need

- Python 3.6 or newer
- An API key from OpenWeatherMap (it's free!)
- A Twilio account with a phone number

## Setting it up

First, grab the code:
```bash
git clone https://github.com/yourusername/rain-alert-app.git
cd rain-alert-app
```

Install the stuff it needs:
```bash
pip install -r requirements.txt
```

Then create a `.env` file in the same folder. Just copy the `.env.example` file and fill in your own details:
```
OWM_API_KEY=your_openweathermap_api_key
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
RECIPIENT_PHONE_NUMBER=your_phone_number
```

Don't forget to update the coordinates in `main.py` to match your location! I've got mine set to Bhopal right now.

## Running it

Just run:
```bash
python main.py
```

If you want it to run automatically every morning (which is what I do), you can set up a cron job on Mac/Linux or use Task Scheduler on Windows.

## Requirements

Here's what gets installed:
```
requests==2.31.0
twilio==8.10.0
python-dotenv==1.0.0
```

## .env.example

I included this so you know what to put in your `.env` file:
```
OWM_API_KEY=your_openweathermap_api_key_here
TWILIO_ACCOUNT_SID=your_twilio_account_sid_here
TWILIO_AUTH_TOKEN=your_twilio_auth_token_here
TWILIO_PHONE_NUMBER=+1234567890
RECIPIENT_PHONE_NUMBER=+1234567890
```

## Note

Make sure your `.env` file is in the `.gitignore`! You don't want to accidentally push your API keys to GitHub (yes, I almost did that).

## License

MIT License - do whatever you want with it!

---

