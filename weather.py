import requests
city = input("Enter city name: ")
url = f"https://api.open-metro.com/v1/forecast?latitude=35.7&longitude=51.4&current_weather=true"
response = requests.get(url)
data = response.json()
print("Temperature:", data["current_weather"]["temperature"])
print("Wind speed:", data["current_weather"]["windspeed"])
