package twosumbst

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func FindTarget(root *TreeNode, k int) bool {
	return findTarget(root, k)
}

func findTarget(root *TreeNode, k int) bool {
	left_child := root
	right_child := root

	root_sum := root.Val * 2

	if root_sum > k {
		left_child = root.Left
	} else if root_sum < k {
		right_child = root.Right
	} else {
		right_child = root.Right
		left_child = root.Left
	}

	for sum := left_child.Val + right_child.Val; sum != k; {
		if sum < k {
			right_child = right_child.Right
		} else if sum > k {
			left_child = left_child.Left
		} else {
			return true
		}

		if left_child == nil || right_child == nil {
			return false
		}

		sum = left_child.Val + right_child.Val
	}

	return false
}
