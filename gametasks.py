from os import rename, remove


def printInstructions(instruction):
    print(instruction)


def getUserScore(userName):
    try:
        file = open("userScores.txt", "r")
        for line in file:
            content = line.split(',')
            if content[0] == userName:
                file.close()
                return content[1]
        file.close()
        return "-1"
    except IOError:
        print("File not found.")
        file = open("userScores.txt", "w")
        file.close()
        return "-1"


def updateUserScore(newUser, userName, score):
    if newUser == True:
        file = open("userScores.txt", "a")
        file.write("\n" + userName + "," + str(score))
        file.close()
    else:
        file = open("userScores.tmp", "w")
        uFile = open("userScores.txt", "r")
        for line in uFile:
            content = line.split(',')
            if content[0] == userName:
                content[1] = score
                file.write(content[0] + "," + str(content[1]) + "\n")
            else:
                file.write(content[0] + "," + str(content[1]))
        file.close()
        uFile.close()
        remove("userScores.txt")
        rename("userScores.tmp", "userScores.txt")


print(updateUserScore(False, "Ann", 200))
