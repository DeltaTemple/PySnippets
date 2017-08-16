code = ""
x = 1

while code != "exit":
    code = input("Enter code: ")
    exec(code)
    x += 1