import os, random

print("Password generator tool: How long would you like your password to be?")
print("Recommendations:")
print("1. 12 chars - offsite utility")
print("2. 32 chars - General online account")
print("3. 64 chars - AES (maximum)")
print("4. 256 chars - disk/volume encryption")
print("5. Other (Custom integer)")

option = raw_input("Enter option, 1-5: ")

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' + '!@#$%^&*()'
random.seed = (os.urandom(256))




if (option == '1' or option == '12'):
        length = 12
        print ''.join(random.choice(chars) for i in range (length))

elif(option == '2' or option == '32'):
    length = 32
    print ''.join(random.choice(chars) for i in range(length))

elif (option == '3' or option == '64'):
    length = 64
    print ''.join(random.choice(chars) for i in range(length))

elif (option == '4' or option == '256'):
    length = 256
    print ''.join(random.choice(chars) for i in range(length))

elif (option == '5'):
    length = int(input("Key length: "))
    print ''.join(random.choice(chars) for i in range(length))
else:
    print("Invalid option")
    exit()
