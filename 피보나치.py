n = int(input())

result =[0,1]
def Fibo(n):
    
    for i in range(1,n):
        result.append(result[i-1]+result[i])
    
    return result

print(Fibo(n)[n])