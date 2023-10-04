#string is an immutable datatype in python
#string is created using single(''),  ouble("") or triple("""/''') quotes in python
#a single character enclosed in quotes is also a string

#Creating an empty string
a=''  #single quotes
b="" #double quotes
c=""" """ #triple quote
d=''' ''' #triple single quotes
e=str() #using str() function

#Creating non-empty string
a='Hello'
b="World"
c="""
I am learning python.
python is a high level language
"""
d='''
I am learning python,
python is a high level language
'''

#we cant start with one quote and end with another quote in strings
#a='Hello World" #This is wrong

a='Hello World. I\'m learning python'
print(a)
#'\ is an escape sequence

b= "Hello\nWorld" #\n is an escape sequence
print(b)

c="Hello\tWorld" #\t is an escape sequence
print(c)
 
