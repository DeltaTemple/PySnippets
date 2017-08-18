days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

x = int(input("Enter a day number"))

#I subtract in this tuple to make up for element zero
print("That day is", days[x-1])