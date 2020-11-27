#create a set
s = {22,25,14,21,5}
#printing the set.Set never follows the order in which the elements are added to the set.Notice that the set is not in its original order but is in ascending order
print(s)
#when printing for the second time the result is different because the set uses a concept of hash to improve performance by fetching the element as fast as possible
t = {25,14,98,63,75,98}
print(t)
#in a set index is not supported so t[1] returns error set object does not support indexing

#adds an element to the set
s.add(45)
#removes the last element from the list
s.pop()
#removes the specified element from the list
s.remove(14)
print(s)
#combines both elements in the sets specified(s and t)
print(s.union(t))
#prints the element which is in both sets
print(s.intersection(t))
#sets do not support duplicate values
v = {27,28,29,30,31,32,28}
print(v)