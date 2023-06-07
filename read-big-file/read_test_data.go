package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"log"
	"os"
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
	// Store highest counts in descending order
	//var countListDescendingOrder []int64
	var urlMap = map[int64]string{}

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

		heap.Push(&h, count)
		urlMap[count] = url

		if len(h) > 10 {
			minHeap := heap.Pop(&h)
			delete(urlMap, minHeap.(int64))
		}
	}

	for _, v := range h {
		fmt.Println(v)
	}
	fmt.Println()
	for k, v := range urlMap {
		fmt.Println(k, v)
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
