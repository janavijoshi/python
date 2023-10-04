#tuples in python can be packed and unpacked

#tuple packing
a=1, #this is tuple packing
print(a)
a=2,3,4 #this is also tuple packing
print(a)

vowels="a","e","i","o","u"
print(vowels) #("a","e","i","o","u")

#tuple unpacking
a,b,c=2,3,4
print(a) #2
print(b) #3
print(c) #4

#errors in tuple packing and unpacking
#a,b=2,3,4 #too many values to unpack
#a,b,c=1,2 #not enough values to unpack

#swapping two values in python
a=1
b=2
print(a)
print(b)

a=1
b=2
c=a
a=b
b=c
print(a)
print(b)

a=1
b=2
a,b=b,a
print(a) #2
print(b) #1
