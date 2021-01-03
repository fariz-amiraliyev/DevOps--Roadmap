
# Python program to demonstrate
# lmabda functions


def power(n):
    return lambda a : a ** n

# base = lambda a : a**2 get
# returned to base
base = power(2)

print("Now power is set to 2")

# when calling base it gets
# executed with already set with 2
print("8 powerof 2 = ", base(8))

# base = lambda a : a**5 get
# returned to base
base = power(5)
print("Now power is set to 5")

# when calling base it gets executed
# with already set with newly 2
print("8 powerof 5 = ", base(8))



# Python program to demonstrate
# lambda functions inside map()
# and filter()


a = [100, 2, 8, 60, 5, 4, 3, 31, 10, 11]

# in filter either we use assignment or
# conditional operator, the pass actual
# parameter will get return
filtered = filter (lambda x: x % 2 == 0, a)
print(list(filtered))

# in map either we use assignment or
# conditional operator, the result of
# the value will get returned
maped = map (lambda x: x % 2 == 0, a)
print(list(maped)) 
