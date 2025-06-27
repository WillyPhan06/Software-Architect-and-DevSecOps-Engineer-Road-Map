import matplotlib.pyplot as plt

# Sample data structure – replace with your actual averages
url_counts = [1, 10, 100, 1000]

# Replace these with your real average time taken values
time_asyncio = [0.17, 13.64, 21.1, 29.6]
time_threading = [0.16, 14.41, 34.04, 74.23]
time_multiprocessing = [1.39, 12.27, 62.55, 634.48]
time_mix = [0.16, 11.84, 38.62, 223.25]

# Plot each method
plt.plot(url_counts, time_asyncio, marker='o', label='Asyncio')
plt.plot(url_counts, time_threading, marker='o', label='Threading')
plt.plot(url_counts, time_multiprocessing, marker='o', label='Multiprocessing')
plt.plot(url_counts, time_mix, marker='o', label='Mix (1/3 of each)')

# Labeling
plt.title("⏱️ Average Time Taken vs Number of URLs")
plt.xlabel("Number of URLs")
plt.ylabel("Average Time Taken (seconds)")
plt.xscale('log')  # Optional: Use log scale if gaps are huge
plt.grid(True)
plt.legend()

# Show it
plt.tight_layout()
plt.show()
