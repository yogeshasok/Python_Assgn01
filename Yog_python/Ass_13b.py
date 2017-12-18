print "Enter the Four numbers"
big =0;
a = int(input("Enter number one "))
b = int(input("Enter number two "))
c = int(input("Enter number three"))
d = int(input("Enter number four"))
e = int(input("Enter number fifth"))

if(a>b and a>c and a>d and a>e):
        big = a
elif(b>a and b>c and b>d and b>e):
        big = b
elif(c>a and c>b and c>d and c>e):
        big = c
elif(d>a and d>b and d>c and d>e):
        big = d
elif(e>a and e>b and e>c and e>d):
        big = e;
print "Biggest of ", a , b , c , d , e ,"is ",big
