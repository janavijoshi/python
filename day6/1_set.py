#set in python are mutable datatype. however, every element of a set must be immutable.
#set doesnt support indexing or slicing.
#set elements are always unique.
#set are unordered. {1,2} and {2,1} are the same.
#set are created by enclosing objects in curly brackets{}.

#Creating an empty set
a=set()
#a={} is not an empty set it is an empty dictionary.

#Creating non-empty set
data={1,2,3,4} #set of intergers and all elemets are immutable
fruits={"apple","mango","banana"} #set of strings and all elements are immutable
a={1,"a",(1,2),2.2} #set of mixed type but all elemets are immutable
print(a)

a={[1,2],"hello"} #invalid because set elements cant be mutable
a={(1,2,["hello","world"]),3} #this is not a valid set, it raises error
