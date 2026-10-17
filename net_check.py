import requests
def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        print(f"{url} is Up! Status code: {response.status_code}")
    except requests.exceptions.RequestException:
        print(f"{url} is DOWN or unreachable.")
##تست کردن چند سایت
check_website("https://google.com")
check_website("https://github.com")
check_website("https://thiswebsitedoesnotexidt123.com")
            