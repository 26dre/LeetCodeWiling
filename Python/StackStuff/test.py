import validParens


def test_wrapper(string_input: str, expected_result: bool):
    print(f'Expected result {expected_result} on {string_input}')

    new_var = validParens.Solution()

    received_result = new_var.isValid(string_input)
    print(f'Received result : {received_result}')

    if received_result != expected_result:
        print("\033[31mReceived UNEXPECTED RESULT\033[0m")
