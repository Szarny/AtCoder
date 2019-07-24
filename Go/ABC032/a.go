package main

import "fmt"

func main() {
	var a, b, n int
	fmt.Scanf("%d", &a)
	fmt.Scanf("%d", &b)
	fmt.Scanf("%d", &n)

	for i := n; ; i++ {
		if i%a == 0 && i%b == 0 {
			fmt.Println(i)
			return
		}
	}
}
