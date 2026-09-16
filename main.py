name = input("Enter your name: ")

maths = float(input("Enter Maths marks: "))
physics = float(input("Enter Physics marks: "))
computer = float(input("Enter Computer marks: "))

total = maths + physics + computer
percentage = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage, "%")