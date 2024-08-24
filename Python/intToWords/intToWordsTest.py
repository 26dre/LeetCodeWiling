from typing import List
import intToWords
import time
import sys


def test_wrapper(nums: List[int], nums_response: List[str], test_function):
    print()
    print(f'Running function: {test_function.__name__}')
    print(f'inputs = {nums}')
    print(f'expected results = {nums_response}')
    failed_tests = list()

    passed_test = True
    for num, num_response in zip(nums, nums_response):
        print(f'Running {test_function.__name__} with {num}: {num_response}')
        result = test_function(num)
        if result != num_response:
            sys.stderr.write(f"Failed test: {num}, received |{
                             result}| instead of |{num_response}| \n\n")
            passed_test = False
            failed_tests.append(num)
        else:
            print(f'successfully executed\n')

    if passed_test:

        print(f'SUCCESSFULLY EXECUTED {test_function.__name__}')
    else:

        sys.stderr.write(f'FAILED TEST: {test_function.__name__}\n\n')
        time.sleep(1)
        for test in failed_tests:
            sys.stderr.write(f'Failed tests: {test}\n')

    print()


def ones_test(input: int) -> str:
    return intToWords.handle_ones_no_zero(input)


def hundreds_test(input: int) -> str:
    return intToWords.handle_hundreds(input)


def below_hundred_test(input: int) -> str:
    return intToWords.handle_2_digits(input)


def three_dig_test(input: int) -> str:
    return intToWords.handle_3_digits(input)


def thousands_test(input: int) -> str:
    return intToWords.handle_thousands(input)


def generic_test(input: int) -> str:
    return intToWords.handle_larger(input, '')


def full_test(input: int) -> str:
    return intToWords.int_to_words(input)

# def three_dig_test_again


if __name__ == '__main__':
    # test_teens()
    # test_below_100()
    # test_hundreds()
    # test_wrapper(nums=[123, 111, 21, 999, 1, 0], nums_response=["One Hundred Twenty Three", "One Hundred Eleven",
    #  "Twenty One", "Nine Hundred Ninety Nine", "One", "Zero"], test_function=test_three_digs)
    # test_wrapper(nums=[0, 1, 2, 3, 4], nums_response=[
    #              '', 'One', 'Two', 'Three', 'Four'], test_function=ones_test)

    # test_wrapper(nums=[0, 10, 20, 30, 40, 21, 98, 14], nums_response=[
    #              '', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Twenty One', 'Ninety Eight', 'Fourteen'], test_function=below_hundred_test)

    # test_wrapper(nums=[1, 2, 9], nums_response=[
    #              "One Hundred", "Two Hundred", "Nine Hundred"], test_function=hundreds_test)

    # test_wrapper(nums=[0, 1, 22, 200, 942], nums_response=[
    #     "", "One", "Twenty Two", "Two Hundred", "Nine Hundred Forty Two"], test_function=three_dig_test)

    # test_wrapper(nums=[0, 1, 22, 200, 942], nums_response=[
    #     "", "One", "Twenty Two", "Two Hundred", "Nine Hundred Forty Two"], test_function=generic_test)

    # test_wrapper(nums=[1, 124, 139], nums_response=[
    #              "One Thousand", "One Hundred Twenty Four Thousand", "One Hundred Thirty Nine Thousand"], test_function=thousands_test)

    # test_wrapper(nums)

    test_wrapper(nums=[1, 124, 139, 200, 942, 1_111, 1_999_432, 2_000_000, 2_123_321_999, 1_000_010], nums_response=[
                 'One', 'One Hundred Twenty Four', 'One Hundred Thirty Nine', "Two Hundred", "Nine Hundred Forty Two", "One Thousand One Hundred Eleven",
                 "One Million Nine Hundred Ninety Nine Thousand Four Hundred Thirty Two", "Two Million", "Two Billion One Hundred Twenty Three Million Three Hundred Twenty One Thousand Nine Hundred Ninety Nine", "One Million Ten"], test_function=full_test)
