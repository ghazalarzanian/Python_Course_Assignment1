Name = input("Enetr your name: ")
Family = input("Enter your family: ")
Course1 = float(input("Enter the score of course number 1: "))
Course2 = float(input("Enter the score of course number 2: "))
Course3 = float(input("Enter the score of course number 3: "))

Average = (Course1+Course2+Course3) / 3

if Average < 12:
    print("Fail")
if Average >=12 and Average<17:
    print("Normal")
if Average >= 17:
    print("Great")