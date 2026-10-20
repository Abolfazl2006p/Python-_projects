import requests

common_paths = ["admin", "login", "backup", "config", "dashboard", "secret"]

target_url = "http://ginandjuice.shop"

print(f"Scanning {target_url}...")

for path in common_paths:
    url = f"{target_url}/{path}"
    try:
        response = requests.get(url, timeout=3)
        
        if response.status_code == 200:
            print(f"[+] Found: {url}")
        else:
            print(f"[-] Not found: {url}")
            
    except requests.exceptions.RequestException:
        print(f"[!] Error connecting to {url}")