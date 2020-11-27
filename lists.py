#lists help to assign multiple values to variables
friends = ["Hoyo","Zaks","Ahmedo","Abdinasir","Mustafa","Abdallah","Space",1342,9.5,True]
#printing value of the whole list
print(friends)
#printing values of the list at certain index positions
print(friends[0])
print(friends[6])
print(friends[-1])
#printing the values of lists from certain starting positions to certain end points
print(friends[1:3])
print(friends[0:-1])
#the values in a list are not immutable and can be changed
friends[2] = "Ahmedi"
print(friends[2])
names = ['Mike','Kiran','John']
print(names)
#combining two lists together
combined_lists = [friends,names]
print(combined_lists)
#adds an element to the end of the list
names.append('Navin')
print(combined_lists)
#adds an element to a certain index position in the list
friends.insert(2,77)
#removes a certain element of the list
friends.remove("Mustafa")
friends.pop(1)
#removes the last element
friends.pop()
#deletes a certain portion of the list
del names[2:]
print(combined_lists)
#adds multiple values.use the .extend keyword
names.extend([29,12,14,36])
print(names)
#some inbuilt functions for performing certain list arithmetic operations(minimum number,maximum number,sum of the numbers and sorting the list)
numbers = [1,2,5,4,3]
print(min(numbers),max(numbers),sum(numbers))
numbers.sort()
print(numbers)


