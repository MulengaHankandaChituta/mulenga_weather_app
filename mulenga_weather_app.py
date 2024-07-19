import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching weather data: {e}")
        return None

def display_weather(weather_data):
    if weather_data:
        result = (f"City: {weather_data['name']}\n"
                  f"Temperature: {weather_data['main']['temp']}°C\n"
                  f"Humidity: {weather_data['main']['humidity']}%\n"
                  f"Description: {weather_data['weather'][0]['description']}")
        result_label.config(text=result)
    else:
        result_label.config(text="No weather data available.")

def get_weather_button_clicked():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    api_key = "c6ec8aff2594866c806b70cbda6a6128"  # Replace with your actual API key
    weather_data = get_weather(api_key, city)
    display_weather(weather_data)

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create and place the widgets
city_label = tk.Label(root, text="Enter the city name:")
city_label.pack(pady=5)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather_button_clicked)
get_weather_button.pack(pady=10)

result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=10)

# Run the application
root.mainloop()