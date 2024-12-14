from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        result = 0
        for number in nums:

            result ^= number
            print(f'Result changed to : {result}')

        return result


if __name__ == '__main__':

    s = Solution()
    result = s.singleNumber([1, 2, 5, 4, 5, 6, 7, 2])
    print(f'Result = {result}')
    result = s.singleNumber([1, 2, 3, 4, 5, 6, 7, 3])
    print(f'Result = {result}')
    result = s.singleNumber([1, 2, 3, 4, 5, 6, 7, 7])
    print(f'Result = {result}')
