from helpers import (remove_whitespace, invalid_chars, consecutive_operations, 
					 get_variable_count, get_operations_count, isoperation, isvariable, isnumber)

def get_valid_equation_input(): 
	while True:
		usr_input = input("Enter an equation: ")
		if validate_input(usr_input) != False: return validate_input(usr_input)

def validate_input(usr_input):
	usrinput = remove_whitespace(usr_input)
	if '=' not in usrinput:
		print("Invalid input: '=' not found")
		return False
	elif usrinput[0] == '=' or usrinput[-1] == '=':
		print("Invalid input: something is missing...")
		return False
	elif invalid_chars(usrinput) != False:
		unsupported_chars = invalid_chars(usrinput)
		print(f"Invalid input: unsupported character(s): {unsupported_chars}")
		return False
	elif consecutive_operations(usrinput):
		print("Invalid input: equation must not contain consecutive operation symbols")
		return False
	else: 
		variable_count = get_variable_count(usrinput)
		operations_count = get_operations_count(usrinput)
	
		if variable_count != 1:
			print(f"Invalid input: must contain exactly 1 instance of 1 variable, {variable_count} instances detected")
			return False
		elif operations_count > 2:
			print(f"Invalid input: up to 2 operations supported, {operations_count} instances detected")
			return False
		else:
			for token in usrinput:
				if token == '/' and operations_count == 2:
					print(f"Invalid input: equations with division and another operation not supported")
					return False
			for i in range(len(usrinput) - 1):
				if isvariable(usrinput[i]) and isnumber(usrinput[i+1]):
					print(f"Invalid input: multiplication must be declared explicitly with '*' (for example, 'q * 4' not 'q4')")
					return False
				if isnumber(usrinput[i]) and isvariable(usrinput[i+1]):
					print(f"Invalid input: multiplication must be declared explicitly with '*' (for example, '3 * x' not '3x')")
					return False
			else:
				left, right = usrinput.split('=')
				if isoperation(left[0]) or isoperation(right[0]) or isoperation(left[-1]) or isoperation(right[-1]):
					print("Invalid input: expression must not lead or conclude with operation")
					return False
	return usrinput, get_input_variable(usrinput)

def get_input_variable(eqn):
	for token in eqn:
		if isvariable(token): return token