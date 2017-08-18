mylist = [20, 60, 500, 1200, 9000]

#Variable that starts from zero and counts up by one each loop iteration
for counter, x in enumerate(mylist):
    print("Counter is:", counter)
    print("x is:", x)
    mylist [counter] = x * 2

print(mylist)