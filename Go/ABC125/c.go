package main

import (
	"fmt"
	"sort"
	"math"
)

func concat(A, B []int) []int {
	Z := []int{}

	for _, a := range A {
		Z = append(Z, a)
	}

	for _, b := range B {
		Z = append(Z, b)
	}

	return Z
}

func gcdseq(A []int) int {
	g := A[0]

	for i := 1; i < len(A); i++ {
		g = gcd(g, A[i])
	}

	return g
}

func gcd(x, y int) int {
	if x % y == 0 {
		return y
	} else {
		return gcd(y, x % y)
	}
}

func main() {
	var N int
	fmt.Scanf("%d", &N)

	A := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scanf("%d", &A[i])
	}
	
	sort.Sort(sort.Reverse(sort.IntSlice(A)))

	minAns := math.MaxInt64
	minIdx := -1

	for i := 0; i < len(A)-1; i++ {
		if g := gcd(A[i], A[len(A)-1]); g < minAns {
			minAns = g
			minIdx = i
		}
	}

	gcd1 := gcdseq(concat(A[:minIdx], A[minIdx+1:]))
	gcd2 := gcdseq(A[:len(A)-1])

	if gcd1 > gcd2 {
		fmt.Println(gcd1)
	} else {
		fmt.Println(gcd2)
	}
}