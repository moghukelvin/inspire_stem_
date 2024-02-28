friends = ["jane","pauline","jill","james","peter"]
for friend in friends:
    print(friend)

enemies = friends[:]


for enemy in enemies:  # to copy one list in to another
    print(enemy)

friuts = ["guava","lemon","strawberry","orange","mango"]

# slice the list ie get part of the list
print(friuts[0:3])

del friuts[0]

print(friuts)

squares =[] # initilises an empty list

for x in range(0,11):
    squares.append(x**2)

print(squares)    