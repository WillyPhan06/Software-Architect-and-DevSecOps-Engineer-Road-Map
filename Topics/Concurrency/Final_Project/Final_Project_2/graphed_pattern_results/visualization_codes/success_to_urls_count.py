import matplotlib.pyplot as plt

# X-axis (log scale)
urls = [1, 10, 100, 1000]

# Replace these with your actual results
asyncio_dps = [0, 0.073, 1.66, 11.82]
threading_dps = [0, 0.069, 0.88, 4.51]
multiproc_dps = [0, 0.081, 0.54, 0.53]
mix_dps = [0, 0.084, 0.83, 1.52]

plt.figure(figsize=(20, 8))

plt.plot(urls, asyncio_dps, marker='o', label='Asyncio')
plt.plot(urls, threading_dps, marker='o', label='Threading')
plt.plot(urls, multiproc_dps, marker='o', label='Multiprocessing')
plt.plot(urls, mix_dps, marker='o', label='Mix (1/3 of each)')

plt.xlabel("Number of URLs", fontsize=14)
plt.ylabel("Average Successful Downloads Per Second", fontsize=14)
plt.title("⚡ Avg Downloads/sec vs Number of URLs", fontsize=16)
plt.legend()
plt.grid(True)
plt.xscale("log")

plt.tight_layout()
plt.show()
