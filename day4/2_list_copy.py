#copy() method creates a new copy of the exisiting list

a=[1,2,3]
b=a
print(a) #[1,2,3]
print(b) #[1,2,3]

a.append(4)
print(a) #[1,2,3,4]
print(b) #[1,2,3,4]

#copy()
a=[1,2,3]
b=a.copy() #is not same as b=a;
print(a) #[1,2,3]
print(b) #[1,2,3]

a.append(4)
print(a) #[1,2,3,4]
print(b) #[1,2,3]

#shallow opy()
a=[[1,2,3],4,5]
b=a.copy()
print(a) #[[1,2,3],4,5]
print(b) #[[1,2,3],4,5]

a[0][1]=7
print(a) #[[1,7,3],4,5]
print(b) #[[1,7,3],4,5]
#shallow copy() will only change the mutable items in the list.

#deep copy()
from copy import deepcopy
a=[[1,2,3],4,5]
b=deepcopy(a)
print(a) #[[1,2,3],4,5]
print(b) #[[1,2,3],4,5]

a[0][1]=7
print(a) #[[1,7,3],4,5]
print(b) #[[1,2,3],4,5]
