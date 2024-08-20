package kthdistinctstring

func kthDistinct(arr []string, k int) string {
	seen := make(map[string]bool)

	for _, val := range arr {
		if _, exists := seen[val]; !exists {
			seen[val] = false

		} else {
			seen[val] = true
		}

	}

	for _, val := range arr {
		if !seen[val] {
			k--
			if k == 0 {
				return val
			}
		}
	}

	return ""
}

func KthDistinct(arr []string, k int) string {
	return kthDistinct(arr, k)
}
