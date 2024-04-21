a = 5
b = 6

a = a + b
b = a - b
a = a - b

print("a = " + str(a))
print("b = " + str(b))

a = 5
b = 6
a = a ^ b
b = a ^ b
a = a ^ b
print("a = " + str(a))
print("b = " + str(b))

a = 5
b = 6

a, b = b, a
print("a = " + str(a))
print("b = " + str(b))