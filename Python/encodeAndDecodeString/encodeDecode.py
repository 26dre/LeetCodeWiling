from typing import List

EMBEDDING = '\\0'


class Solution:

    def encode(self, strs: List[str]) -> str:
        ret_str = ''
        for s in strs:
            ret_str += s
            ret_str += EMBEDDING

        print(ret_str)
        return ret_str

    def decode(self, s: str) -> List[str]:
        l = list()
        curr_string = ''
        i = 0
        while i < len(s):
            if s[i] not in EMBEDDING or (s[i] != EMBEDDING[0] and s[i + 1] != EMBEDDING[1]):
                curr_string += s[i]
            else:
                l.append(curr_string)
                curr_string = ''
                i += 1

            i += 1
        return l


if __name__ == '__main__':
    s = Solution()
    l = s.encode(['hello', 'World'])
    print(s.decode(l))
