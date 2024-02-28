# program to find salary of an employee
# date : 26/2/2024
# name : kelvin moghul

salary = int(input("enter current salary"))
if salary < 100000:
    salary = 1.3 * salary
    print("new salary is :" ,salary)
elif salary > 100000 and salary < 150000 :
    salary = 1.5 * salary
    print("new salary is :" ,salary)
elif salary > 150000 :
    salary = 1.05 * salary
    print("new salary is :" ,salary)    