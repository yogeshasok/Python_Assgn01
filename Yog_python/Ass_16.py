num = int(input("Enter the number to be checked"))
i = 2
count = 0
if (num ==2):
    print "Number is Prime"
elif(num==3):
    print "Number is Prime"
else:
    while(i<=num):
        if(num%i==0):
            count= count+1;
        i = i+1;
    if(count==1):
        print "Number is Prime"
    else:
        print "Number is not prime"


div,nu = 2,4
lim = int(input("Enter limit to generate prime numbers "))
pri = [2,3]
dummy = 0
while(nu<=lim):
    dummy = 0
    div = 2
    while(div<=nu):
        if(nu%div==0):
            dummy = dummy+1
        div =div +1
    if(dummy==1):
        pri.append(nu)
    nu = nu+1

print pri
