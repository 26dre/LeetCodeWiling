package codents

const OpenParen = '('
const CloseParen = ')'
const Add = '+'
const Subtract = '-'
const Multiply = '*'
const Divide = '/'
const Modulus = '%'

func calculate(s string) int {
	return 0
}

func get_number(s string, position int) (int, int) {
	// will return first the number at position position
	// next will return the new position at which to begin reevaluating the string
	return -1, -1
}

func skip_whitespace(s string, position int) int {
	// returns new position from which to evaluate string
	return -1
}

func evaluate_paren(s string, position int) int {
	return -1
}

func evaluate_addition(s string, position int) int {
	return -1
}
