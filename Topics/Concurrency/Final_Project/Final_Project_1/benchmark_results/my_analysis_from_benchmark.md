For the benchmark of 10 URLS:

Threading came out as fastest followed by multiprocessing then asyncio.

Based on theory, this is quite off since for I/O bound tasks, asyncio is known for light weight and deal very well with I/O bound tasks such as downloading content from web, but here in small scale of 10 urls the overhead of aiohttp and event loop features in asyncio is too heavy while thread won because of no process bootup and no heavy overhead. Multiprocessing also dealt with overhead of spawning processes.

But for 100 URLS things got real very quick:

Asyncio came out fastest being around twice as fast as threading and 3 times faster than multiprocessing.

This is thanks to the nature of single thread and the I/O bound tasks of asyncio. And this completely matches with hypothesis of asyncio being super efficient for large scale I/O tasks.

Overview, most successes in each benchmark are the same since certain websites block automation and bots stuff via 403 Forbidden as we can see in the log.txt for both threading and asyncio.

In conclusion, for I/O bound tasks like downloading web, threading and asyncio are very efficient but if we be speaking of large scale I/O tasks  then it's best for asyncio while for heavy CPU tasks then it will be multiprocessing since it spawns independent processes to divide and calculate the workload used in rendering images, videos and other CPU intensive tasks.