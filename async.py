import aiohttp
import asyncio

async def fetch(session, url):
    print(url)
    async with session.get(url) as response:
        print(response)
        return await response.text()

async def main():
    urls = [
            'http://python.org',
            'https://google.com',
            'http://yifei.me'
        ]
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch(session, url))
        htmls = await asyncio.gather(*tasks)  #gathering the results. it waits on a bunch of futures and return their results in a given order
                                              #Return a future aggregating results from the given coroutines or futures
        for html in htmls:
            print(html[:100])

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())