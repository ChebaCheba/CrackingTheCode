package main

import (
	"fmt"
	"os"
	"bufio"
)

func is_unique(word string) bool {
	unique := make(map[string]bool)
	for _, char := range word {
		if _, ok := unique[string(char)]; !(ok) {
			unique[string(char)] = true
		} else {
			return false
		}
	}
	return true

}

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Introduce a string")
	word, _ := reader.ReadString('\n')

	var uniqueness = is_unique(word)
	if uniqueness {
		fmt.Println("It has only unique characters")
	} else {
		fmt.Println("It does not have only unique characters")
	}
}