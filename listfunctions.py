lucky_numbers = [42,16,15,8,23,4]
friends = ["Hoyo","Zaks","Ahmedo","Abdinasir","Mustafa","Abdallah","Space",1342,True]
print(friends)
friends.extend(lucky_numbers)
print(friends)
friends.append("Creed")
print(friends)
friends.insert(1,"Hamza")
print(friends)
friends.remove("Creed")
print(friends)
friends2 = friends.copy()
print(friends2)
print(friends.append("Zaks"))
print(friends.count("Zaks"))
friends = ["Hoyo","Zaks","Ahmedo","Abdinasir","Mustafa","Abdallah","Space"]
friends.sort()
print(friends)
friends.clear()
print(friends)
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
