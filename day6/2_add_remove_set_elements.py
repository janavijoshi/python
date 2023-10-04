#set doesnt support indexing and slicing because set is unordered
a=[1,2]
b=[2,1]
print(a==b) #False

a={1,2}
b={2,1}
print(a==b) #True

#add()
#only one value can be added to the set using add()
s={1,2,3}
s.add(4)
print(s) #{1,2,3,4}

#update()
#can add multiple values to the set using update()
s={1,2,3}
s.add([4,5,6])
print(s) #{1,2,3,4,5,6}

#remove()
s={1,2,3,4,5,6}
s.add(4)
print(s) #{1,2,3,5,6}
s.remove(8) #it raises error

#discard()
s={1,2,3,4,5,6}
s.add(4)
print(s) #{1,2,3,5,6}
s.remove(8) #it doesnt raise error

#pop()
s={1,2,3,4,5,6}
s.pop()
print(s) #randomly pops out any one element from the set

#clear()
s.clear()
print(s) #{}

