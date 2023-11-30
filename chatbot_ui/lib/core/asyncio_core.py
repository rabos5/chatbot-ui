import asyncio


async def gather_tasks(tasks):
    return await asyncio.gather(**tasks, return_exceptions=True)