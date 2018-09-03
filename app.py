import os
import sys
import FILENAME

#os.chdir("PATH")

# Colors only for Linux
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
            while True:
                try:
                    city = input("Provide city: ").title()
                    print("\n" + str(FILENAME.allData[city]) + "\n")
                    input("Press Enter to continue...")
                    break
            except KeyError:
                print(bcolors.red + "City not found!" + bcolors.end)
                input("Press Enter to continue...")
        
        elif number == "2":
            while True:
                try:
                    streetAddress = input("Provide street address: ").title()
                    print("\n" + str(FILENAME.allData[streetAddress]) + "\n")
                    input("Press Enter to continue...")
                    break
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