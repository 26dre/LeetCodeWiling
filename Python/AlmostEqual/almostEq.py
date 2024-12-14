from typing import List


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if self.compareBitches(nums[i], nums[j]):
                    res += 1
        return res

    def compareBitches(self, num1, num2) -> bool:

        num1List = list(map(int, str(num1)))
        num2List = list(map(int, str(num2)))

        print(f'Num 1 = {num1List}, Num 2 = {num2List}')

        # if len(set_dif) > 0:
        #     if len(set_dif) != 1 or 0 not in set_dif:
        #         return False

        while (len(num1List) < len(num2List)):
            num1List = [0] + num1List

        while (len(num2List) < len(num1List)):
            num2List = [0] + num2List

        num_diffs = 0

        for n1, n2 in zip(num1List, num2List):
            if n1 != n2:
                num_diffs += 1

        if num_diffs == 2 or num_diffs == 0:

            # print(f'Returns true on: \n {num1List}\t{num2List}')

            if sorted(num1List) == sorted(num2List):
                return True

        return False
