package main

import (
	"fmt"
	"os"
	"bufio"
)


func check_perm(word, word2 string) bool {
	count1 := 0
	count2 := 0
	word_set := make(map[byte]struct{})
	for {
		if count1 >= len(word) && count2 >= len(word2){
			break
		}
		char1 := word[count1]
		char2 := word2[count2]
		
		if _, ok := word_set[char1]; !(ok) {
			word_set[char1] = struct{}{}
		} else {
			delete(word_set, char1)
		}

		if _, ok := word_set[char2]; !(ok) {
			word_set[char2] = struct{}{}
		} else {
			delete(word_set, char2)
		}
		count1++
		count2++
	}
	if len(word_set)!=0 {
		return false
	}
	return true
}

func main(){
	reader := bufio.NewReader(os.Stdin)
	word, _ := reader.ReadString('\n')
	word2, _ := reader.ReadString('\n')

	is_perm := check_perm(word, word2)
	if(is_perm){
		fmt.Println("It is a permutation")
	} else {
		fmt.Println("It is not a permutation")
	}
}