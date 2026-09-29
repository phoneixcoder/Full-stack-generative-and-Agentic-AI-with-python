import asyncio

async def async_one():
    print("async_one started")
    await asyncio.sleep(2)
    print("async_one finished")

asyncio.run(async_one())