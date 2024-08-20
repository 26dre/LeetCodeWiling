package node

type SinglyLinkedNode[T any] struct {
	value T
	next  *SinglyLinkedNode[T]
}

func NewSinglyLinkedNode(val any) *SinglyLinkedNode {

}

type DoublyLinkedNode[T any] struct {
	value T
	prev  *SinglyLinkedNode[T]
	next  *SinglyLinkedNode[T]
}
