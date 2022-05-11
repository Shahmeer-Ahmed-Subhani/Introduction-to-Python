
employee_file = open("employees.txt", "r")
print(employee_file.read)

#reading first line
print(employee_file.readline())
#reading second line
print(employee_file.readline())
#reading third line
print(employee_file.readline())

#checking if the file is readable. Answer is in boolean
print(employee_file.readable)

# Make sure to close the file aswell
employee_file.close()

# THESE WILL NOT WORK BECAUSE I DID NOT PUT "CLOSE" AFTER THEM. JUST EXAMPLES