package main

import "fmt"

func isContain(L []string, t string) bool {
	for _, l := range L {
		if l == t {
			return true
		}
	}
	return false
}

func main() {
	var s string
	var k int

	fmt.Scanf("%s", &s)
	fmt.Scanf("%d", &k)

	L := make([]string, 0)

	for i := 0; i < len(s)-k+1; i++ {
		t := string(s[i : i+k])

		if !isContain(L, t) {
			L = append(L, t)
		}
	}

	fmt.Println(len(L))
}
