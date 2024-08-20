package main

import "fmt"

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func createTreeNode(curr_val int, left_ch *TreeNode, right_child *TreeNode) *TreeNode {

	new_node := TreeNode{Val: curr_val, Left: left_ch, Right: right_child}
	fmt.Println("making a new Treenode with ", curr_val, left_ch, right_child)
	return &new_node
}

func createBinaryTree(descriptions [][]int) *TreeNode {

	var possible_parent *TreeNode = nil
	possible_parents := make(map[int]*TreeNode, len(descriptions))
	// tree_nodes_list := make([]*TreeNode, len(descriptions))
	int_to_node := make(map[int]*TreeNode)

	for i := 0; i < len(descriptions); i += 1 {
		// new_thing := createTreeNode(descriptions[i][0], nil, nil)
		// int_to_node[descriptions[i][0]] = new_thing
		curr_node, c_node_exists := int_to_node[descriptions[i][0]]

		if !c_node_exists {
			curr_node = createTreeNode(descriptions[i][0], nil, nil)
			possible_parents[descriptions[i][0]] = curr_node
			int_to_node[descriptions[i][0]] = curr_node
		} else {
			delete(possible_parents, descriptions[i][0])
		}

		if descriptions[i][1] != 0 {

			if left_child, l_c_exists := int_to_node[descriptions[i][1]]; l_c_exists {
				int_to_node[descriptions[i][0]].Left = left_child
			} else {
				left_child = createTreeNode(descriptions[i][1], nil, nil)
				int_to_node[descriptions[i][1]] = left_child
			}
		}
		if descriptions[i][2] != 0 {
			if right_child, r_c_exists := int_to_node[descriptions[i][2]]; r_c_exists {
				int_to_node[descriptions[i][0]].Left = right_child
			} else {
				right_child = createTreeNode(descriptions[i][2], nil, nil)
				int_to_node[descriptions[i][2]] = right_child
			}
		}
	}

	for _, node := range possible_parents {
		possible_parent = node
		break
		//this statement should never run with more than 1 parent as all non parents would be eliminated
	}

	return possible_parent
}

func stupid_shit() {
	fmt.Println("This is stupid shit")
	fmt.Println("This is a weird way to make this shit work it's like c but not it's kinda resepcatgvel lwk")
}
