package main

import (
	"fmt"
	"bufio"
	"bytes"
	"os"
)

func urlify(originalURL string) string {
	buffer := bytes.Buffer{}
	for _, char := range originalURL {
		if char == ' ' {
			buffer.WriteString("%20")
		} else {
			if char != '\n'{
				buffer.WriteByte(byte(char))
			}
		}
	}
	return buffer.String()
}

func main(){
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Introduce URL")
	word, _ := reader.ReadString('\n')

	url := urlify(word)

	fmt.Println("URL: "+url)
}