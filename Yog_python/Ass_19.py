for i in range(1,101):
    if(i%2==0):
        if(i==50):
            break
        elif(i==10 or i==20 or i==30 or i==40 or i==50):
            continue
        else:
            print i


print"By using While loop"
num=0
while(num<=100):
    num =num +1
    if(num%2==0):
        if(num==90):
            break
        elif(num==60 or num==70 or num==80 or num==90 ):
            continue
        else:
            print num
