l=[3,5,6]
print(l)
print(type(l))
if 7 in l:
    print("Yes")
else: 
    print("No")


# List Comprehension
myList=[i for i in range(4)]
print(myList)
myList=[i*i for i in range(10) if i%2==0]
print(myList)
