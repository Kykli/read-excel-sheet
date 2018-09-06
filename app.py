import os
import sys
import FILENAME

#os.chdir("PATH")

# Colors only for Linux
class bcolors:
    red = "\033[0;31m"
    end = "\033[0m"

replaceList = ["{", "}"]

try:
    while True:
        print("******************")
        print("* Chosoe 1 or 2: *")
        print("******************")
        print("1. City")
        print("2. Street address")
        number = input("")

        if number == "1":
            restart = True
            while restart:
                try:
                    city = input("Provide city: ").title()
                    pickedCity = str(FILENAME.allData[city])
                    print("\n" + re.sub("|".join(replaceList)," ", pickedCity.replace(",", "\n")) + "\n")    
                    input("Press Enter to continue...\n")
                    break
                except KeyError:
                    print(bcolors.red + "City not found!" + bcolors.end)
                    back = input("Press Enter to continue or 'b' to start over...\n")
                    
                    if back == "b":
                        restart = False
                        break
        
        elif number == "2":
            restart = True
            while restart:
                try:
                    streetAddress = input("Provide street address: ").title()
                    pickedStreetAddress = str(FILENAME.allData[streetAddress])
                    print("\n" + re.sub("|".join(replaceList)," ", pickedStreetAddress.replace(",", "\n")) + "\n")
                    input("Press Enter to continue...\n")
                    break
                except KeyError:
                    print(bcolors.red + "Street address not found!" + bcolors.end)
                    back = input("Press Enter to continue or 'b' to start over...\n")
                    
                    if back == "b":
                        restart = False
                        break
        else:
            print(bcolors.red + "Please choose 1 or 2." + bcolors.end)
            input("Press Enter to continue...")

except EOFError:
    print("Force shutdown...")
except KeyboardInterrupt:
    print("Force shutdown...")