#Write a program which takes radius as an input and calculate the area of the circle.  Pi*r**2
a=int(input("radius"))
area=(3.14*a**2)
print(area)

#Write a program to find the frequency of the input number in a list 
#[5, 2, 3, 5, 3, 2, 3, 3, 1, 4]
a=[5, 2, 3, 5, 3, 2, 3, 3, 1, 4]
num=int(input("number giv"))
result=a.count(num)
print(f"{num} is repeated {result} times")
