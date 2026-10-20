import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = requests.Session()
session.trust_env = False

common_paths = ["admin", "login"]
target_url = "https://example.com"

print(f"Starting scan on {target_url}...")

for path in common_paths:
    url = f"{target_url}/{path}"
    print(f"Testing: {url}")
    
    try:
        response = session.get(url, timeout=5, verify=False)
        if response.status_code == 200:
            print(f"  [+] Found: {url}")
        else:
            print(f"  [-] Not found (Status: {response.status_code})")
    except Exception as e:
        print(f"  [!] Connection failed: {e}")
        
print("Scan finished!")