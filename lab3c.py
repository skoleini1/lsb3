#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: skoleini1

def operate(number1, number2, operator):
# Place logic in this function
	if operator == 'add':
		return int(number1) + int(number2)
	if operator == 'subtract':
		return int(number1) - int(number2)
	if operator == 'multiply':
		return int(number1) * int(number2)
	if operator == 'divide':
		 return 'Error: function operator can be "add", "subtract", or "multiply"'





if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))

