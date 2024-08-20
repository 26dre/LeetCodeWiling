from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nth_triangle_result: int = (len(nums)*(len(nums) + 1)) / 2
        list_additive: int = 0
        for number in nums:
            if number > 0:
                list_additive += number

        return int(nth_triangle_result - list_additive)
