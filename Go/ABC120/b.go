package main

import (
	"fmt"
	"sort"
)

func main() {
	var A, B, K int
	fmt.Scanf("%d %d %d", &A, &B, &K)

	D := make([]int, 0)

	var X int
	if A > B {
		X = B
	} else {
		X = A
	}

	for i := 1; i <= X; i++ {
		if A % i == 0 && B % i == 0 {
			D = append(D, i)
		}
	}

	sort.Sort(sort.Reverse(sort.IntSlice(D)))
	fmt.Println(D[K-1])
}