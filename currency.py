import requests
def get_usd_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data["rates"]["IRR"] / 10
def convert_to_toman(usd):
    rate = get_usd_rate()
    return usd * rate
usd = float(input("Enter USD amount: "))
try:
    rate = float(input("Enter USD rate (Toman): "))
except ValueError:
    print("Invalid rate! Please enter a number.")    
toman = usd *  rate
print(f"{usd} USD = {toman:,.0f} Toman")
