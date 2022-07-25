import math
weight = int(input("Enter weight in Kilograms: "))
height = float(input("Enter height in metres: "))
height = math.pow(height,2)
print(height)
BMI = weight / height

if BMI <= 18.5:
    print("under wwight")
if BMI>18.5 and BMI<24.9:
    print("normal")
if BMI>25 and BMI<29.9:
    print("overwight")
if BMI>30 and BMI<34.9:
    print("obese")
if BMI>35 :
    print("extremely obese")
