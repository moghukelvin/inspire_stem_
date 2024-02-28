laptop ={"make":"lenovo","colour":"grey","weight":"1.2","year":"2023"}


print(laptop["make"])
print(laptop["colour"])
print(laptop["year"])

laptop["colour"] = "red"
laptop["year"] = "2009"

print(laptop)

laptop["size"] ="1200mm * 600mm"

del laptop["colour"]

print(laptop)

siz_laptop = laptop.copy()
print(siz_laptop)

"""
"""
for key,value in laptop.items():
    print(key)
    print("\n")
    print(value)