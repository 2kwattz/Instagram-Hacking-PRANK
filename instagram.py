import pyfiglet
import keyboard
import time



banner = pyfiglet.figlet_format("Insta Cracker")
print(banner)
email = input("Enter the username of the associated account")
emailchar = len(email)
if emailchar>0:
    print("Searching for the user")
    time.sleep(3)
    print("User found\nDo you want to use proxy [y/n] ?")
    prox = input()
    if prox == 'y':
        print("Connected to 57.45.345.89 , Starting the attack...")
        time.sleep(4)
        print("15 % completed\n")
        time.sleep(2)
        print("30 % completed\n")
        time.sleep(2)
        print("55 % completed")
        time.sleep(2)
        print("70 % completed")
        time.sleep(3)
        print("Account cracked successfully ! Press enter to view the password\n")
        keyboard.wait("enter")
        print("\nHey Listen ! \nWe have got the password of the victim account")
        print("But we cannot share it with you .Hacking anyone's account \nwithout their prior consence is an illegal activity .Be a responsible citizen")
        print("press ESC to exit the program\n")
        keyboard.wait("ESC")

else:
    print("Enter proper username :D :D \n")
