# input a number : 15
# divide by 3 : Fizz
# divide by 5 : Buzz
# divide by both 3 and 5: FizzBuzz
# print the number itself

a = int(input("enter a num"))
if a % 5 == 0 and 0 == a % 3:
    print("fizzzbuzzz")
elif a % 3 == 0:
    print("fizzz")
elif a % 5 == 0:
    print("buzzz")
else:
    print(a)
