#factorial
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n* factorial(n-1)
    
# print(factorial(3))
# print(factorial(4))
# print(factorial(5))

#fibonacci sequence
f0=0
f1=1
def fibo(n):
    if(n==0 ):
        return 0    
    elif(n==1):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
print(fibo(6))