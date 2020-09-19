# solver
Author: Taylor Dieffenbach

Written in Python, 'Solver' is a command-line program that solves a variety of simple user-input 'solve-for-x' equations.

To give it a try, please 'cd' into the 'solver' directory and execute 'python main.py' in the terminal. 
I execute 'python3 main.py' in Terminal (from within the 'solver' directory) on my machine (running iOS).

Included in the directory 'solver' should be 7 files:

	(1)	README.md
	(2) 	DESIGN.md
	(3)	input.py
	(4)	postfix.py
	(5)	solve.py
	(6)	helpers.py
	(7)	main.py

These files work together, and should all remain in the 'solver' directory.

These 5 Python source code files , understood in the order that they are listed above (items 3, 4, 5, 6, and 7), 
represent the highest level of abstraction of the program. In order for the program to do what it is intended to do, 
we need 'input' that gets converted to 'postfix' notation, which is used to 'solve' a simple equation for a variable of the user's choice
--all with the help of some 'helper' functions. 
A human can interact with all of the pieces via 'main.' 
Again--executing 'python3 main.py' in Terminal on an machine running iOS will do the trick (assuming that you're in the 'solver' directory).

As a brief preamble, the program prints some playful info and instructions, then prompts the user to enter an equation at the command-line.

The program supports solving for 'x' for equations like any of the following:

x + a = b
x - a = b
x * a = b
x / a = b

a + x = b
a - x = b
a * x = b
a / x = b

a * x + b = c
a * x - b = c

x * a + b = c
x * a - b = c

b + a * x = c
b - a * x = c

...	as well as any of the above, with left and right side flipped (e.g. 'c = x * a - b' etc.)

...	for any real numbers 'a', 'b', and 'c', with at most 2 operations. Anything else--no promises. 

Equations with division and another operation not supported.

Multiplication must be declared explicitly ('2x = 4' not supported; use '2 * x = 4').

Grouping symbols are not supported.

Exponents are not supported.

Valid input may contain whatever whitespace you like, or none:

	'3				*x + 2 =  7'
	'3*x+2=7' and
	'3 * x + 2 = 7'
	
	will all be solved successfully.

In the event that the user enter any other input, the program prints an error message with some details about the nature of the error, 
hopefully guiding the user in the direction of inputting a 'Solver'-supported equation. 
The program re-prompts the user for input until a valid equation is entered, without exiting.

Upon solving and reporting a solution to a 'Solver'-supported equation, the program will offer the option of 'playing again.' 
Enter 'y' to solve another equation (without repeating the preamble) or 'n' to exit.

Once more--to give it a try, please 'cd' into the 'solver' directory and execute 'python main.py' in the terminal 
(I execute 'python3 main.py' in Terminal (from within the 'solver' directory) on my machine (running iOS)).

Thank you!

- Taylor
