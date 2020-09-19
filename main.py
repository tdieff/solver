import sys, time, random

from input import get_valid_equation_input
from postfix import convert_equation_to_postfix_lists
from solve import solve_using_postfix_lists
from helpers import get_variable_count


def main():

	equation, variable = get_valid_equation_input()

	leftpostfix, rightpostfix = convert_equation_to_postfix_lists(equation)

	if get_variable_count(leftpostfix) == 1:
		variable_side = leftpostfix
		otherside = rightpostfix[0]
	else:
		variable_side = rightpostfix
		otherside = leftpostfix[0]

	solution = solve_using_postfix_lists(variable_side, otherside)

	print(f"Your solution is: {variable} = {solution}")

	offer_to_play_again()


def offer_to_play_again():
	while True:
		response = input("Play again? (y / n) ")
		if response == 'y': return main() 
		elif response == 'n':
			time.sleep(0.25)
			print("Goodnight.\n\n\n")
			time.sleep(1)
			
			sys.exit("		         		...zzz.")
		else: print("Enter 'y' for yes, 'n' for no")


def preamble():
	time.sleep(0.8)

	text0 = "Welcome, "
	for i, char in enumerate(text0):
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.05)
	time.sleep(0.5)

	text1 = "h u m a n. "
	for char in text1:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.15)
	time.sleep(0.5)

	text2 = "This is Solver. We can solve equations of the following sort:"
	for char in text2:
		sys.stdout.write(char)
		sys.stdout.flush()
		r = 0.0001 * random.randint(1, 1500)
		time.sleep(r)
	time.sleep(0.25)

	text6 = "\n	     2 * x + 12 = 7"
	for char in text6:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.08)
	time.sleep(0.5)

	text7 = "\n 	       	   or"
	sys.stdout.write(text7)
	time.sleep(0.7)

	text8 = "\n    p - 3 = .14159265358979323846264338327950288419716939937510582097494459"
	for i, char in enumerate(text8):
		sys.stdout.write(char)
		sys.stdout.flush()
		t = 1 + (3 * i / 5)
		time.sleep(0.3 / t)
	time.sleep(1.5)
	
	print("\n")
	time.sleep(0.3)


preamble()
main()