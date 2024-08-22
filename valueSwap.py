# this code will switch the two values entered by the user

value1 = int(input('Enter a value:'))
value2 = int(input('Enter a second value:'))
print()

print(f'The first number value is {value1} and the second number value is {value2}.')
print()

# the trick here is the arithmetic to find how to switch the values

value1 = value1+value2
value2 = value1-value2
value1 = value1-value2

print(f'After the swap, the value of the first variable is {value1}.\nThe value of the second variable is {value2}.')
