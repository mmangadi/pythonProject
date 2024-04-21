# Data Types in Python

# None
# Numeric [int, float, complex, bool]
# List
# Tuple
# String
# Range
# Dictionary


num = 2.5
print("type of num : " + str(num) + " = " + str(type(num)))
num = 5
print("type of num : " + str(num) + " = " + str(type(num)))
num = 6 + 3j
print("type of num : " + str(num) + " = " + str(type(num)))
a = 5.6
b = int(a)
print("")
print("type of a : " + str(a) + " = " + str(type(a)))
print("type of b : " + str(b) + " = " + str(type(b)))
c = float(b)
print("type of c : " + str(c) + " = " + str(type(c)))
print("")
k = 6
i = complex(b, k)
print("type of i : " + str(i) + " = " + str(type(i)))
print("")
bl = b < k
print("type of bl : " + str(bl) + " = " + str(type(bl)))
bl = b > k
print("type of bl : " + str(bl) + " = " + str(type(bl)))

print("")

lt = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("type of lt : " + str(lt) + " = " + str(type(lt)))
st = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print("type of st : " + str(st) + " = " + str(type(st)))
tp = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print("type of tp : " + str(tp) + " = " + str(type(tp)))

print()

name = "Pathmanathan"
print("type of name : " + str(name) + " = " + str(type(name)))
print()
x = list(range(10))
print(x[1])

print()
dt = {1: "manju", 2: "mahi", 3: "ravi"}
print("type of dt : " + str(dt) + " = " + str(type(dt)))
