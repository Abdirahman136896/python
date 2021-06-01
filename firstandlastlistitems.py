#Python program to display the first and last items from a list
listItems = input("Enter values for the list separated by commas: ")
thisList = listItems.split(",")
print("This is the complete list ", thisList)
print("The first item in the list is: ", thisList[0])
print("The last item in the list is: ", thisList[-1])