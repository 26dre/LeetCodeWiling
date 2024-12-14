class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())

        print(s)

        start = 0
        end = len(s) - 1

        while start < end:

            print(f"Comparing {s[start]} to {s[end]}")
            if (s[start] != s[end]):
                return False

            start += 1
            end -= 1
        return True
