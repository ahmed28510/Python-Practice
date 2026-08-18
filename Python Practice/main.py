print("Hello world!")

# Arithmetic Operators
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# Relational Operators
a = 10
b = 5
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than or Equal:", a >= b)
print("Less Than or Equal:", a <= b)

# Assignment Operators
a = 10
print("Original value of a:", a)
a += 5
print("After a += 5:", a)
a -= 3
print("After a -= 3:", a)
a *= 2
print("After a *= 2:", a)
a /= 4
print("After a /= 4:", a)

# Logical Operators
x = True
y = False
print("And Operator:", "x and y:", x and y)
print("Or Operator:", "x or y:", x or y)
print("Not Operator:", "not x:", not x)

# Bitwise Operators
a = 10  # 1010 in binary
b = 6   # 0110 in binary
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)

# Membership Operators
my_list = [1, 2, 3, 4, 5]
print("Is 3 in my_list?", 3 in my_list)
print("Is 6 in my_list?", 6 in my_list)

# Identity Operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print("Is x the same object as y?", x is y)
print("Is x the same object as z?", x is z)

# Type Conversion
a = 10
b = 3.5
c = "100"

print("Integer to Float:", float(a))
print("Float to Integer:", int(b))
print("String to Integer:", int(c))
print("String to Float:", float(c))

# User Input
name = input("Enter your name: ")
print("Hello, " + name + "!")

