package minkeypresses

func minimumPushesBasic(word string) int {
	const numbers_to_use = 8

	accumulator := 0

	layer := 1
	for x := len(word); x > 0; x -= numbers_to_use {
		accumulator += x
		layer += 1
	}

	return accumulator

}

func MinimumPushesBasic(word string) int {
	return minimumPushesBasic(word)
}
