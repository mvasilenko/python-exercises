package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

// An IntHeap is a min-heap of ints.
type IntHeap []int64

func (h *IntHeap) Push(x interface{}) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(int64))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	item := old[n-1]
	*h = old[:n-1]
	return item
}

func (h IntHeap) Less(i, j int) bool {
	return h[i] < h[j]
}

func (h IntHeap) Len() int {
	return len(h)
}

func (h IntHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func main() {
    // peek top 10 values
	const topK = 10

	// store map of urls to topK values
	var urlMap = map[string]int64{}

	readFile, err := os.Open("test_data.txt")
	defer readFile.Close()

	if err != nil {
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(readFile)

	h := IntHeap{}

	for scanner.Scan() {

		// parse line delimited by whitespace
		line := scanner.Text()
		fields := strings.Fields(line)
		if len(fields) != 2 {
			continue
		}
		url := fields[0]
		count, err := strconv.ParseInt(fields[1], 10, 64)
		if err != nil {
			continue
		}

		// initial fill for heap
		if len(h) < topK {
			heap.Push(&h, count)
			urlMap[url] = count
			continue
		}
		// value is bigger then min in heap h[0] ?
		if count > h[0] {
			heap.Push(&h, count)
			urlMap[url] = count
			// pop out min value from the heap
			minHeap := heap.Pop(&h)
            // delete corresponding url from map of topK urls
			for k, v := range urlMap {
				if v == minHeap {
					delete(urlMap, k)
					break
				}
			}
		}
	}
    // create keys list from urlMap
	keys := make([]string, 0, len(urlMap))
	for key := range urlMap {
        keys = append(keys, key)
    }
    // sort map by value in descending order
	sort.Slice(keys, func(i, j int) bool { return urlMap[keys[i]] > urlMap[keys[j]] })
	for _, key := range keys {
        fmt.Printf("%s\n", key)
    }

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
