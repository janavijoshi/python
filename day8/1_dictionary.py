#dictionary is a mutable datatype in python
#it is the datatype with key-value pair enclosed in curly brackets

#Creating an empty dictionary
a={}
print(a) #{}
a=dict() #using built in function
print(a) #{}

#Creating non-empty dictionary
a={"name":"Jon", "age":30}
print(a) #{"name":"Jon", "age":30}

a=dict(name="Jon", age=30)
print(a) #{"name":"Jon", "age":30}

a={"first name":"Jon", "last name":"Doe"} #this is correct
print(a)

#a=dict(first name:"Jon", last name:"Doe") #this is incorrect
a=dict(first_name:"Jon", last_name:"Doe") #we should connect words in keys
print(a)

#Accessing dictionary elements
student={"name":"Jane", "age":30,"address":"KTM"}
address=student['address']
print(address) #KTM
print(student["roll_no"]) #KeyError

name = student.get("name")
print(name)  #Jane
print(student.get("roll_no")) #None

#Adding and updating dictionary elements
student={"name":"Jon", "age":30,"address":"KTM"}
student=["roll_no"]=2
print(student) #{"name":"Jane", "age":30,"address":"KTM","roll_no":2}

student["name"]="Alex"
print(student) #{"name":"Alex", "age":30,"address":"KTM","roll_no":2}

student.update({"email":"jane@email.com","contact":4745313138})
print(studnet) #{"name":"Alex", "age":30,"address":"KTM","roll_no":2,"email":"jane@email.com","contact":4745313138}

student.update(email:"jane@email.com",contact:"4745313138")
print(student)

#Removing dictionary elements
student={"name":"Alex", "age":30,"address":"KTM","roll_no":2,
         "email":"jane@email.com","contact":4745313138}

student.pop("contact") #removes key item
print(student) #{"name":"Alex", "age":30,"address":"KTM","roll_no":2, "email":"jane@email.com"}
contact=student.pop("contact") #value return
print(contact) #4745313138

keyvalue=student.popitem() #removes the last item from dictionary #("email","jane@email.com")
print(student) #{"name":"Alex", "age":30,"address":"KTM","roll_no":2}
key,value=student.popitem()
print(key)
print(value)

student.clear()
print(student)  #{}

del student
print(student)  #NameError

#Restriction in dictionary keys
#all immutable objects can be used as a dictionary key
#there are no restrictions in dictionary values

data={1="Jon",4:"Doe"} #valid
print(data[4])

data = {1.1: "Jon", 3.2: "Doe"}  #Valid
data = {[1, 2]: "Ram", "age": 30}  #Invalid
data = {(1, 2): "Ram", "age": 30}  #Valid
data = {(1, [2, 3]): "Ram", "ages": [30, 31]}  #Invalid
