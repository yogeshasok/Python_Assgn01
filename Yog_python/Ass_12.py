tot = 0
lis =[]
grt = []
les =[]
eql =[]
for i in range(10):
    lis.append(int(input("Enter the Elements")))
for i in lis:
    tot+=i
print "Total of numbers is ", tot
avg = tot/10;
print "Average of sum is ",avg
for ele in lis:
    if(ele>avg):
        grt.append(ele)
    elif(ele<avg):
        les.append(ele)
    else:
        eql.append(ele)

print "Elements greater than average were ",grt
print "Elements lesser than average were ",les
print "Elements equal to average were ",eql
