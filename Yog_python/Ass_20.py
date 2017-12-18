limit = int(input("Enter the limit to generate Fibo series "))
li =[0,1]
a = 0
b = 1
c = 0
res=0
while(c<limit):
    li.append(a+b)
    res=a+b
    print res
    a = b
    b = res
    c = c+1

print li
