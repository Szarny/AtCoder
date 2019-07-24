package main

import (
	"fmt"
)

func main() {
	var A, B, T int
	ans := 0

	fmt.Scan(&A, &B, &T)

	for t := A; t <= T; t += A {
		ans += B
	}

	fmt.Println(ans)
}