#create tuple
coordinates = (4,5)
#prints all the values in the tuple
print(coordinates)
#prints values of the tuple at a specific index
print(coordinates[0])
print(coordinates[1])
#coordinates[1] = 6 returns an error tuple object not supporting assignment because tuples are immutable
list_coordinates = [(4,5),(6,7),(8,9)]
print(list_coordinates)
list_coordinates.insert(0,(0,1))
print(list_coordinates)
