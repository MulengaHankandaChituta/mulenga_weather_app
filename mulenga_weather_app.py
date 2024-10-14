import tkinter as tk
from tkinter import messagebox
import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv(dotenv_path='.env')

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather(city, weather_data):
    if weather_data:
        weather_conditions = (
            f"City: {city}\n"
            f"Temperature: {weather_data['main']['temp']}°C\n"
            f"Humidity: {weather_data['main']['humidity']}%\n"
            f"Description: {weather_data['weather'][0]['description']}"
        )
        messagebox.showinfo("Weather Conditions", weather_conditions)
    else:
        messagebox.showerror("Error", "No weather data available.")

def fetch_weather(api_key, city_entry):
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    weather_data = get_weather(api_key, city)
    display_weather(city, weather_data)

def main():
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        messagebox.showerror("Error", "API key not found. Please set the API key in your .env file.")
        return

    root = tk.Tk()
    root.title("Weather App")

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    label = tk.Label(frame, text="Enter city name:")
    label.pack(side=tk.LEFT)

    city_entry = tk.Entry(frame, width=30)
    city_entry.pack(side=tk.LEFT, padx=10)

    fetch_button = tk.Button(frame, text="Fetch Weather", command=lambda: fetch_weather(api_key, city_entry))
    fetch_button.pack(side=tk.LEFT)

    root.mainloop()

if __name__ == "__main__":
    main()