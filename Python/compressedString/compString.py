
def comp_string_helper(word: str, max_consecutive: int = 9) -> tuple[str, int]:

    curr_letter = word[0]
    curr_consecutive = 0
    for letter in word:
        if curr_letter == letter and curr_consecutive < max_consecutive:
            curr_consecutive += 1
        else:
            break

    return tuple([curr_letter, curr_consecutive])


class Solution:
    def compressedString(self, word: str) -> str:

        ret_str = []

        while word:
            chr_res, int_res = comp_string_helper(word)
            ret_str.append(str(int_res))
            ret_str.append(chr_res)

            word = word[int_res:]

        return ''.join(ret_str)
