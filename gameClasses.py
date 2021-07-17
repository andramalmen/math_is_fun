from random import randint


class Game:
    def __init__(self, noOfQuestions=0):
        self._noOfQuestions = noOfQuestions
        print("Game class initialized")

    @property
    def noOfQuestions(self):
        return self._noOfQuestions

    @noOfQuestions.setter
    def noOfQuestions(self, value):
        if value < 1:
            self._noOfQuestions = 1
            print("Minimum Number of Questions = {}.".format(1))
            print("Hence, number of questions will be set to {}".format(1))
        elif value > 10:
            self._noOfQuestions = 10
            print("Maximum Number of Questions = {}.".format(10))
            print("Hence, number of questions will be set to {}".format(10))
        else:
            self._noOfQuestions = value


class BinaryGame(Game):
    def __init__(self):
        super().__init__()
        print("BinaryGame class initialized")

    def generateQuestions(self):
        score = 0
        for i in range(self.noOfQuestions):
            base10 = randint(1, 100)
            userResult = input(
                "Convert the number {} to binary: ".format(base10))

            while True:
                try:
                    answer = int(userResult, base=2)
                    if answer == base10:
                        print("The answer is correct")
                        score = score + 1
                        break
                    else:
                        print(
                            "Wrong answer. The correct answer is {:b}.".format(
                                base10))
                        break
                except:
                    print("You did not enter a binary number")
                    userResult = input(
                        "Convert the number {} to binary".format(base10))

        print("Score is: {}.".format(score))
        return score


# binaryGame = BinaryGame()
# binaryGame.noOfQuestions = 1
# binaryGame.generateQuestions()

class MathGame(Game):
    def __init__(self):
        super().__init__()
        print("MathGame class initialized")

    def generateQuestions(self):
        score = 0
        numberList = [0] * 5
        symbolList = [""] * 4
        operatorDict = {
            1: "+",
            2: "-",
            3: "*",
            4: "**"
        }
        for i in range(self.noOfQuestions):
            for index in range(0, len(numberList)):
                numberList[index] = randint(1, 9)
            for index in range(0, len(symbolList)):
                if index > 0 and symbolList[index-1] == "**":
                    symbolList[index] = operatorDict[randint(1, 3)]
                else:
                    symbolList[index] = operatorDict[randint(1, 4)]
            questionString = str(numberList[0])
            for index in range(0, len(symbolList)):
                questionString = questionString + \
                    symbolList[index] + str(numberList[index+1])
            result = eval(questionString)
            questionString = questionString.replace("**", "^")

            userResult = input(
                "What is the result of {}? ".format(questionString))

            while True:
                try:
                    answer = int(userResult)
                    if answer == result:
                        print("The answer is correct")
                        score = score + 1
                        break
                    else:
                        print(
                            "Wrong answer. The correct answer is {}.".format(
                                result))
                        break
                except:
                    print("You did not enter a  number")
                    userResult = input(
                        "What is the result of {}? ".format(questionString))
        print("Score is: {}.".format(score))
        return score


# mathGame = MathGame()
# mathGame.noOfQuestions = 1
# mathGame.generateQuestions()
