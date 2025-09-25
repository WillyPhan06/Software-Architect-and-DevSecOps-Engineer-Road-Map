# Apply Observer Pattern with asyncio which was related to concurrency that I already learnt early on in the road map, the total time it took is always concurrent, basically based on the single longest time of a single task

# observer/async_observer.py
import asyncio
import time

class AsyncEvent:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, coro):
        self._subscribers.append(coro)

    async def notify(self, message):
        await asyncio.gather(*(subscriber(message) for subscriber in self._subscribers))

class Timer:
    @staticmethod
    def start_timer():
        start_time = time.perf_counter()
        return start_time
    
    @staticmethod
    def end_timer():
        end_time = time.perf_counter()
        return end_time
    
    @staticmethod
    def get_total_time(start, end) -> float:
        total_time = end - start
        return total_time

# Example subscribers
async def email_async(msg):
    await asyncio.sleep(0.5)
    print(f"[Async Email] {msg}")

async def sms_async(msg):
    await asyncio.sleep(0.95)
    print(f"[Async SMS] {msg}")

async def main():
    event = AsyncEvent()
    event.subscribe(email_async)
    event.subscribe(sms_async)
    start = Timer.start_timer()
    await event.notify("Async Observer Event!")
    end = Timer.end_timer()
    total_time = Timer.get_total_time(start, end)
    print(f"All took total of {total_time}")

asyncio.run(main())
