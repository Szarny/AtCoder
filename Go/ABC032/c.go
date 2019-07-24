package main

import "fmt"

func main() {
	var N, K int
	fmt.Scanf("%d %d", &N, &K)

	var a int
	A := make([]int, 0)
	for i := 0; i < N; i++ {
		fmt.Scanf("%d", &a)
		A = append(A, a)
	}

	for _, v := range A {
		if v == 0 {
			fmt.Println(N)
			return
		}
	}

	var pi int
	for sublen := N; sublen >= 1; sublen-- {
		pi = func(L []int) int {
			r := 1
			for _, v := range L {
				r *= v
			}
			return r
		}(A[0:sublen])

		if pi <= K {
			fmt.Println(sublen)
			return
		}

		for i := 0; i < N-sublen; i++ {
			pi *= A[i+sublen]
			pi /= A[i]

			if pi <= K {
				fmt.Println(sublen)
				return
			}
		}
	}

	fmt.Println(0)
}
