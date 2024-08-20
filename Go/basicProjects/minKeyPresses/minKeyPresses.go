package minkeypresses

import "container/heap"

// An IntHeap is a min-heap of ints.
type letter_number struct {
	num    int
	letter byte
}

func new_letter_num(letter byte, num int) letter_number {
	x := letter_number{num: num, letter: letter}
	return x
}

type LetterNumberHeap []letter_number

func (h LetterNumberHeap) Len() int           { return len(h) }
func (h LetterNumberHeap) Less(i, j int) bool { return h[i].num < h[j].num }
func (h LetterNumberHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *LetterNumberHeap) Push(x any) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(letter_number))
}

func (h *LetterNumberHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func MinimumPushes(word string) int {
	// fmt.Println("hi")
	return minimumPushes(word)
}
func minimumPushes(word string) int {
	key_commonality := make(map[byte]int)
	int_heap := make(LetterNumberHeap, len(word))
	heap.Init(&int_heap)

	for _, character := range word {
		if _, char_in_map := key_commonality[byte(character)]; char_in_map {
			key_commonality[byte(character)] += 1
		} else {
			key_commonality[byte(character)] = 1
		}
	}

	for key, val := range key_commonality {
		new_ln := new_letter_num(key, val)
		heap.Push(&int_heap, new_ln)

	}
	total_num_clicks := 0

	for i := 0; len(int_heap) > 0; i++ {
		num_clicks_to_button := i/9 + 1
		curr_ln := heap.Pop(&int_heap).(letter_number)
		total_num_clicks += num_clicks_to_button * curr_ln.num // number of clicks to get to the button * the number of appearances for that letter
		// looking at it now couldve used a simpler intheap as the information required here only requires that the number of appearances be mentioned as information for the question

	}

	return total_num_clicks
}
