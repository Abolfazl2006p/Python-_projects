from requester import Requester

scanner = Requester()
print("Sending request to Local Flask...")

response = scanner.get("http://127.0.0.1:5000/login")

if response:
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
else:
    print("Failed to connect.")