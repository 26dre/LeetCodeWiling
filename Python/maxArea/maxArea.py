
from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left: int = 0
        right: int = len(heights) - 1
        curr_max: int = 0

        while left < right:
            curr_area = min(heights[left], heights[right])*(right - left)

            print(f'left = {left}, right = {right}, heights[left], heights[right] = {
                  heights[left], heights[right]}, area = {curr_area}')
            if curr_area > curr_max:
                curr_max = curr_area

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return curr_max
