package main

import (
	"bufio"
	"log"
	"os"
)

func main() {

	readFile, err := os.Open("test_data.txt")
	defer readFile.Close()

	if err != nil {
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(readFile)
	for scanner.Scan() {

	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
