import os
import sys
import FILENAME

#os.chdir("PATH")
class bcolors:
    red = "\033[0;31m"
    end = "\033[0m"

try:
    
    while True:
        print("******************")
        print("* Chosoe 1 or 2: *")
        print("******************")
        print("1. City")
        print("2. Street address")
        number = input("")

        if number == "1":
            try:
                city = input("Provide city: ")
                print(str(vero2018.allData[city]))
                input("Press Enter to continue...")
            except KeyError:
                print(bcolors.red + "City not found!" + bcolors.end)
                input("Press Enter to continue...")
        
        elif number == "2":
            try:
                streetAddress = input("Provide street address: ")
                print(str(vero2018.allData[streetAddress]))
                input("Press Enter to continue...")
            except KeyError:
                print(bcolors.red + "Street address not found!" + bcolors.end)
                input("Press Enter to continue...")
        else:
            print(bcolors.red + "Please choose 1 or 2." + bcolors.end)
            input("Press Enter to continue...")

except EOFError:
    print("Force shutdown...")
except KeyboardInterrupt:
    print("Force shutdown...")