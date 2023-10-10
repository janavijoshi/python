# WAP to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number.

a=input("enter hours: ")
a= float(a)
b=input("enter rate: ")
b=float(b)
if a >= 40:
    print(a * b)
elif a < 40:
    print(40 * (a * b) * 1.5)
else:
    print(" ")