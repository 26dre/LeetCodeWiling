from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = dict()
        for number in nums:
            if x.get(number) != None:
                x[number] += 1
            else:
                x[number] = 1

        print(x)
        return sorted(x.keys(), key=x.get, reverse=True)[0:k]
