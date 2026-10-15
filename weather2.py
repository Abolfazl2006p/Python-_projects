import requests
city = input("Enter city name: ")
url = f"https://wttr.in/{city}?format=j1"
response = requests.get(url)
data = response.json()
print("Temperature:", data["current_condition"][0]["temp_C"])
print("Weather:", data["current_condition"][0]["weatherDesc"][0]["value"])
