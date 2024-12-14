from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tmp = 1

        zero_cntr = nums.count(0)

        if zero_cntr == 0:
            for num in nums:
                tmp *= num

            for i in range(len(nums)):
                nums[i] = tmp // nums[i]

        elif zero_cntr == 1:
            for num in nums:
                if num != 0:
                    tmp *= num

            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] = 0
                else:
                    nums[i] = tmp
        else:
            nums = [0 for num in nums]
        return nums
