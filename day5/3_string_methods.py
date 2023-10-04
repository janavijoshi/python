#1. capitalize()
messsage="hello world"
result=messsage.capitalize()
print(result) #"Hello world"

#2. title()
result=messsage.title()
print(result) #Hello World

#3. upper()
result=messsage.upper()
print(result) #HELLO WORLD

#4. lower()
result=messsage.lower()
print(result) #hello world

#5. split()
messsage="Hello World"
result=messsage.split()
print(result) #["Hello", "World"]

result=messsage.split("o")
print(result) #['Hell', ' W', 'rld']

result=messsage.split("l")
print(result) #['He', '', 'o Wor', 'd']

#6. join()
data=["Hello", "World"]
result="-".join(data)
print(result) #Hello-World

data=["Hello", "World"]
result=" ".join(data)
print(result) #Hello World
#data.join(" ")  #it raises error because join() should be called with string object not with list

#7. find()
message="hello world"
result=message.find('w')
print(result) #6 #index of the first letter

result=message.find('rld')
print(result) #8

result = message.find("wold")
print(result)  #-1 #if the world cannot be found it will always display -1

#8. replace()
message="hello world"
result=message.replace("hello","Hello")
print(result) #Hello world
