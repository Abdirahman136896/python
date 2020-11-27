employee_file = open("employees.txt","r")
print(employee_file.readable())
#print(employee_file.read())
print(employee_file.readline())
for employee in employee_file.readlines():
    print(employee)
#print(employee_file.readlines()[1])
employee_file.close()