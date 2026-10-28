a = float(input("Read a: "))
b=float(input("Read b: "))
operation=input("User Operation(+,-,*,/): ")
if(operation == "+"):
    result = a + b
elif(operation =="-"):
    result = a - b
elif(operation == "*"):
    result = a * b
elif(operation == "/"):
    result = a / b
 
print(f"{a}{operation}{b} = {result}")