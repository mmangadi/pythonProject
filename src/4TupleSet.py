# Tuple is almost same as list, but you can't change the values in tuple. It's immutable

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tup)
print(type(tup))

print(tup[1])
# TypeError: 'tuple' object does not support item assignment
# tup[2] = 3

# Set is the collection of unique elements
s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s)
print(type(s))
s1 = {1, 1 , 2, 3, 67, 88, 11, 11, 12, 15}
print(s1)