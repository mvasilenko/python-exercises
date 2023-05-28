#!/usr/bin/env python3
import random
import os

url_max = 10**4
value_max = 10**6

lines = 10**6
groups = 10**3

files_count = 10**3
tmp_file = "test_data.tmp"
data_file = "test_data.txt"

with open(tmp_file, "w") as f:
    for i in range(groups):
        data = '\n'.join(f"http://api.example.com/{random.randint(0,url_max)} {random.randint(0, value_max)}" for i in range(lines//groups))
        f.write(data)

with open(data_file, "w") as f:
    pass

print("small sample generated, populating")
for i in range(files_count):
    os.system(f"cat {tmp_file} >> {data_file}")
    print(".", end='', flush=True)

os.remove(f"rm -f {tmp_file}")
