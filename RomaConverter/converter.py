import sys
import time

######################################################
# Just for fun #######################################
######################################################

def printProgressBar():
    # Prints the Progress Bar
    print("Progress [ ", end="", flush=True)
    print(" ] - [Converting]", end="", flush=True)

def addProgress(num, progress):
    # Adds and prints a new percentage to the Progress Bar
    sys.stdout.write("\033[2K\033[1G")

    progress += int(num)

    print("Progress [ ", end="", flush=True)

    for x in range(0, int(progress)):
        print("█", end="", flush=True)
        time.sleep(0.00125)
    print(" ] - [Converting]", end="", flush=True)

def setFinished(progress):
    # Sets the Progress Bar to finished and deletes it
    sys.stdout.write("\033[2K\033[1G")

    print("Progress [ ", end="", flush=True)
    print("100%", end="", flush=True)
    print(" ] - [Done]", end="", flush=True)

    progress == 0

    sys.stdout.write("\033[2K\033[1G")

######################################################
# Essential Components ###############################
######################################################

def askForReusage():
    # Sends the question if the user wants to reuse the converter
    answer = str(input("Do you want to convert another number? (Y/N) "))

    if answer == "Y":
        # Asks for the number to convert
        i = int(input("Your number (1-3999): "))
        # Calls run converter method
        runConverter(i)
    elif answer == "N":
        # Quits the application
        exit()
    else:
        # Asks again because the input was not valid
        askForReusage()

def runConverter(num):
    # Defines progress variable
    # @Annotation: Essential for Progress Bar
    progress = 1

    # Defines main number variable
    # @Annotation: Essential for Converting Process
    i = int(num)
    
    # Checks for invalid numbers
    # @Annotation: Essential for Converting Process
    if i > 3999:
        print("Numbers in range 1-3999")
        exit()

    # Defines what to run through
    # @Annotation: Essential for Converting Process
    values = [1000, 100, 10]
    letters = ["M", "C", "X"]

    # Defines what letters to append
    # @Annotation: Essential for Converting Process
    counter = 0

    # Defines result variable
    # @Annotation: Essential for Converting Process
    result = ""

    # Prints the Progress Bar
    # @Annotation: Essential for Progress Bar
    printProgressBar()

    # Runs through the pre defined values
    # @Annotation: Essential for Converting Process
    for v in values:
        # Defines ammount of letters to be appended
        # @Annotation: Essential for Converting Process
        worker = int(i / v)
        i -= worker * v

        # Defines process output variable
        # @Annotation: Essential for Converting Process
        output = ""

        # Handles the letter 'M' (1000)
        # @Annotation: Essential for Converting Process
        if v == 1000:
            for t in range(0, worker):
                output += str(letters[counter])
 
            addProgress(25, progress)
            progress += 25
        
        # Handles the letter 'C & D' (100, 500)
        # @Annotation: Essential for Converting Process
        elif v == 100:
            if worker == 9:
                output += str(letters[counter])
                output += str(letters[counter-1])

            elif worker == 5:
                output += "D"

            elif worker == 4:
                output += str(letters[counter])
                output += "D"

            else:
                if int(worker / 5) == 1:
                    output += "D"
                    worker -= 5

                for t in range(0, worker):
                    output+= str(letters[counter])

            addProgress(25, progress)
            progress += 25

        # Handles the letter 'X & L' (10, 50)
        # @Annotation: Essential for Converting Process
        else:
            if worker == 9:
                output += str(letters[counter])
                output += str(letters[counter-1])

            elif worker == 5:
                output += "L"

            elif worker == 4:
                output += str(letters[counter])
                output += "L"

            else:
                if int(worker / 5) == 1:
                    output += "L"
                    worker -= 5

                for t in range(0, worker):
                    output+= str(letters[counter])
            
            addProgress(25, progress)
            progress += 25

        result += output

        counter += 1

    # Handles the letter 'I, V & X' (1, 5, 10)
    # @Annotation: Essential for Converting Process
    if i != 0:
        if i == 9:
            result += str("I")
            result += str("X")
            addProgress(25, progress)
            progress += 25

        elif i == 5:
            result += "V"
            addProgress(25, progress)
            progress += 25

        elif i == 4:
            result += "I"
            result += "V"
            addProgress(25, progress)
            progress += 25

        else:
            if int(i / 5) == 1:
                result += "V"
                i -= 5
                addProgress(20, progress)
                progress += 20

            for t in range(0, i):
                result+= str("I")
            addProgress(5, progress)
            progress += 5

    # Handles the result
    # @Annotation: Essential for Converting Process
    setFinished(progress)
    progress = 0
    print("\n")
    print("[C] Your number '", str(num), "' got converted to ", result)
    print("\n")

######################################################
# Main ###############################################
######################################################

print("\n")
i = int(input("Your number (1-3999): "))
runConverter(i)
askForReusage()