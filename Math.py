from Stack import Stack
import re
OPERATOR = '[+\\-/*%]'
PLUS_MINUS = '[+\\-]'
DIVIDE_MULTIPLY = '[/*]'
NUMBER = '[\\d.]'
PARENTHESES_OPEN = '\\('
PARENTHESES_CLOSED = '\\)'


def _calc(v1, v2, operator):  # Switch Statements
	if operator == '+':
		return v1 + v2
	if operator == '-':
		return v1 - v2
	if operator == '*':
		return v1 * v2
	if operator == '/':
		return v1 / v2
	if operator == '%':
		return v1 % v2
	if operator == '**':
		return v1 ** v2
	if operator == '//':
		return v1 // v2
	if operator == '++':
		return v1 + 1
	if operator == '--':
		return v1 + 1
	return None


def _calc_expression_stack(expression: Stack) -> int:
	running_val = 0
	current_operator = None
	while expression.height > 0:
		last_char = expression.pop().value
		if re.search(OPERATOR, last_char) is not None:
			current_operator = last_char
			if expression.top and re.search(PLUS_MINUS, expression.top.value) is not None:
				current_operator += expression.pop().value
				running_val = _calc(running_val, None, current_operator)
				current_operator = None
			elif expression.top and re.search(DIVIDE_MULTIPLY, expression.top.value) is not None:
				current_operator += expression.pop().value
		elif re.search(NUMBER, last_char) is not None:
			current_number = last_char
			while expression.top and re.search(NUMBER, expression.top.value) is not None:
				current_number += expression.pop().value
			current_number = float(current_number)
			if current_operator:
				running_val = _calc(running_val, current_number, current_operator)
				current_operator = None
			else:
				running_val = current_number
		elif re.search(PARENTHESES_OPEN, last_char):
			if current_operator:
				running_val = _calc(running_val, _calc_expression_stack(expression), current_operator)
			else:
				running_val = _calc_expression_stack(expression)
		elif re.search(PARENTHESES_CLOSED, last_char):
			return running_val

	return running_val


def calc_expression(expression: str) -> int:
	char_stack = Stack()
	for i in range(len(expression)):
		if expression[-(i + 1)] != ' ':  # last -> first so calculated left -> right
			char_stack.push(expression[-(i + 1)])
	return _calc_expression_stack(char_stack)


print(calc_expression(input('')))
