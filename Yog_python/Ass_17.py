print "Enter the number of Elements to be enetered"
lis = []
limit = int(input())
for i in range(limit):
    lis.append(int(input("Enter Element ")))
print lis

big = 0

for ele in lis:
    if(big<ele):
        big = ele
    else:
        continue
print "Biggest among N numbers is ", big
small = big
for ele in lis:
    if(small>ele):
        small = ele
    else:
        continue
print "Smallest among N numbers is ", small
