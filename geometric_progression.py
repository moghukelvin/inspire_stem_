# this is a programme to generate the terms and sum in geometric progression
#date : 20/2/2024
#name : moghul

a = int(input("enter the first term"))
r = int(input("enter the common ration"))
n = int(input("enter the number of the terms"))

sum = 0
term = a

for i in range(n):
    print(term, end_"")
    sum + = term
term * = r
print("\n the sum of the geometric progression is",sum)
