import asyncio
import aiohttp

url = 'http://core.zelorain.online'

async def check_port(client, port):
    print(port)
    async with client.get(f'{url}:{port}') as get_data:
        if get_data.ok:
            return f'OK PORT: {port}'
        else:
            return None


async def main():
    async with aiohttp.ClientSession() as session:
        get_data = [check_port(session, port) for port in range(0, 600 + 1)]

        status = await asyncio.gather(*get_data, return_exceptions=True)
        print(status)


asyncio.run(main())
