package main

import (
	"fmt"
	"os"
	"bufio"
	"strings"
	"strconv"
	"bytes"
)

func string_comp(str string) string {
	count := 0
	curr_letter := str[0]
	buffer := bytes.Buffer{}

	for _, char := range str {
		if byte(char) == curr_letter {
			count++
		} else {
			buffer.WriteByte(curr_letter)
			buffer.WriteString(strconv.Itoa(count))
			curr_letter = byte(char)
			count = 1
		}
	}
	buffer.WriteByte(curr_letter)
	buffer.WriteString(strconv.Itoa(count))
	comprehension := buffer.String()
	fmt.Println(comprehension)
	if len(str) > len(comprehension) {
		return comprehension
	}
	return str
}

func main(){
	reader := bufio.NewReader(os.Stdin)
	word, _ := reader.ReadString('\n')
	word = strings.TrimSpace(word)

	comp := string_comp(word)

	fmt.Println(comp)
}