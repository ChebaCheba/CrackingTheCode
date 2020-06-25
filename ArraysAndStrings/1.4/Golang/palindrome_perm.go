package main

import (
	"fmt"
	"bufio"
	"os"
	"strings"
)

func is_palindrome(word string) bool {
	wordS := strings.TrimSpace(word)
	wordS = strings.ReplaceAll(wordS, " ", "")
	wordS = strings.ToLower(wordS)
	temp := make(map[byte]struct{})
	for i, _ := range wordS {
		if _, ok := temp[wordS[i]]; ok {
			delete(temp, wordS[i])
		} else {
			temp[wordS[i]] = struct{}{}
		}
	}
	if len(temp) > 1 {
		return false
	}
	return true
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Introduce a word")
	word, _ := reader.ReadString('\n')

	is := is_palindrome(word)
	if is {
		fmt.Println("It is a palindrome!")
	} else {
		fmt.Println("It is not a palindrome :(")
	}
}