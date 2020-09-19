SOLVER - 'DESIGN'
Author: Taylor Dieffenbach

Included in the directory 'solver' are 7 files:

	(1)	README.md
	(2) DESIGN.md
	(3)	input.py
	(4)	postfix.py
	(5)	solve.py
	(6)	helpers.py
	(7)	main.py

These files work together, and should all remain in the 'solver' directory. I execute 'python3 main.py' in Terminal 
(from within the 'solver' directory) on my machine (running iOS).




#DIRECTORY STRUCTURE
For purposes of project management, clarity to readers, and ease of adding features in the future, 
I broke up and named the 5 .py source code files very intentionally (items 3 through 7 above).

These 5 Python source code files , understood in the order that they are listed above (items 3, 4, 5, 6, and 7), 
represent the highest level of abstraction of the program. 
The names of which files offer, at a glance, some loose sense of what goes on in the program. 
In order for the program to do what it is intended to do, we need 'input' that gets converted to 'postfix' notation, 
which is used to 'solve' a simple equation for a variable of the user's choice--all with the help of some 'helper' functions. 
The pieces are tied together with 'main.' Again--executing 'python3 main.py' in Terminal on an iOS machine will do the trick 
(assuming that you're in the 'solver' directory).

Reading the function calls in the function called 'main' in the 'main.py' source code reveals more detail in the way of arguments 
to certain functions and return data. Also included in 'main.py' are a couple of functions called 'preamble' and 'offer_to_play_again', 
which briefly introduce and conclude the program by printing to the command-line for purposes of goofy user-experience.






#DOCUMENTATION
One goal of mine was to write 'self-documenting' code. As such, function and variable names are fairly verbose, 
but reveal the logical intentions behind their existence. I have since added a bunch of comments anyway.
In some cases, I think the comments in my code add clutter and make the logic harder to follow, but perhaps other readers would feel differently.

To this end, I have broken processes into shorter, easier-to-follow functions where possible. 
I have made extensive use of functions calling other functions to hide what I deem to be distracting syntax 
and relatively lower levels of abstraction in the logic. The result is code that more clearly distills key logic in the real 'problem-solving' functions. 
Even without documentation within the source code files, some parts of the code read easily to outline the processes that they acheive.

To offer insight on lower levels of of abstraction of the program, I will remark on notable functions in each of the 5 source code files:






#HELPERS
The functions contained in 'helper.py' are ones that I find fairly uninteresting, 
but are helpful to other functions in other files in one of a couple of ways. 

For example, 'isnumber' and 'isoperation' hide some ugly-looking regex stuff. 
To check if a given token is a supported operation, I find that 'isoperation(token)' reads much more smoothly than 're.match(r"^[\+\-\*\/]$", token)'.

Otherwise, functions in 'helpers.py' tend to be fairly rote, 
so I wanted to hide them so as not to clutter and add cognitive overhead to the logic of other more complex functions.

The helper functions are aides in layering abstraction and building self-documenting code.






#INPUT
The functions contained in 'input.py' get and validate user input. 

**The 'validate_input' function**...
...is sort of tricky in that it requires so many 'if-else' conditions. 
Here I have managed to in some sense rule out possible inputs that are either nonsense or not supported 
(and would thus trigger errors or incorrect results). There may still be some inputs that the program doesn't like.

My intent is for the program to support solving for 'x' for equations like any of the following:

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

'input.py' calls a handful of functions from 'helpers.py'






#POSTFIX
The functions in 'postfix.py' convert user-input equation to postfix notation via the 'Shunting-yard' algorithm. 
Postfix notation (also called 'reverse Polish notation') post-fixes an operation to the values that it (the operation) will operate on. I read up on Wikipedia.



**The 'generate_postfix_list' function**...
... accepts a mathematical expression in list form, delimited by token (a 'token' should be understood as an arbitrary number, variable, or operation). 
The function first declares the lists 'postfix' and 'opstack'. 
'postfix' lists will later later function as queues in 'solve.py'. 
'opstack' functions like a stack--list elements are popped off the top (most recently appended) to generare 'postfix'

**The 'enque' function** (from helpers) is called to append a given token to the 'postfix' list (which later functions as a queue).

**The 'push' function** (from helpers) is called to append a given token to the 'opstack' list (which functions like a stack).

**'generate_postfix_list'** iterates through each token in an expression formatted as a list, in order to:

- allocate all operations to 'postfix' or 'opstack', (see 'allocate_operation' function below)

- enque any other tokens (i.e. numbers and variables) to 'postfix' (see 'enque' function in helpers.py), and

- finally, 'pop' each remaining operation off the top of 'opstack' one at a time and 'enque' to 'postfix'

'generate_postfix_list' returns the resulting list 'postfix', which is the original expression accepted as an argument, 
but now formatted as a list in postfix notation.



**The 'order_ops' function** ... 
... accepts a pair of tokens (pre-determined to be operations) as arguments and returns the operation that has the greater order-of-operations precedence.

'op1' and 'op2' are used as keys to compare associated 'order' dictionary values, per 'order-ops' function calls in 'allocate_operation' 
(which is itself called by 'generate_postfix').

'op1' is the operation at current index of expression list, 'op2' is what currently sits at the top of 'opstack'.

Each next operation in the expression list (here, 'op1'), 
should only get pushed to 'opstack' on top of 'op2' when it has *greater* precedence than 'op2', 
because 'generate_postfix' concludes by popping each operation token from 'opstack' and enqueing to 'postfix', 
where operations are "first-in, first-out" (see Shunting-yard algorithm).

Thus higher precedence operations should sit at the top of 'opstack' to ultimately be evaluated before lower precedence operations, 
equal-precedence operations should be evaluated as they appear in order left-to-right in the original expression.



**The function 't'**...
... simply return the operation currently on the top of the operation stack (the list 'opstack'):

	def t(opstack):
		return opstack[-1]

Created for readability purposes when used in 'allocate_operation', 't' is not strictly necessary. 
't(opstack)'--pronounced in my head like 'topstack'--
is intended to be a quick and fun way to communicate the operation at the last element of the list 'opstack'. 
Many times have I encountered the coding advice 'don't be cute.' I recognize that bugs live in funny function names, but I like 't(opstack)'







#SOLVE
The single function in 'solve.py' calls a few functions from 'helpers.py' in order solve for the user-input-determined variable. 

**The function 'solve_using_postfix_lists'**...
...accepts two lists--left and right sides of the original equation (in postfix notation)--as arguments.

In a nutshell, it pops tokens from postfix lists, creates a list called 'values' to use almost like buffer, and does some bits and pieces of arithmetic. 

The long chain of various if-else conditions works according to standard order-of-operations-rules and equation-solving rules 
(given various other constraints in the program). 







#MAIN
The functions and function calls in 'main.py' tie the program together, from all its pieces in all its files. Works almost like a town-center.

**The 'preamble' function**...
... is for fun, but also orients user toward correct program use, even without the README background.

**The 'offer_to_play_again' function**...
... exists so that users can optionally solve multiple equations in a row without having to deal with that annoying *'preamble'* again.

I execute 'python3 main.py' in Terminal (from within the 'solver' directory) on my machine (running iOS).


