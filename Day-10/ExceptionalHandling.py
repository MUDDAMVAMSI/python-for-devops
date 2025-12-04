a = 10
b = 0
print(a / b)

#Output
#ZeroDivisionError: division by zero
=======================================

#With exception handling:
a = 10
b = 0

try:
    print(a / b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
 
#Output    
#Error: Cannot divide by zero.
