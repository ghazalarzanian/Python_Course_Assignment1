from cgitb import reset
from unittest import result


Side1 = float(input("Enter side 1: "))
Side2 = float(input("Enter side 2: "))
Side3 = float(input("Enter side 3: "))
result = "false"
if Side1 + Side2 > Side3 and Side1 + Side3 > Side2 and Side2 + Side3 > Side1:
    result = "true"
print(result)
