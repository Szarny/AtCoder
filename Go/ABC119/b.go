package main

import (
	"fmt"
)

func main() {
	var N int
	fmt.Scanf("%d", &N)

	ans := 0.0

	var x float64
	var u string
	for i := 0; i < N; i++ {
		fmt.Scan(&x)
		fmt.Scan(&u)

		if u == "JPY" {
			ans += x
		} else {
			ans += x * 380000.0
		}
	}

	fmt.Println(ans)
}
