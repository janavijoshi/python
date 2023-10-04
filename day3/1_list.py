#python lists are mutable datatypes
#they are sequential datatypes enclosed in big brackets []

#unlike array, data inside a list may or may not be of the same type

#Creating an empty list
a=[]
b=list() #empty list using list() built in function


#creating a non-empty list
a=[1,2,3] #list with same/ homogenous datatypes
b=["hello", "python", 1, 2,[4,5]] #list with different/ heterogenous datatypes


##accessing list item##
#list items are accessed using indexing or slicing


#Indexing
#indexing in list starts from 0 for forward indexing and -1 for reverse indexing

vowels=["a","e","i","o","u"]
print(vowels[0]) #a
print(vowels[3]) #o
print(vowels[-1]) #u
print(vowels[-4]) #e

print(vowels[10]) #this raises IndexError
print(vowels[-7]) #this also raises IndexError

#Slicing
#Slicing is done using ':' with start and end values

values=["a","b","c","d","e","f","g","h","i","j"]
print(values[:5]) #["a","b","c","d","e"]
print(values[6:]) #["g","h","i","j"]
print(values[0:7]) #["a","b","c","d","e","f","g"]
print(values[3:7]) #["d","e","f","g"]
print(values[8:2]) #[]
print(values[2:8:2]) #["c","d","e"]

print(values[:-3]) #["a","b","c","d","e","f","g"]
print(values[:-6]) #["e","f","g","h","i","j"]
print(values[-8:-2]) #["c","d","e","f","g","h","i","j"]
print(values[-3:-9]) #[]

print(values[-9:6]) #["b","c","d","e","f"]

# taskwork
print(values[2:9])  # ["c", "d", "e", "f", "g", "h", "i"]
print(values[4:])  # ["e", "f", "g", "h", "i", "j"]
print(values[0:5])  # ["a", "b", "c", "d", "e"]
print(values[8:3])  # []
print(values[:6])  # ["a", "b", "c", "d", "e", "f"]
print(values[-8:-3])  # ["c", "d", "e", "f", "g"]
print(values[-2:-6])  # []
print(values[-9:7])  # ["b", "c", "d", "e", "f", "g"]
print(values[-9:-2:2])  # ["b", "d", "f", "h"]

#List Operations
#Concatenation (+)
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)  # [1, 2, 3, 4, 5, 6]

#Membership operation ("in" and "not in")
a = [1, 2, 3]
print(2 in a)  # True
print(3 not in a)  # False
print(5 in a)  # False


