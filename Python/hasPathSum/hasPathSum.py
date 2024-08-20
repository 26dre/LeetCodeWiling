# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.preOrderAdv(root=root, util_fn=self.hasPathSumUtil, util_args=targetSum, util_target=0)

    def preOrderAdv(self, root: Optional[TreeNode], util_fn: Optional[function], util_args: Optional[any], util_target: Optional[any]) -> bool:
        if root != None:
            util_result = util_fn(util_args, util_target)
            if util_result == util_target:
                return True
            else:
                return self.preOrderAdv(root=root.left, util_fn=util_fn, util_args=util_result, util_target=util_target) \
                    or self.preOrderAdv(root=root.right, util_fn=util_fn, util_args=util_result, util_target=util_target)
        else:
            return False

    def hasPathSumUtil(curr: int, target: int) -> int:
        if type(curr) != int and type(target) != int:
            raise TypeError(
                "Hello motherfucker, you're using some trash ass arguments here you dumb bitch")
        return target - curr
