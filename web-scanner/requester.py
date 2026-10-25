import requests

class Requester:
    def __init__(self, timeout=15):
        self.session = requests.session()
        self.timeout = timeout 
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0 Win64; x64) Web-Scanner/1.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
        })

    def get(self, url, params=None):
         try:
             response = self.session.get(url, params=params, timeout=self.timeout)
             return response
         except requests.RequestException as e:
             print(f"[-] Error GET {url}: {e}")
             return None
         
    def post(self, url, data=None):
         try:
             response = self.session.post(url, data=data, timeout=self.timeout)
             return response
         except requests.RequestException as e:
             print(f"[-] Error POST {url}: {e}")
             return None     