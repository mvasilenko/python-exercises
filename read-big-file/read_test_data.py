#!/usr/bin/env python3

import heapq

"""
input file sample

http://api.tech.com/item/121345  9
http://api.tech.com/item/122345  350
http://api.tech.com/item/123345  25
http://api.tech.com/item/124345  231
http://api.tech.com/item/125345  111

result = url list for 2 max values

http://api.tech.com/item/122345
http://api.tech.com/item/124345
"""
d = {
    "http://api.tech.com/item/121345": "9",
    "http://api.tech.com/item/122345": "350",
    "http://api.tech.com/item/123345": "250",
    "http://api.tech.com/item/124345": "231",
    "http://api.tech.com/item/125345": "111",
}


def process_heapq(filename: str, max_values: int) -> list:
    h = []
    with open(filename, "r") as f:
        for line in f:
            line_split = line.strip().split(" ")
            url, size = line_split[0], int(line_split[1])
            heapq.heappush(h, (size, url))
            if len(h) > max_values:
                heapq.heappop(h)

    result = [(t[1], t[0]) for t in h]
    # sort by value (size), not size
    return sorted(result, key=lambda item: item[1])


def process_dict(filename: str, max_values_count: int) -> list:
    values = []
    d = {}
    with open(filename, "r") as f:
        for line in f:
            line_split = line.strip().split(" ")
            url, size = line_split[0], int(line_split[1])
            # initial values list build
            if len(values) < max_values_count:
                values.append(size)
                values = sorted(values)
                d[url] = size
            else:
                # if size bigger than smallest value in values list
                # then replace it by current, and update dict with urls
                if size > values[0]:
                    # delete first (smallest by value) dict element
                    key = next(iter(d))
                    del d[key]
                    # add new size to dict
                    d[url] = size
                    # sort dict by size (value)
                    d = dict(sorted(d.items(), key=lambda item: item[1]))

                    # remove smallest value from values list
                    values.append(size)
                    values = sorted(values[1:])

    result = [(k, v) for k, v in d.items()]
    return result


if __name__ == "__main__":
    result1 = process_dict("test_data.tmp", 10)
    result2 = process_heapq("test_data.tmp", 10)
    for i in result1:
        print(i)
    print()
    for i in result2:
        print(i)
