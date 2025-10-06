from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from flyweight_glyphs import ThreadSafeFactory


glyph_refs = []
list_lock = Lock()  # protect glyph_refs

text = "a" * 200

def put_char_to_list(start, end):
    for i in range(start, end):
        ch = text[i]
        intr = ThreadSafeFactory.get_intrinsic(ch, "Roboto", 12, "regular")
        extrinsic = {"pos": i}
        # append safely
        with list_lock:
            glyph_refs.append((intr, extrinsic))


# Split work for threads
num_threads = 4
chunk_size = len(text) // num_threads
futures = []

with ThreadPoolExecutor(max_workers=num_threads) as executor:
    for t in range(num_threads):
        start = t * chunk_size
        # last thread handles remaining characters
        end = (t + 1) * chunk_size if t != num_threads - 1 else len(text)
        futures.append(executor.submit(put_char_to_list, start, end))

# Wait for all threads to finish
for f in futures:
    f.result()

print(f"Total glyphs: {len(glyph_refs)}")
