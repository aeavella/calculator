print 'Type in the sign of the operation you wish to perform.'
operation=raw_input('Operation sign:')
add='+'
sub='-'
mult='*'
div='/'
if operation==str(add):
	num1= input('First number:')
	num2= input('Second number:')
	def addingfunc(num1, num2):
		return num1+num2
	print addingfunc(num1, num2)
elif operation==str(sub):
	num1= input('First number:')
	num2= input('Second number:')
	def subingfunc(num1, num2):
		return num1-num2
	print subingfunc(num1, num2)
elif operation==str(mult):
	num1= input('First number:')
	num2= input('Second number:')
	def multingfunc(num1, num2):
		return num1*num2
	print multingfunc(num1, num2)
elif operation==str(div):
	num1= input('First number:')
	num2= input('Second number:')
	def divingfunc(num1, num2):
		return num1/num2
	print divingfunc(num1, num2)
else:
	print 'ERROR 404: FILE NOT FOUND'
	print 'Please enter an operation symbol.'