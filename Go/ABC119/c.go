package main

import (
	"fmt"
)

func main() {
	var N, A, B, C int
	fmt.Scanf("%d %d %d %d", &N, &A, &B, &C)

	var l int
	L := make([]int, 0)
	for i := 0; i < N; i++ {
		fmt.Scan(&l)
		L = append(L, l)
	}

}
