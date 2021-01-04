n = int(input())

def factorial(n):
    mul = 1
    for i in range(1,n+1):
        mul = mul*i
    
    return mul

if n == 0:
    print(1)
else:    
    print(factorial(n))


