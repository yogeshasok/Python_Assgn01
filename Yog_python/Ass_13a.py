print "Enter the Four numbers"
big =0;
a = int(input("Enter number one "))
b = int(input("Enter number two "))
c = int(input("Enter number three"))
d = int(input("Enter number four"))
if(a>b and a>c and a>d):
        big = a
elif(b>a and b>c and b>d):
        big = b
elif(c>a and c>b and c>d):
        big = c
elif(d>a and d>b and d>c):
        big = d
print "Biggest of ", a , b , c , d ,"is ",big
