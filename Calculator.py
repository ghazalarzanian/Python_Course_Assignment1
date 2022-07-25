import math

a = int(input("plese enter you first number: "))
b = int(input("please enter your second number: "))

op =input("Enter your operator + - * / radical sin cos tan cot factorial: ")

if op =="+":
    result= a + b
if op == "-":
    result= a - b
if op =="*":
    result= a * b
if op == "/":
    if b ==0:
        result = "oh No!!!"
        print("Error")
    else :
        result= a / b
if op == "radical":
    print(math.sqrt(a))
    result = math.sqrt(b)
###########################################
if op == "sin" or op == "cos" or op == "tan" or op == "cot" :
    a = math.radians(a)
    b = math.radians(b)
if op == "sin":
    print(math.sin(a))
    result = math.sin(b)
if op == "cot":
    print(math.cot(a))
    result = math.cot(b)
if op == "cos":
    print(math.cos(a))
    result = math.cos(b)
if op == "tan":
    print(math.tan(a))
    result = math.tan(b)
############################################
if op == "factorial":
    print(math.factorial(a))
    result = math.factorial(b)
print(result)