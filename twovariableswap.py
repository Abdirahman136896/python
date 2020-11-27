a = 5
b = 6

#first technique(using a third(temporary) variable

#create  a temporary variable and store the value of a in temp
temp = a
#store the value of b in a
a = b
#copy the value stored in temp to b
b = temp

print("a->"+str(a) + " b->"+str(b))

a = 5
b = 6

#second technique

a = a + b #a = 11
b = a - b #b = 5
a = a - b #a = 11 - 5 = 6

print("a->"+str(a) + " b->"+str(b))

#third technique
#using the xor operator

a,b = 5,6
a = a ^ b #a = 11
b = a ^ b #b = 5
a = a ^ b #a = 11 - 5 = 6

print("a->"+str(a) + " b->"+str(b))

#fourth technique
#rotation two concept in python

a,b = 5,6
a,b = b,a

print("a->"+str(a) + " b->"+str(b))


