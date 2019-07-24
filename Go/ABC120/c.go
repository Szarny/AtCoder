package main

import (
	"fmt"
	"strings"
)

func main() {
	var S string
	fmt.Scanf("%s", &S)

	nZero := strings.Count(S, "0")
	nOne := strings.Count(S, "1")

	var ans int
	if nZero < nOne {
		ans = nZero
	} else {
		ans = nOne
	}

	fmt.Println(ans * 2)
}