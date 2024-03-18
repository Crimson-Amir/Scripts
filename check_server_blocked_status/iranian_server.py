import asyncio
import aiohttp
import time
import json

urls_to_check = ['https://admin.ggkala.shop', 'https://netherlands.ggkala.shop']
api_address_for_report = 'https://check.ggkala.shop/report_connection_problem'
report_problem_text = "🔴 The Server Is Probably Blocked"
check_every_min = 1

async def fetch(url, session):
    try:
        async with session.get(url, timeout=2) as response:
            if response.status == 200:
                data = await response.json()
                if data.get('success'):
                    print('OK')
                    return
            await report(f'{report_problem_text}\nstatus code: {response.status}\nreason: {response.reason}\nSERVER: {url}')
    except Exception as e:
        await report(f'{report_problem_text}\nSERVER: {url}\nerror type: {type(e).__name__}\nerror: {e}')

async def report(text):
    async with aiohttp.ClientSession() as session:
        await session.post(api_address_for_report, data={'message': text})

async def check_periodically():
    while True:
        async with aiohttp.ClientSession() as session:
            await asyncio.gather(*[fetch(url, session) for url in urls_to_check])
            await asyncio.sleep(check_every_min * 60)

if __name__ == "__main__":
    asyncio.run(check_periodically())
