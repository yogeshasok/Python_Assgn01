# two list with one list is emp name and other with name
emp_id = [1,2,3,4,5,6,7,8,9,10]
emp_name = ['ab','cd','ef','gh','ij','kl','mn','op','qr','st']


# a) Print all the names
print"Employees Name List :"
for ele in emp_name:
    print ele

#b) Read index from user and display current name
ind = int(input("Enter index to be display"))
print "Employee Id and name of ", ind ,"is ",emp_id[ind] , emp_name[ind]

#c) Print names from 4 th to 9 th
print "From 4th to 9th is", emp_name[3:9]

#d)print from 3rd to last
print "From 3rd to last ", emp_name[2:]

# e) Repeat list
tim = int(input("Enter number of times you want to repeat"))
print emp_name*tim

#f) Concatenate two list
print "After Concatenation ",emp_id+emp_name


# g) Print side by side
for i in range(len(emp_id)):
    print emp_id[i],"is ", emp_name[i]
