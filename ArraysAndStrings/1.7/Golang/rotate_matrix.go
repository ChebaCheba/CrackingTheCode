package main

import (
	"fmt"
	"strconv"
	"bufio"
	"os"
	"strings"
	"math"
)

func rotate_matrix(m [][]int) {
	l := len(m)
	n := int(math.Floor(float64(l/2)))
	for i:= 0; i<n;i++ {
		last := l-i-1
		j := i
		for ;j<last;j++{
			offset := j-i
			top := m[i][j]
			m[i][j] = m[last-offset][i]
			m[last-offset][i] = m[last][last-offset]
			m[last][last-offset] = m[i+offset][last]
			m[i+offset][last] = top
		} 
	}
}

func print_matrix(m [][]int) {
	l := len(m)
	for i:=0;i<l;i++{
		for j:=0;j<l;j++{
			fmt.Printf("%d ", m[i][j])
		}
		fmt.Printf("\n")
	}
}

func init_matrix(num int) [][]int {
	matrix := make([][]int, num)
	for i:=0;i<num;i++{
		matrix[i] = make([]int, num)
		for j:=0;j<num;j++{
			matrix[i][j]=j+1
		}
	}
	return matrix
}

func main(){
	reader := bufio.NewReader(os.Stdin)
	number, _ := reader.ReadString('\n')
	number = strings.TrimSpace(number)
	num, err := strconv.Atoi(number)
	if err != nil {
		fmt.Println(err)
		os.Exit(2)
	}
	matrix := init_matrix(num)
	print_matrix(matrix)
	fmt.Println("")
	rotate_matrix(matrix)
	print_matrix(matrix)
}
