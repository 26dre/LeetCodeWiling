package pow

func Pow(x float64, n int) float64 {
	for range n - 1 {
		x *= x
	}

	return x
}
