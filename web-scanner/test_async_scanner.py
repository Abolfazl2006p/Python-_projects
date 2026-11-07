import asyncio
import aiohttp
from async_requester import AsyncRequester

async def main():
    requester = AsyncRequester()
    urls = [
        "http://127.0.0.1:5000/login",
        "http://127.0.0.1:5000/search?q=test",
        "http://127.0.0.1:5000/my-account"
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(requester.get(session, url))
        
        results = await asyncio.gather(*tasks)
        
        for url, (status, text) in zip(urls, results):
            if status:
                print(f"[{status}] {url} - Length: {len(text)}")
            else:
                print(f"[Failed] {url}")

if __name__ == "__main__":
    asyncio.run(main())
    