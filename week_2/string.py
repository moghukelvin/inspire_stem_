# strings in python
# Date 22/2/2024
# Name : kelvin moghul

city = "nairobi"

# convert to uppercase

print(city)
print("\n") # prints a new line
print(city.upper())

name ="KELVIN MOGHUL"
print(name)
print(name.lower()) # converts string to lower case

town = "    Naivasha    "

print(town)
print("\t") # new tab
print(town.strip())

# add two strings

f_name = "eve"
s_name = "katani"

full_name = f_name + s_name

print(full_name)


city = "nairobi"
print(city[-7])# n
print(city[-6])
print(city[-5])
print(city[-4])
print(city[-3])
print(city[-2])
print(city[-1])# i

#replacing a character

fruit ="orangeoooooooo"

print(fruit.replace("o","y"))

subject = "physical,sciences"

print(subject.split(":"))

#printing an integer
age = 22
height = 2.1

print("i am {0} years old and {1} meters tall ".format(age,height))

#printing a string
activity = "dancing"
print("my hobby is %s"%(activity))


name = "kelvin moghul"
print(len(name))

#printing a float
height = 1.23
print("my height is %5.4f"%(height))

name = "kelvin moghul"
print(len(name))

print(f"my full name is {name}")


school ="electrical"
course ="engineering"

print("i am studying{course}in the school of{school}"format(course = "medicine",school="human sciences"))

