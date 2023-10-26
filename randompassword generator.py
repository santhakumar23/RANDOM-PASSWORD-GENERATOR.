import random
print("werlcome to the password generator!")
randomchars="abcdefghijklmnopqrstuvwxuyzABCDEFGHIJKLNMOPQRSTUVWXYZ1234567890*/-*&^$"
numberofpassword=int(input("Enter the number of password to be generator : "))
passwordlength=int(input("plese entert the length of the password needed:"))
print("Here are your passwords:")
for i in range(numberofpassword):
    password=""
    for x in range(passwordlength):
        password=password+random.choice(randomchars)
    print(password)
