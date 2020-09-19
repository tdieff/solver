import re

from input import get_valid_equation_input
from helpers import isoperation, push, enque


# 'convert_equation_to_postfix_lists' is called in 'main.py' to tie in with the program as a whole
def convert_equation_to_postfix_lists(equation):
	leftlist, rightlist = break_expression_into_leftside_rightside_lists(equation)
	leftpostfix = generate_postfix_list(leftlist)
	rightpostfix = generate_postfix_list(rightlist)
	return leftpostfix, rightpostfix


# Format valid user-input equation into right and left expression lists
def break_expression_into_leftside_rightside_lists(equation):
	leftside_string, rightside_string = equation.split('=')
	leftlist = delimit_by_token(leftside_string)
	rightlist = delimit_by_token(rightside_string)
	return leftlist, rightlist

# A 'token' should be understood as an arbitrary number, variable, or operation
def delimit_by_token(expression_string):
	li = re.split(r"([\+\-\*\/a-zA-Z])", expression_string)
	for token in li:
		if token == '': li.remove(token) 
	return li


# 'enque' number- and variable-tokens to 'postfix' list, and...
# ... decide what to do with operation-tokens by calling 'allocate-operations'
def generate_postfix_list(expression_list):
	postfix = []
	opstack = []
	for token in expression_list:
		allocate_operation(token, postfix, opstack) if isoperation(token) else enque(token, postfix)
	while len(opstack) != 0: enque(opstack.pop(), postfix)
	return postfix
# 'postfix' lists will later later function as queues in 'solve.py'
# 'opstack' functions like a stack, list elements are popped off the top to generare 'postfix'


# 'enque' given operation-token to postfix queue 'postfix', or ...
# ... 'push' operation-token to operation stack 'opstack'
def allocate_operation(operation, postfix, opstack):
	if len(opstack) == 0 or order_ops(operation, t(opstack)) == operation: push(operation, opstack)
	else:
		while len(opstack) != 0 and order_ops(operation, t(opstack)) == t(opstack): 
			enque(opstack.pop(), postfix)
		push(operation, opstack)
	return


# Return the operation currently on the top of the operation stack
def t(opstack):
	return opstack[-1]


# Given a pair of operations, return the operation that has greater order of operations precedence
def order_ops(op1, op2):
	order = {'+': 0, '-': 0, '*': 1, '/': 1}
	return op1 if order[op1] > order[op2] else op2