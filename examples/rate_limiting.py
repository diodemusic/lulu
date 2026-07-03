import asyncio
import os

from dotenv import load_dotenv

from pyke import Continent, Pyke, exceptions

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")


async def main() -> None:
    async with Pyke(API_KEY, timeout=60, print_url=True) as api:
        # Lets call some endpoint
        await api.account.by_riot_id(Continent.EUROPE, "saves", "000")

        # Now we can have a look at the latest rate limit information
        print(
            api.rate_limit
        )  # Output: RateLimit(app_limit='100:120,20:1', app_count='1:120,1:1', method_limit='1000:60', method_count='1:60')

        # Call the endpoint again
        await api.account.by_riot_id(Continent.EUROPE, "saves", "000")

        # Rate limit information automagically updated!
        print(
            api.rate_limit
        )  # Output: RateLimit(app_limit='100:120,20:1', app_count='2:120,2:1', method_limit='1000:60', method_count='2:60')

        # Now you can easily implement your own rate limit handling

        # What if we hit a 429? Easy, just grab the retry-after header from the exceptions response
        try:
            await api.account.by_riot_id(Continent.EUROPE, "saves", "000")
        except exceptions.RateLimitExceeded as e:
            if e.response:
                print(
                    f"Rate limited, please retry after {e.response.headers.get('retry-after')} seconds"
                )  # Output: Rate limited, please retry after x seconds

                return


if __name__ == "__main__":
    asyncio.run(main())
