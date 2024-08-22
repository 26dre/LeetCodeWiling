

class Solution:
    def numberToWords(self, num: int) -> str:
        tmp_str = ""

        if num == 0:
            return "Zero"

        first_2_digits = num % 100
        num //= 100

        tmp_str += handle_below_100(first_2_digits)

        tens = handle_tens(num)
        tens += tmp_str
        tmp_str = tens
        tmp_str += handle_hundos(num)
        tmp_str += handle_thousands(num)
        tmp_str += handle_thousands(num)
        tmp_str += handle_millis(num)
        tmp_str += handle_billis(num)

        return tmp_str


def numToWords(num: int) -> str:
    tmp_str = ""

    if 10 <= num % 100 < 20:
        tmp_str += handle_teens(num)
    else:
        tmp_str += handle_ones(num)

    return tmp_str


def handle_below_100(processed_num: int) -> str:
    # processed num must be <= 99
    if 10 <= processed_num % 100 < 20:
        return handle_teens(processed_num)
    else:
        tens = handle_tens(processed_num)
        if len(tens) > 0:
            return tens + " " + handle_ones(processed_num)
        else:
            return handle_ones(processed_num % 10)


def handle_ones(num: int) -> str:
    num %= 10
    match num:
        case 1:
            return "One"
        case 2:
            return "Two"
        case 3:
            return "Three"
        case 4:
            return "Four"
        case 5:
            return "Five"
        case 6:
            return "Six"
        case 7:
            return "Seven"
        case 8:
            return "Eight"
        case 9:
            return "Nine"
        case 0:
            return ""


def handle_tens(num: int) -> str:

    # num /= 100
    num %= 100
    # get last two digits of number, then remove the last one anyway
    num //= 10

    match num:
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


def handle_teens(num: int) -> str:
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


def handle_hundos(processed_num: int) -> str:

    if processed_num == 0:
        return ""

    # tmp: str = handle_ones(processed_num)
    # tmp += " Hundred"
    tmp: str = handle_ones(processed_num)
    tmp += " Hundred"

    print(f'Tmp = {tmp}')
    if len(tmp) > 0:
        return tmp
    else:
        return ""


def handle_bases_larger_than_hundos(num: int, variable_base: int, appending_string: str) -> str:
    if variable_base <= 3:
        return ValueError
    num %= 10**variable_base
    num //= (10**(variable_base - 3))

    if num == 0:
        return ""

    tmp: str = handle_hundos(num)
    tmp += appending_string
    return tmp


def handle_thousands(num: int) -> str:
    num %= 1_000_000
    num //= 1_000

    if num == 0:
        return ""

    tmp = handle_hundos(num)
    tmp += " Thousand"


def handle_millis(num: int) -> str:
    num %= 1_000_000_000
    num //= 1_000_000

    if num == 0:
        return ""

    tmp = handle_hundos(num)
    tmp += " Million"


def handle_billis(num: int) -> str:
    num %= 1_000_000_000
    num //= 1_000_000

    if num == 0:
        return ""

    tmp = handle_hundos(num)
    tmp += " Billion"


def handle_three_digits(processed_num: int) -> str:
    bottom_two_digits = processed_num % 100
    processed_num //= 100
    processed_num %= 10
    hundos = handle_hundos(processed_num)
    if len(hundos) > 0:
        return hundos + " " + handle_below_100(bottom_two_digits)
    else:
        return handle_below_100(bottom_two_digits)


def handle_large_digits(processed_num: int, appending_string: str) -> str:
    res = handle_hundos(int)

    return res + " " + appending_string if len(res) > 0 else ""


def handle_thousands(processed_num: int) -> str:
    return handle_large_digits(processed_num, "Thousand")


def handle_millions(processed_num: int) -> str:
    return handle_large_digits(processed_num, "Million")


def handle_billions(processed_num: int) -> str:
    return handle_large_digits(processed_num, "Billion")
