#1 Arithmetic operator: +, -, *, / etc.
a=2
b=3
c=a+b
print(c)

#2 Assignment operator: =, +=, -= etc.
a = 4-2 # Assign 4-2 in a
print(a)

b=4
b = b+4
# b +=3
print(b)

#3 Comparison operators: ==(equal to), >, <, != etc.  
# return value is  always boolean.

d = 5 < 4
print(d)

#4 Logical operators: and, or, not.

e = True or False # e = 1 or 0
print(e)

# Truth table of 'or'
print("True or False is ", True or False)
print("True or False is ", True or True)
print("True or False is ", False or True)
print("True or False is ", False or False)

# Truth table of 'and'
print("True and False is ", True and False)
print("True and False is ", True and True)
print("True and False is ", False and True)
print("True and False is ", False and False)

# not operator
print(not(True))
print(not(False))