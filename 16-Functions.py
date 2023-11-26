# Function Definition
# def sum(a,b):
#     print("The Sum Of",a,"and",b,"is",a+b)

# Function Call
# c=int(input("Enter 1st number:"))
# d=int(input("Enter the 2nd Number:"))
# sum(c,d)

# return statment
# def sum(a,b):
#     return a+b

# c=sum(5,5)
# print(c)

# Function With Default Arguments
# def avg(a=9,b=1):
#     print("The Avergage is",(a+b)/2)

# avg()       #Defaultly excutes for a=9 and b=1
# avg(5,1)    #Ignores a=9 and b=1 and takes a=5 and a=1

# keyword arguments
# avg(b=10,a=6)   #we can change th order of the arguments

# variable length arguments
# def avg(*numbers):  Here numbers is a tuple
#     print(type(numbers))
#     sum=0
#     for i in numbers:
#         sum=sum+i
#     print("Average Is :",sum/len(numbers))
# avg(5,6)       with the help of this way,we can pass howmuchever values we want to find the average
# avg(5,6,7)


