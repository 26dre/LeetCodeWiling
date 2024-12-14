from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            for i in range(len(code)):
                code[i] = 0
        elif k < 0:
            code.reverse()
            k = -k
            reversed_code = True
        else:
            reversed_code = False

        return decrypt(code, k)


def decrypt(code: List[int], k: int) -> List[int]:
    res_list = list()
    curr_sum = sum(code[-k:])
    res_list.append(curr_sum)

    for idx, frontier in enumerate(code):
        print(f'Curr sum = {curr_sum}')
        to_remove_idx = (idx - k) % len(code)
        to_remove = code[to_remove_idx]
        print(f'to_remove = {to_remove}')

        curr_sum = curr_sum + frontier - to_remove
        print(f'Curr sum = {curr_sum}')
        res_list.append(curr_sum)
        print(res_list)
    return res_list  # alias it because we want to return in place
