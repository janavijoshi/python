#we do string formatting using f-string

name="jon"
message=f"Hello I am {name}"
print(message) #Hello I am jon

name="jon doe"
age=23
message=f"Hello I am {name}, and I am {age} years old"
print(message) #Hello I am jon doe, and I am 23 years old

#using format specifier(%s, %d, %f, etc.)
print('I am %s and I am %d yeards old'%(name,age))

#using .format() method
print('I am {}'.format(name))
