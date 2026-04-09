import asyncio
import httpx
import time 
from functools import wraps
def my_decorator(func):
    @wraps(func)
    async def wrapper(*args,**kwargs):
        before=time.time()
        await func(*args,**kwargs)
        after=time.time()
        execution_time =after-before
        print(f"⏱  main took {execution_time :.4f} seconds")
    return wrapper
async def fetch_weather(place):
    url = f"https://wttr.in/{place}?format=j1"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        temp = data["current_condition"][0]["temp_C"]
        desc = data["current_condition"][0]["weatherDesc"][0]["value"]
        return f"🌤  Weather In {place}: {temp}°C, {desc}"
    

async def fetch_github(username):
    url = f"https://api.github.com/users/{username}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        return f"👤 GitHub:  {data['name']} | {data['public_repos']} repos | {data['followers']} followers"
    
async def fetch_news():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        return f"📰 Latest Post: '{data['title']}' by User {data['userId']}"
    
@my_decorator
async def main():
    results = await asyncio.gather(
        fetch_weather("calicut"),
        fetch_github("ajmalyaseen"),
        fetch_news()
        )
    
    for result in results:
        print(result)
    print()
    print("✅ All 3 APIs fetched concurrently")


asyncio.run(main())