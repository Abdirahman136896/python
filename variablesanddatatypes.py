#creating a variable
character_name = "John"
character_age = "35"
is_male = True
#to get the address of the variable which is different for all variables
print(id(character_name))
print(id(character_age))
print("There once was a man named " + character_name + ",");
print("he was " + character_age + " years old.")
#variables are mutable so python allows changing of variable values at different parts of the program
character_name = "George"
character_age = "70"
print("He really liked the name " + character_name + ",")
print("but didn't like being " + character_age + ".")
#when you assign a value belonging to a variable to another variable the
# variables get the same address(Assigning the value of one variable to another
a = 10
b = a
print("a->"+str(id(a))+" b->"+str(id(b)) + " 10->"+str(id(10)))
#variables having the same value e.g constants is not applicable in python
#for example there is no way of making the value of PI = 3.14 the same throughout the program.
# The user is free to change
PI = 3.14
print(PI)
PI = 3.24
print(PI)
#to find out the data type of a specified variable
print(type(PI))