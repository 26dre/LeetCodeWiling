from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret_list: List[List[int]] = list()
        print(nums)

        for initial in range(len(nums) - 2):

            val: int = nums[initial]
            if val > 0:
                break
            if initial > 0 and nums[initial] == nums[initial - 1]:
                continue
            left = initial + 1
            right = len(nums) - 1
            target = -val  # makes val positive

            while left < right:
                res: int = nums[left] + nums[right]
                if res < target:
                    left += 1
                elif res > target:
                    right -= 1
                else:
                    ret_list.append([nums[initial], nums[left], nums[right]])
                    left += 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return ret_list
