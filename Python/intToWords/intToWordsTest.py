from typing import List
import intToWords


def test_teens(n1: int = 14, n1_ans: str = "Fourteen"):
    print("Running test teens with", n1)
    test_word = intToWords.handle_below_100(n1)
    print("Test word result =\t", test_word)
    assert test_word == n1_ans, True

    print("Passed test teens\n")


def test_below_100(nums: List[int] = [14, 15, 28, 99, 1], nums_response: List[str] = ["Fourteen", "Fifteen", "Twenty Eight", "Ninety Nine", "One"]) -> None:
    print("Running test below 100\n")

    for num, num_response in zip(nums, nums_response):
        print("Running test teens with", num)
        test_word = intToWords.handle_below_100(num)
        print("Test word result = ", test_word, "\texpected : ", num_response)
        assert test_word == num_response, True

        print("Passed test" + str(num) + '\n')


def test_hundreds(nums: List[int] = [1, 1, 2, 9, 1], nums_response: List[str] = ["One Hundred", "One Hundred", "Two Hundred", "Nine Hundred", "One Hundred"]) -> None:
    print("Running test hundos\n")

    for num, num_response in zip(nums, nums_response):
        print("Running test hundreds with", num)
        test_word = intToWords.handle_hundos(num)
        print("Test word result = ", test_word, "\texpected : ", num_response)
        assert test_word == num_response, True

        print("Passed test" + str(num) + '\n')


def test_three_digs(nums: List[int] = [123, 111, 21, 999, 1], nums_response: List[str] = ["One Hundred Twenty Three", "One Hundred Eleven", "Twenty One", "Nine Hundred Ninety Nine", "One"]) -> None:
    print("Running test hundos\n")

    for num, num_response in zip(nums, nums_response):
        print("Running test hundreds with", num)
        test_word = intToWords.handle_three_digits(num)
        print("Test word result = |", test_word,
              "|\texpected : |", num_response)
        assert test_word == num_response, True

        print("Passed test " + str(num) + '\n')


if __name__ == '__main__':
    # test_teens()
    # test_below_100()
    # test_hundreds()
    test_three_digs()
