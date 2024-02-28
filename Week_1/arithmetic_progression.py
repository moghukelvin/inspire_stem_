#programme to determine the arithmetic progression of sequences
#date : 20/2/2024
#name : kelvin moghul

a = int(input("enter the firt term: "))
d = int(input("enter the common difference: "))
n =int(input("enter the number of terms: "))

sum = 0
term = a

for i in range(n):
    print(term, end="")
    sum += term
    term += d
    print("\n The sum of the arithmetic progression is", sum)