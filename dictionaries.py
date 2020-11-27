#A dictionary is a simple data structure that maps a dictionary
# name to a set of key/value of each element.
#creating a dictionary
monthlyConversions = {
#specify a key value pair.The key should be unique and should not be repeated and is immutable
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
    "None": "No",
}
#print the whole dictionary
print(monthlyConversions.items())#returns a list of tuples where each pair is the key and value
print(monthlyConversions)
#print only the keys
print(monthlyConversions.keys())
#print only the values
print(monthlyConversions.values())
#to iterate over the keys
for key in monthlyConversions.keys():
    print(key)
#to iterate over the dictionary using the items function
for key,value in monthlyConversions.items():
    print(key,value)
#to print specific values based on the keys provided
print(monthlyConversions["Jul"])
#also use the function get and specify the key to print the value
print(monthlyConversions.get("Dec"))
#if a key is not in the dictionary the program returns none
print(monthlyConversions.get("Luv"))
#to provide a statement if the key is not available in the dictionary add
# the statement after specifying the key
print(monthlyConversions.get("Luv","Not a valid key"))
#to remove the last key value pair in the dictionary use pop
print(monthlyConversions.pop("None"))
#converting the values of two lists into a dictionary(merging two lists into a dictionary
keys = ['navin','kiran','harsh']
values = ['python','java','javascript']
data = dict(zip(keys,values))
print(data)
#to add key-value pair to the above
data['Jamie'] = 'C++'
print(data)
#to delete a key-value pair in the dictionary
del data['harsh']
print(data)
#to define a list as value for a key in a dictionary and a dictionary as a value for a
# key within another dictionary
prog = {
    "JS": "Atom",
    "C++": "Visual Studio",
    "Python": ['Pycharm','Sublime'],
    "Java": {"JSE":"Netbeans","JEE":"Eclipse"},
}
print(prog)
print(prog['JS'])
print(prog['Python'])
print(prog['Python'][0])
print(prog['Python'][1])
print(prog['Java'])
print(prog['Java']['JSE'])
print(prog['Java']['JEE'])

