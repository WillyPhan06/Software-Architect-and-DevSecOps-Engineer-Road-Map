Analysis of 1 URL run:

For the 1 URL i picked a fail url for all models to run to benchmark the overhead of starting.

Here are the rankings of fastest to slowest of 1 URL run:

1st. Threading

2nd. Mix

3rd. Asyncio

4th. Multiprocessing

So as seen from results, we can see this for quite the same for results we got from project 1 where for small scale of 10 URL, threading came out as fastest. This is due to the reason threading has lack initial overhead compared to the aiohttp of asyncio and spawning processes of multiprocessing. And the 2nd fastest is Mix, i designed mix to split list of urls into 3 parts, first part will be run for multiprocessing, second part will be for threading, and last part for asyncio. But since i coded the logic using slicing and use floor division so for cases below 3 parts, its usually be prioritize to asyncio first then threading second then multiprocessing last. So for the 1 URL case it was handled by asyncio alone and somehow it was faster than Asyncio alone but only around 0.01 seconds faster which is understandable.

Analysis of 10 URLs run:

This is to simulate just small scale but still its different than rather cold start and measure compared to 1 fail URL benchmark.

1st. Mix
2nd. Multiprocessing
3rd. Asyncio
4th. Threading

Now this is quite unexpected compared to my hypothesis of threading being the fastest then whatever come next like Asyncio or Mix then finally multiprocessing. The range is about 3 seconds and in 10 URLs tested, only 1 URL worked which is a mp4 video file. Might be due to net work issues which lead to these results or other factors. From this 10 URLs benchmark, it can be seen the results is quite different than 1 URL and what i expected, and I found out the network speed is not in control in the benchmark.

Analysis of 100 URLs run:

1st. Asyncio
2nd. Threading
3rd. Mix
4th. Multiprocessing

For this one, at first i forgot to increase the TCPConnector of asyncio up to 100 from original limit of 10, the result is still asyncio came out as fastest around 30 seconds, around 4 seconds faster than threading. But after i realized that flaw in benchmark and decided it was kinda unfair for asyncio, i increased TCPConnector limit up to 100 and it ran like a flash and finished within 20 seconds in average. Around 1.5x faster than threading and more than 3 times faster than multiprocessing. Threading come 2nd is expected since its excellence in I/O task but now the overhead of context switching between multiple threads is now starting to pay its cost compared to the natural of single thread, light weight, event loop of asyncio. And multiprocessing being the last is not surprised, for I/O tasks it's too overkill for multiprocessing since it have to spawn processes to run. Definitely not multiprocessing's playground yet until we see intensive CPU tasks in play.

Analysis of 1000 URLs run:

This now simulates practical scale of downloading web.

1st. Asyncio
2nd. Threading
3rd. Mix
4th. Multiprocessing

As expected from the theory and the real results speak for itself. In I/O bound tasks, especially for large scale one, asyncio smokes all other methods thanks to its light weight nature of using single thread for waiting tasks which is super efficient. Mix came as third as representative of "average" of all methods, all of it ran quite equally between all methods and come last is multiprocessing as i explained for the 100 URLs benchmark. In 1k URLs benchmark, even though the scale is 10x before but the time it took was only 1.5x slower than results from 100 URLs benchmark before thanks to concurrency. Asyncio showed results of more than twice as fast as threading, and 20x times faster than multiprocessing basically as benchmark went up 10x by scale, its results also went 10x which was around 600 seconds for 1k compared to 60 seconds for 100.

In conclusion, for small scale and overhead. Threading seems to showcase good work but still we can't ignore the fact that threading is super flexible since for blocking libraries than asyncio can't work on, threading can do the job. Or when you don't wanna recode everything in asyncio due to complexity, threading is there for you. Threading is jack of all trade here. For multiprocessing, well as you know the I/O bound tasks are too overkilled for multiprocessing, the nature of spawning different processes is to divide workload of CPU intensive tasks for true parallelism but for waiting tasks like web downloading, that's too much overhead. And the winner for large scale I/O bound tasks, as expected, is asyncio! This analysis compared all methods across different scales and spot patterns and analyzes pros and cons of different methods. Finally, let's say this for short, for large scale I/O bound tasks, take asyncio anytime unless you have to use blocking libraries that doesn't support asyncio then go for threading.