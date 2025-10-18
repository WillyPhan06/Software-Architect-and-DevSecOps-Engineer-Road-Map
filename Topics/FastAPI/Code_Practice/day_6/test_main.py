# test_main.py
import pytest
from httpx import AsyncClient  # <- normal httpx AsyncClient
from main import app

@pytest.mark.asyncio
async def test_sync_sleep():
    # need to actually run the server, so use AsyncClient with URL
    async with AsyncClient(base_url="http://127.0.0.1:8000") as client:
        res = await client.get("/sync-sleep?seconds=1")
    assert res.status_code == 200
    data = res.json()
    assert data["endpoint"] == "sync-sleep"

@pytest.mark.asyncio
async def test_async_sleep():
    async with AsyncClient(base_url="http://127.0.0.1:8000") as client:
        res = await client.get("/async-sleep?seconds=1")
    assert res.status_code == 200
    data = res.json()
    assert data["endpoint"] == "async-sleep"


@pytest.mark.asyncio
async def test_proxy_async():
    async with AsyncClient(base_url="http://127.0.0.1:8000") as client:
        res = await client.get("/proxy-async")
    assert res.status_code == 200
    data = res.json()
    assert "status" in data

@pytest.mark.asyncio
async def test_sync_call_in_async():
    async with AsyncClient(base_url="http://127.0.0.1:8000") as client:
        res = await client.get("/sync-call-in-async?x=5")
    assert res.status_code == 200
    data = res.json()
    assert "from_threadpool" in data
