package main

import (
	"fmt"
)

func main() {
	var A, B, C int
	fmt.Scanf("%d %d %d", &A, &B, &C)

	if able := B / A; able < C {
		fmt.Println(able)
	} else {
		fmt.Println(C)
	}
}