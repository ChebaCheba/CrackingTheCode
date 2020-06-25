package main

import (
	"fmt"
	"os"
	"bufio"
	"math"
)

func one_away(word1, word2 string) bool {
	if math.Abs(float64(len(word1)-len(word2))) > 1 {
		return false
	}
	count1 := 0
	count2 := 0
	diff := 0

	for count1<len(word1) && count2<len(word2) {
		if diff>1 {
			return false
		}
		if word1[count1] == word2[count2] {
			count1++
			count2++
		} else {
			diff++
			if word1[count1+1] == word2[count2+1] {
				count1++
				count2++
			} else if word1[count1+1] == word2[count2] {
				count1++
			} else if word1[count1] == word2[count2+1] {
				count2++
			} else {
				return false
			}
		}
	}
	if diff > 1 {
		return false
	} 
	return true
}

func main(){
	reader := bufio.NewReader(os.Stdin)
	word, _ := reader.ReadString('\n')
	word2, _ := reader.ReadString('\n')

	one := one_away(word, word2)

	if(one){
		fmt.Println("They are one away")
	} else {
		fmt.Println("They are not one away")
	}
}