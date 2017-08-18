mylist = [100, 350, 720, 2500, 7800, 9000]


print("Single element:")
print(mylist[0])


print("Whole list:")
for x in mylist:
    print(x)

print("Last 3 elements:")
for x in mylist[-3:]:
    print(x)

print("Skips an element:")
for x in mylist[::2]:
    print(x)