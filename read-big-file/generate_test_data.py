#!/usr/bin/env python3
import random

url_max = 10**5
value_max = 10**6

# generate 1000 chunks with 1000 text lines each
chunk_lines = 10000
chunk_count = 10
test_data = "test_data.txt"

with open(test_data, "w") as f:
    print("Generating test data chunk, please wait few seconds")
    data = ""
    for i in range(chunk_count):
        data += '\n'.join(
            f"http://api.example.com/{random.randint(0,url_max)} {random.randint(0, value_max)}" for i in range(chunk_lines))
        data += '\n'
    print("Outputing test data chunks to file")
    for j in range(chunk_count):
        f.write(data)
        # progress bar with dots
        print(".", end='', flush=True)
