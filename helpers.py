import re


# used to allow user-input freedom, but still wind up with consistent formatting later
def remove_whitespace(string):
	return re.sub(r'\s+', '', string)


# used to rule out user input with unsupported symbols
def invalid_chars(string):
	unsupported_chars = []
	for char in string:
		if not isnumber(char) and not isvariable(char) and not isoperation(char) and char != '=' and char != '.':
			unsupported_chars.append(char)
	return unsupported_chars if len(unsupported_chars) > 0 else False


# returns true if string contains multiple consecutive operation symbols
def consecutive_operations(string):
	for i in range(len(string) - 1):
		if isoperation(string[i]) and isoperation(string[i + 1]): return True
	return False


# accomplishes same as the re.match, but hides distracting regex syntax
def isoperation(token):
	return True if re.match(r"^[\+\-\*\/]$", token) else False


# used to rule out user input with too many variables in 'input.py'
# used to determine which side of equation contains variable in 'main.py'
def get_variable_count(iterable_object):
	variable_count = 0
	for element in iterable_object:
		if isvariable(element): variable_count += 1
	return variable_count


# used to rule out user input with too many operation symbols
def get_operations_count(string):
	variable_count = 0
	for char in string:
		if isoperation(char): variable_count += 1
	return variable_count


# accomplishes same as the re.match, but hides distracting regex syntax
def isnumber(token):
	return True if re.match(r"^\d*(\.\d+)?$", token) else False


def isvariable(token):
	return True if token.isalpha() else False

# 'enque' token to 'postfix' list (which later functions as a queue)
def enque(token, postfix):
	postfix.append(token)
	return

# 'push' token tp 'opstack' list (which functions like a stack)
def push(token, opstack):
	opstack.append(token)
	return


def get_reverse_list(list1):
	return list1[::-1]


def get_next_number(li, i):
	return li[i + 1] if isnumber(li[i + 1]) else li[i + 2]


# 'evaluate_and_update_lists' runs a few errands for the central process in 'solve.py'
def evaluate_and_update_lists(value1, value2, operation, values):
	num1 = value1
	num2 = value2
	result = eval(f"{num1}{operation}{num2}")
	values.append(result)
	return


# 'get_values_and_operation' simplifies syntax in 'solve.py'
def get_values_and_operation(values, token):
	return values.pop(), values.pop(), token


# dictionary is keyed into with an operation-token
# returns a dictionary value (the inverse operation of the key)
def get_inverse_operation(operation):
	inverse_of = {'+': '-', '-': '+', '*': '/', '/': '*'}
	return inverse_of[operation]