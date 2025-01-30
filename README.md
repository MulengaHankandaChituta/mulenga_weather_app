Weather App

Description

This is a simple Weather app built using python and Tkinter. It allows users to
fetch current weather conditions for any city using the OpenWeather API. The
app displays temperature, humidity, and weather description in a GUI window.

Features

- Fetch real-time weather data
- User-friendly Tkinter-based GUI
- Displays temperature, humidity, and weather description
- Error handling for missing API key or invalid city name

Technologies Used

- Python 3
- Tkinter(GUI)
- Requests(API calls)
- dotenv(Environment variable management)

Prerequisites

- Python3 installed on your system
- OpenWeather API key

How to Run

1. Clone the repositiory
- git clone https://github.com/MulengaHankandaChituta/weather-app.git
- cd weather-app
2. Install Dependencies
- pip install requests python-dotenv
3. Set Up the API Key
- Create a .env file in the project directory and add your OpenWeather API key
- OPENWEATHER_API_KEY=your_api_key_here
4. Run the Application
- python3 weather_app.py

Usage

1. Enter a city name in the input field.
2. Click the"Fetch Weather"button.
3. View the weather details in a pop-up window.

Future Improvements

- Add multiple unit options(Celsius, Fahrenheit, Kelvin)
- Implement a graphical weather icon display
- Allow users to save favorite cities
- Enhance UI design

License

This project is open-source and available under the MIT license

Author

Mulenga Hankanda Chituta
