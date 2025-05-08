# Define the greater-than function
def greater_than(x, y):
    if x > y:
        return True
    else:
        return False

# First test case
a = 2
b = 3
result = greater_than(a, b)
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))

# Second test case
a = 10
b = 6
result = greater_than(a, b)
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))
