math = input(":")
x,y,z = math.split(" ")
x = int(x)
z = int(z)
Add = x+z
Subtract = x-z
Division = x/z
Multiply = x*z
if y == "+":
    print (float(Add))
elif y == "-":
    print(float(Subtract))
elif y == "*":
    print(float(Multiply))
elif y == "/":
    print(float(Division))
else:
    print("i dont understand")