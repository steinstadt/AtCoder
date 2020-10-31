package main

import (
	"fmt"
	"math"
)

func main() {
	// // Problem A
	// // input
	// var tmp string
	// fmt.Scan(&tmp)

	// // configuration
	// count := 0
	// ans := 0

	// // check
	// for i := 0; i < len(tmp); i++ {
	// 	if string(tmp[i]) == "R" {
	// 		count++
	// 		ans = count
	// 	} else {
	// 		ans = max(ans, count)
	// 		count = 0
	// 	}
	// }

	// // output
	// fmt.Println(ans)

	// // Problem B Making Triangle
	// // input
	// var n int
	// var nums []int
	// fmt.Scan(&n)
	// nums = scanNums(n)

	// // Process
	// if n < 3 {
	// 	fmt.Println(0)
	// } else {
	// 	var L1 int
	// 	var L2 int
	// 	var L3 int
	// 	var count int
	// 	for i := 0; i < (n - 2); i++ {
	// 		for j := i + 1; j < (n - 1); j++ {
	// 			for k := j + 1; k < n; k++ {
	// 				L1 = nums[i]
	// 				L2 = nums[j]
	// 				L3 = nums[k]
	// 				if isOk(L1, L2, L3) == true {
	// 					count++
	// 				}
	// 			}
	// 		}
	// 	}
	// 	fmt.Println(count)
	// }

	// Problem C - Walking Takahashi
	var x int
	var k int
	var d int
	fmt.Scan(&x)
	fmt.Scan(&k)
	fmt.Scan(&d)

	// process
	x = abs(x)
	count := x / d
	if k < count {
		x = abs(x - k*d)
		fmt.Println(x)
	} else {
		k = k - count
		x = abs(x - count*d)
		if k%2 == 0 {
			fmt.Println(x)
		} else {
			x = abs(x - d)
			fmt.Println(x)
		}
	}
}

func abs(a int) int {
	return int(math.Abs(float64(a)))
}

func isOk(n1 int, n2 int, n3 int) (ok bool) {
	return ((n1+n2 > n3 && n1+n3 > n2 && n2+n3 > n1) && (n1 != n2 && n2 != n3 && n3 != n1))
}

func scanNums(len int) (nums []int) {
	var num int
	for i := 0; i < len; i++ {
		fmt.Scan(&num)
		nums = append(nums, num)
	}
	return
}

func pow(p, q int) int {
	return int(math.Pow(float64(p), float64(q)))
}
