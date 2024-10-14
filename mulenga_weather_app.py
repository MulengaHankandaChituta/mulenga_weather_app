# weather  app using python

import  requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except  requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
    
def display_weather(weather_data):
    if weather_data:
        print("\nCurrent Weather Conditions:")
        print(f"City: {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Description: {weather_data['weather'][0]['description']}")
    else:
        print("No weather data availeble.")
def main():
    api_key = "c6ec8aff2594866c806b70cbda6a6128"
    city = input("Enter the city name:  ")

    weather_data = get_weather(api_key,city)
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