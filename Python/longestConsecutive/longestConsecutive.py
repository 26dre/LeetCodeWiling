class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set: set[int] = set(nums)

        longest_streak = 0
        for n in nums:

            curr_streak_len = 1
            test_smaller = n - 1
            test_larger = n + 1

            while test_smaller in num_set:
                num_set.remove(test_smaller)
                test_smaller -= 1

            while test_larger in num_set:
                num_set.remove(test_larger)
                test_larger += 1

            curr_streak_len = (test_larger - 1) - (test_smaller)
            longest_streak = max(curr_streak_len, longest_streak)

        return longest_streak
