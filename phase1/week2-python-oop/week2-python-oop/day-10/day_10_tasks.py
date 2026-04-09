import asyncio
import httpx
import time 
from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper():
        before=time.time()
        func()
        after=time.time()
        excution_time=after-before
        print(f"{excution_time:.4f}")
    return wrapper
async def fetch_api(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.status_code
@my_decorator
async def main():
    results = await asyncio.gather(
        fetch_api("https://httpbin.org/get"),
        fetch_api("https://httpbin.org/get"),
        fetch_api("https://httpbin.org/get"),
    )
    print(results)


asyncio.run(main())