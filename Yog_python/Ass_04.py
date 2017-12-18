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
