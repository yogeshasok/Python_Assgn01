name = ['yogesh','manish','muthu','gokul','praveen']
strg = raw_input("Enter the name to search ")

print "Using Membership Operator 'IN'"
if(strg in name):
    print "Name is present in list"
else:
    print "Name is not present in list"


print "Without Membership Operator"
if(name.count(strg)>0):
    print "Name is present"
else :
    print "Name is not present"
name.reverse()
print "Reversed List is " , name
