a = float(input("Enter the first number: "))
c = input("Enter the operator (+ or -): ")
b = float(input("Enter the second number: "))

if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
else:
    print("Invalid operator")

