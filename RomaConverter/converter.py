import sys
import time

def askForReusage():
    answer = str(input("Do you want to convert another number? (Y/N) "))
    if answer == "Y":
        i = int(input("Your number (1-3999): "))
        runConverter(i)
    elif answer == "N":
        exit()
    else:
        askForReusage()

def printProgressBar():
    print("Progress [ ", end="", flush=True)
    print(" ] - [Converting]", end="", flush=True)

def addProgress(num, progress):
    sys.stdout.write("\033[2K\033[1G")

    progress += int(num)

    print("Progress [ ", end="", flush=True)

    for x in range(0, int(progress)):
        print("█", end="", flush=True)
        time.sleep(0.00125)
    print(" ] - [Converting]", end="", flush=True)

def setFinished(progress):
    sys.stdout.write("\033[2K\033[1G")

    print("Progress [ ", end="", flush=True)
    print("100%", end="", flush=True)
    print(" ] - [Done]", end="", flush=True)

    progress == 0

    sys.stdout.write("\033[2K\033[1G")

def runConverter(num):
    progress = 1

    i = int(num)
    
    if i > 3999:
        print("Numbers in range 1-3999")
        exit()

    values = [1000, 100, 10]
    letters = ["M", "C", "X"]

    counter = 0

    result = ""

    printProgressBar()

    for v in values:

        worker = int(i / v)
        i -= worker * v
        output = ""

        if v == 1000:
            for t in range(0, worker):
                output += str(letters[counter])
 
            addProgress(25, progress)
            progress += 25
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

    setFinished(progress)
    progress = 0
    print("\n")
    print("[C] Your number '", str(num), "' got converted to ", result)
    print("\n")

print("\n")
i = int(input("Your number (1-3999): "))
runConverter(i)
askForReusage()