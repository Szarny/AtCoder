package main

import (
	"fmt"
	"sort"
	"math"
)

func makeabs(A []int) []int {
	for i := 0; i < len(A); i++ {
		A[i] = int(math.Abs(float64(A[i])))
	}
	return A
}

func sum(A []int) int {
	s := 0
	for _, a := range A {
		s += a
	}
	return s
}

func minAbs(A []int) int {
	s := math.Abs(float64(A[0]))

	for i := 1; i < len(A); i++ {
		if t := math.Abs(float64(A[i])); t < s {
			s = t
		}
	}

	return int(s)
}

func main() {
	var N int
	fmt.Scanf("%d", &N)

	A := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scanf("%d", &A[i])
	}

	sort.Sort(sort.Reverse(sort.IntSlice(A)))

	n_neg := 0
	for _, a := range A {
		if a < 0 {
			n_neg++
		}
	}

	if n_neg % 2 == 0 {
		fmt.Println(sum(makeabs(A)))
	} else {
		fmt.Println(sum(makeabs(A)) - 2 * minAbs(A))
	}
}