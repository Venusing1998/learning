package main

import "golang.org/x/tour/pic"

func Pic(dx, dy int) [][]uint8 {
    mat := make([][]uint8, dy)
    for i := 0; i < dy; i++ {
        mat[i] = make([]uint8, dx)
    }

    //draw
    for y, _ := range mat {
        for x, _ := range mat[y] {
            mat[y][x] = uint8(x ^ y)
        }
    }
    return mat
}

func main() {
    pic.Show(Pic)
}
