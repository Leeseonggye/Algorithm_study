n = int(input())
check =[]
for i in range(1,n+1):
    if i < 100:
        check.append(i)
    elif (i%10)+int(i/100) == 2*(i-i%10-int(i/100)*100)/10:
        check.append(i)

print(len(check))
