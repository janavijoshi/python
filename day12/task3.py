# Write a Program (WAP) to input three numbers and find the greatest number among three.

a= int(input("enter 1 num"))
b= int(input("enter 2 num"))
c= int(input("enter 3 num"))
if a>b and a>c:
    print(a,"is greatest")
elif b>c and b>a:
    print(b,"is the greatest")
else:
    print(c,"is the greatest")

# all in one method
num1 = int(input("Enter a number "))
num2 = int(input("Enter a number "))
num3 = int(input("Enter a number "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is the greatest")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is the greatest")
else:
    print(f"{num3} is the greatest")