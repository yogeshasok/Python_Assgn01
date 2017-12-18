import sys
a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]
if(a>b and a>c):
    big = a
elif(b>a and b>c):
    big = b
else :
    big = c
print "Greatest of ",a , b ,c ,"is ", big
