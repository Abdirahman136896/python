#variables that is not assigned any value is known as none/null
#numeric data types
  #float variable
num = 2.5
print(type(num))
  #integer variable
num = 5
print(type(num))
  # complex variable
num = 6 + 9j
print(type(num))
#converting the value of a variable to integer
a = 5.6
b = int(a)
print(a,b)
print(type(b))
#converting the value of a variable to float
k = float(b)
print(k)
print(type(k))
#to convert the value of variable from integer into complex number
k = 6
c = complex(b,k)
print(c)
  #boolean variable
num = b<k
print(num)
print(type(num))
#list variable
lst = [25,36,45,12]
print(type(lst))
#set variable
set = {25,36,45,12}
print(type(set))
#tuple variable
tuple = (25,36,45,12)
print(type(tuple))
#string variable
string = "mike"
print(type(string))
#range
print(list(range(0,10)))
print(list(range(0,11,2)))
print(type(range(0,10)))
#dictionary variable
dic = {
    "Mike":"Samsung",
    "Jose":"iPhone",
    "Pogba":"Oppo",
}
print(type(dic))
#to get the keys for the dictionary
print(dic.keys())
#to get the values for the dictionary
print(dic.values())