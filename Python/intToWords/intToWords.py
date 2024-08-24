

from functools import cache
import gc


class Solution:
    def numberToWords(self, num: int) -> str:
        return int_to_words(num)


def int_to_words(num: int) -> str:
    if num == 0:
        return "Zero"

    appending_words = ["", "Thousand", "Million", "Billion"]

    ret_str = ''

    for word in appending_words:
        curr_eval = num % 1000
        eval_str = handle_larger(curr_eval, word)
        if ret_str == '':
            ret_str = eval_str
        elif eval_str != '':
            ret_str = f'{eval_str} {ret_str}'

        num //= 1000
        if num == 0:
            break

    gc.collect()
    return ret_str


def get_bottom_three_digits(num: int) -> int:
    return num % 1000


@cache
def handle_ones_no_zero(num: int) -> str:
    _tens = {
        0: '',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine'
    }
    return _tens.get(num)


def handle_teens(num: int) -> str:
    # gc.collect()
    match num:
        case 10:
            return "Ten"
        case 11:
            return "Eleven"
        case 12:
            return "Twelve"
        case 13:
            return "Thirteen"
        case 14:
            return "Fourteen"
        case 15:
            return "Fifteen"
        case 16:
            return "Sixteen"
        case 17:
            return "Seventeen"
        case 18:
            return "Eighteen"
        case 19:
            return "Nineteen"
    _teens = {
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen',
    }

    return _teens.get(num)


def handle_2_digits(processed_num: int) -> str:
    if processed_num < 10:
        return handle_ones_no_zero(processed_num)
    elif processed_num < 20:
        return handle_teens(processed_num)
    else:
        ones_processed_num = processed_num % 10
        ones_str = handle_ones_no_zero(ones_processed_num)
        processed_num //= 10
        tens_str = handle_tens(processed_num)
        return f'{tens_str} {ones_str}' if ones_str != '' else tens_str


def handle_3_digits(processed_num: int) -> str:
    bottom_2 = processed_num % 100
    bottom_res = handle_2_digits(bottom_2)
    processed_num //= 100

    hundreds_res = handle_hundreds(processed_num)
    if hundreds_res == '':
        return bottom_res

    return f'{hundreds_res} {bottom_res}' if bottom_res != '' else hundreds_res


@cache
def handle_tens(processed_num: int) -> str:

    match processed_num:
        case 0:
            return ""
        case 1:
            return "Ten"
        case 2:
            return "Twenty"
        case 3:
            return "Thirty"
        case 4:
            return "Forty"
        case 5:
            return "Fifty"
        case 6:
            return "Sixty"
        case 7:
            return "Seventy"
        case 8:
            return "Eighty"
        case 9:
            return "Ninety"


def handle_hundreds(processed_num: int) -> str:
    return f'{handle_ones_no_zero(processed_num)} Hundred' if handle_ones_no_zero(processed_num) != '' else ''


def handle_larger(processed_num: int, appending_str: str) -> str:
    hundreds_res = handle_3_digits(processed_num)
    if appending_str == '':
        return hundreds_res
    elif hundreds_res == '':
        return ''
    else:
        return f'{hundreds_res} {appending_str}'
