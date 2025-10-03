# Example with caching based on time
# caching_proxy.py
from __future__ import annotations
import time
from threading import RLock
from typing import Callable, Any, Dict, Tuple

class TTLCacheProxy:
    def __init__(self, func: Callable[..., Any], ttl: float = 5.0):
        self._func = func
        self._ttl = ttl
        self._cache: Dict[Tuple, Tuple[float, Any]] = {}
        self._lock = RLock()

    def __call__(self, *args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        now = time.time()
        with self._lock:
            meta = self._cache.get(key)
            if meta:
                ts, val = meta
                if now - ts < self._ttl:
                    # cache hit
                    return val
            # cache miss
            val = self._func(*args, **kwargs)
            self._cache[key] = (now, val)
            return val

# demo
if __name__ == "__main__":
    import math, time
    def slow(n):
        time.sleep(0.3); return n*n
    cached_slow = TTLCacheProxy(slow, ttl=2.0)
    print(cached_slow(3))  # slow
    print(cached_slow(3))  # fast (cached)
    time.sleep(2.1)
    print(cached_slow(3))  # slow again (ttl expired)
