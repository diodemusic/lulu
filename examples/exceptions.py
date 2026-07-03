import asyncio
import os

from dotenv import load_dotenv

from pyke import Continent, Pyke, exceptions

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")


async def main() -> None:
    async with Pyke(API_KEY, timeout=60, print_url=True) as api:
        # We can get the full httpx response and headers from the pyke exception
        try:
            await api.account.by_riot_id(Continent.EUROPE, "saves", "000")
        except exceptions.RateLimitExceeded as e:
            print(f"Message: {e.message}")
            print(f"Error code: {e.error_code}")

            if e.response:
                print(f"Response: {e.response}")
                print(f"Headers: {e.response.headers}")


if __name__ == "__main__":
    asyncio.run(main())
