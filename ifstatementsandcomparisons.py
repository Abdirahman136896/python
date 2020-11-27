def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    if num2 >= num1 and num2 >= num3:
        return num2
    if num3 >= num1 and num3 >= num3:
        return num3
print(max_num(2,40,3))
print(max_num(20,4,3))
print(max_num(2,4,30))
