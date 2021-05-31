#The following program adds the elements of a list and computes the sum and the average
print("Only enter -1 in the prompt field to indicate that the values being entered are complete\n")
myList = []
i = 0

while i >= 0:
        num = int(input("Enter element " + str(i) + ": "))
        if (num == -1):
            break
        myList.insert(i, abs(num))
        print(myList)
        i = i + 1
print("Sum of elements in given list is :", sum(myList))
if (len(myList) == 0):
    print("The average of the elements in the given list is: 0")
else:
    print("The average of the elements in the given list is: ", (sum(myList)/len(myList)))


