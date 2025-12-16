"""
A simple python script that uses a api key to retrive user input city weather data
"""
import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    print("Invalid or missing API key")
    exit()

city = input("Enter a city name... : ")


response = requests.get(f"https://api.openweathermap.org/data/2.5/"
                        f"weather?q={city}&units=metric&appid={API_KEY}")

if response.status_code == 200:
    data = response.json()
    temperature = int(data["main"]["temp"])
    humidity = data["main"]["humidity"]
    print(f"The weather in {city} is {temperature} °c with a humidity of {humidity} % ")
else:
    print("Something went wrong ! ")
