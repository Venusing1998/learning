package main

import (
	"strings"
	"golang.org/x/tour/wc"
)

func WordCount(s string) map[string]int {
	m := make(map[string]int)
	//_s := make([]string, 0)
	//_s = strings.Split(s, " ")
　　  _s := strings.Fields(s)
	for _, value := range _s {
		v, ok := m[value]
		if ok {
			v += 1
		} else {
			v = 1
		}
		m[value] = v
	}
	return m
}

func main() {
	wc.Test(WordCount)
}