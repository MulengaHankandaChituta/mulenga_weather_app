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

if __name__ == "__main__":
    main()