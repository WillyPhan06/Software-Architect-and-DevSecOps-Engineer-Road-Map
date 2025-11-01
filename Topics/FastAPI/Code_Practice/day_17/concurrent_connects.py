import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from db_engine import AsyncSessionLocal
from sqlalchemy import text

async def test_pool():
    async def worker(i):
        async with AsyncSessionLocal() as session:
            result = await session.execute(text("SELECT 1"))
            print(f"Worker {i} done")

    # Simulate 30 concurrent tasks
    await asyncio.gather(*(worker(i) for i in range(30)))

asyncio.run(test_pool())
