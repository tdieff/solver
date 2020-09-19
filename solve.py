from helpers import (isoperation, isnumber, isvariable, get_next_number, 
					 evaluate_and_update_lists, get_values_and_operation, get_inverse_operation)


def solve_using_postfix_lists(variable_side, otherside):
	values = []

	while len(variable_side) > 1: 

		token = variable_side.pop(0)

		if isnumber(token) or isvariable(token): values.append(token)

		elif isoperation(token): 

			value1, value2, operation = get_values_and_operation(values, token)

			if isnumber(value1) and isnumber(value2): 
				num1 = value1
				num2 = value2
				evaluate_and_update_lists(num1, num2, operation, values)

			elif isnumber(value1) and isvariable(value2): num2 = value1

			elif isvariable(value1) and isnumber(value2): num2 = value2

			operation = get_inverse_operation(token)
			num1 = otherside
			otherside = eval(f"{num1}{operation}{num2}")
				
			if len(variable_side) > 0:
				for i, token in enumerate(variable_side):
					if isnumber(token):
 						variable_side[i] = str(eval(f"{token}{operation}{num2}"))

			if len(values) > 0:
				for i, num in enumerate(values):
					if isnumber(str(values[i])): 
						values[i] = str(eval(f"{num}{operation}{num2}"))

	if len(values) > 0:
		remaining_operation = variable_side[0]
		num1 = otherside
		value = values.pop()
		if isnumber(value): num2 = value
		else: 
			num2 = values.pop()
			if remaining_operation == '/': return eval(f"{num2} / {num1}")
			elif remaining_operation == '-': return eval(f"{num2} - {num1}")			
		operation = get_inverse_operation(remaining_operation)
		return eval(f"{num1}{operation}{num2}")
	else: return otherside
