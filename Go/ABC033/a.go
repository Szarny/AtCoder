package main

import (
	"fmt"
	"strings"
)

func main() {
	var S string
	fmt.Scanf("%s", &S)

	if s := S[0]; strings.Count(S, string(s)) == 4 {
		fmt.Println("SAME")
	} else {
		fmt.Println("DIFFERENT")
	}
}
