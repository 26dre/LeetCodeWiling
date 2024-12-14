class Solution:
    opening_symbols = ['(', '[', '{']
    curr_position = 0

    def isValidBasic(self, s: str) -> bool:
        ...

    def isValid(self, s: str) -> bool:

        print(f'Evaluating {s}, curr position = {self.curr_position}')
        while Solution.curr_position < len(s):
            if not Solution.verify_symbol(s):
                return False

        return True

    def verify_symbol(string_input: str) -> bool:
        print(f'Evaluating position {Solution.curr_position}')
        if string_input[Solution.curr_position] in Solution.opening_symbols:

            print(f'Identified {
                  string_input[Solution.curr_position]} as opening symbol')
            expected_closing_symbol = Solution.get_closing_symbol(
                string_input[Solution.curr_position])

            Solution.curr_position += 1
            op_res: bool = True

            if string_input[Solution.curr_position] in Solution.opening_symbols:
                op_res = Solution.verify_symbol(string_input)

            print(f'Searching for closing character {
                  expected_closing_symbol}, currently looking at {string_input[Solution.curr_position]}')

            correct_ending_symbol: bool = False
            if Solution.curr_position < len(string_input) and string_input[Solution.curr_position] == expected_closing_symbol:
                Solution.curr_position += 1
                correct_ending_symbol = True
            return op_res and correct_ending_symbol
        else:
            return False

    def get_closing_symbol(symbol: chr) -> chr:
        match symbol:
            case '(':
                return ')'
            case '[':
                return ']'
            case '{':
                return '}'
            case _:
                return ValueError(f'Argument provided of {symbol} not in {Solution.opening_symbols}')
