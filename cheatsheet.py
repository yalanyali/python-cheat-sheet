import os # Os is the module name that refers to "os.py"

def main(): # The name "main" is just a convention, not a requirement. See the bottom of this script.
	print 'Hello world!' # Newline automatically added to print statements. Also no semicolons at the end of the line.

# No curly braces! Instead, the block starts when you add 4 spaces of indentation. (or any other amount, but 4 spaces is the standart)

	print "This is Alice's greeting."
	print 'This is Bob\'s greeting.' #Both quotes are fine. Either way, you don't have to escape the other kind of quote inside the string.

	foo(5,10) # Function call.

	print '=' * 10 # String replication. Evaluates to '=========='
	print 'Current working directory is ' + os.getcwd() # String concatenation. "os.getcwd()" calls a function in the os module.

	counter = 0 # Variables MUST be instaniated first.
	counter += 1

	food = ['apples', 'oranges', 'cats']
	# Lists can contain different data types in the same list, including other lists.

	for i in food: # For loop. "i" takes on each value in the list "food" in order.
	# Notice the one-line block. When the indentation goes back down, the block has ended.
		print 'I like to eat ' + i

	print 'Count to five: '
	for i in range(5): # The range() function returns a list like [0,1,2,3,4,5]. Don't forget the colon at the end!
		print i


def foo(param1, secondParam):
	res = param1 + secondParam

	print '%s plus %s is equal to %s' % (param1, secondParam, res) # String interpolation works basically the same way as it does in C.

	if res < 50:      # The comparison operators are the same as C.
		print 'foo'

	elif (res >= 50) and ((param1 == 42) or (secondParam == 24)): # Boolean operators are words, not && and ||. Also notice the colon at the end.
		print 'bar'

	else:
		print 'moo'

	return res # This is a one-line comment.
	''' A multi-
line string, but can also be a multi-line comment. '''
# Multi-line strings don't affect block indentation, though, only the indention at the start of the statement or expression.

if __name__ == '__main__':
	main()

''' We put a call to main() at the bottom so that each def statement is executed by the time we call main().
	This script's ___name___ variable has the value '___main___' only when the script is run, not imported.
	With this check, the main() function won't run if another script imports this script. '''
