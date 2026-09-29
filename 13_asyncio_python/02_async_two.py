import asyncio
import time
async def brew(name):
    print(f"Brewing {name}...")
    await asyncio.sleep(3)
    print(f"{name} brewed")


async def main():
    await asyncio.gather(
        brew("Masala Chai"),
        brew("Ginger Chai"),
        brew("Elaichi Chai")
    )

asyncio.run(main())