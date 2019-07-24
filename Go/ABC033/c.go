package main

import (
	"fmt"
	"strings"
)

func main() {
	var S string
	fmt.Scanf("%s", &S)
	L := strings.Split(S, "+")

	ans := 0

	for _, l := range L {
		if strings.Count(l, "0") == 0 {
			ans += 1
		}
	}

	fmt.Println(ans)
}
