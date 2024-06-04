# simple version of a lamba function

x = lambda a : 2 * a
print(x(2))

# Useful version of a lamba function
def multFunction(y):
    return lambda a : a * y

myDoubler = multFunction(2)
myTripler = multFunction(3)

print(myDoubler(2), myTripler(2))

