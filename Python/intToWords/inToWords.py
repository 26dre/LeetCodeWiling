def numberToWords(num: int) -> str:
    tmp_str = ""

    return tmp_str


def handle_ones(num: int) -> tuple[str, int]:
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
            return "Zero"


def handle_tens(num: int) -> str:

    # num /= 100
    num %= 100
    # get last two digits of number, then remove the last one anyway
    num //= 10

    match num:
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


def handle_10s(num: int) -> str:
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


def handle_hundos(num: int) -> str:
    num %= 1000
    num //= 100

    if num == 0:
        return ""

    tmp: str = handle_ones(num)
    tmp.join("Hundred")
    return tmp


def handle_bases_larger_than_hundos(num: int, variable_base: int, appending_string: str) -> str:
    if variable_base <= 3:
        return ValueError
    num %= 10**variable_base
    num //= (10**(variable_base - 3))

    if num == 0:
        return ""

    tmp: str = handle_hundos(num)
    tmp.join(appending_string)
    return tmp


def handle_thousands(num: int) -> str:
    num %= 1_000_000
    num //= 1_000

    if num == 0:
        return ""

    tmp = handle_hundos(num)
    tmp.join("Thousand")


def handle_millis(num: int) -> str:
    num %= 1_000_000_000
    num //= 1_000_000

    if num == 0:
        return ""

    tmp = handle_hundos(num)
    tmp.join("Million")


def handle_billis(num: int) -> str:
    num %= 1_000_000_000
    num //= 1_000_000

    if num == 0:
        return ""

    tmp = handle_hundos(num)
    tmp.join("Million")
