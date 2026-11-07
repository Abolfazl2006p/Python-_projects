import aiohttp

class AsyncRequester:
    def __init__(self, timeout=10):
        self.timeout = aiohttp.ClientTimeout(total=timeout)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (windows NT 10.0; win64; x64) web-Scanner/2.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
        }

    async def get(self, session, url, params=None):
        try:
            async with session.get(url, params=params, headers=self.headers, timeout=self.timeout) as response:
                text = await response.text()
                return response.status, text
        except Exception as e:
            print(f"[-] Error GET {url}: {e}")
            return None, None
    async def post(self, session, url, data=None):
        try:
            async with session.post(url, data=data, headers=self.headers, timeout=self.timeout) as response:
                text = await response.text()
                return response.status, text
        except Exception as e:
            print(f"[-] Error POST {url}: {e}")
            return None, None     
    