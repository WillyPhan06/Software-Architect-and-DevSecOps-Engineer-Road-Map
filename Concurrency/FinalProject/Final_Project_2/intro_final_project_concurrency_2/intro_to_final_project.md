This is the 2nd project in final projects of concurrency, for project 1 I already made a CLI (Command-Line Interface) concurrent downloader to download multiple websites concurrently using command lines in the terminal.

In this 2nd project, i reconstructed the project 1 all from scratch all from my understanding and memory, no help from AI code or other source code, just full understanding and memory from project 1 and in this 2nd project I also fix edge cases, potential bugs, and improvements such as:

1/ Adding timeout to prevent waiting for ever.

2/ Separate the log.txt to different folder to avoid naming confusion in the downloads folder.

3/ Add try accept to handle all possible errors gracefully.

4/ Add a method named "mix" which is basically all three model respectfully multiprocessing, threading, and asyncio and all of them are submitted in ThreadPoolExecutor to run concurrently. This method is a fun mix and worth benchmarking along with other ones for better behavior recognition among different benchmarks.

5/ Add log recorded how many successful/fail file after downloading in terminal for asyncio and threading. Unfortunately its not applied for multiprocessing since its not process safe.

6/ Added renaming logic in downloaded files to prevent overwriting existing files which leads to incorrect results, so basically i added in a while loop which will check for existing file name, if its already existed that file name then the counter goes up until not then the counter number will be added to the name to make it unique to avoid overwriting if its the same name.

7/ Update the log in log.txt to shoutout the name of the method that called for the log for better clarification through passing parameter of method name to the logger.py

8/ Added Lock() for both threading and asyncio to avoid race condition when updating successful/fail count of downloads as well as calling log action for log.txt

In this downloader I coded all threading, asyncio, multiprocessing, and mix models then benchmark them based on total time run and its successful downloads then rank them based on successful file downloaded per second and analyze them.

Btw there are logs for threading and asyncio downloads, but unfortunately there is no log for multiprocessing approach because its not process safe.

For more visualization you can check the high level diagram next to this to understand the big picture. Also check my benchmark results and my analysis! 😁
