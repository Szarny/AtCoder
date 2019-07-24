package main

import "fmt"

type Town struct {
	name string
	popu int
}

func main() {
	towns := make([]Town, 0)

	var N int
	fmt.Scanf("%d", &N)

	var name string
	var popu int
	for i := 0; i < N; i++ {
		fmt.Scanf("%s %d", &name, &popu)
		towns = append(towns, Town{name, popu})
	}

	sumPopu := func(towns []Town) int {
		total := 0
		for _, town := range towns {
			total += town.popu
		}
		return total
	}(towns)

	for _, town := range towns {
		if town.popu*2 > sumPopu {
			fmt.Println(town.name)
			return
		}
	}

	fmt.Println("atcoder")
}
