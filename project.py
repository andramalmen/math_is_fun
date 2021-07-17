from gameClasses import Game, MathGame, BinaryGame
import gametasks as gt

try:
    mathInstructions = "In this game, you will be given a simple arithmetic question.\nEach correct answer gives you one mark.\nNo mark is deducted for wrong answers."
    binaryInstructions = "In this game, you will be given a number in base 10.\nYour task is to convert this number to base 2.\nEach correct answer gives you one mark.\nNo mark is deducted for wrong answers."

    bg = BinaryGame()
    mg = MathGame()

    userName = input("What is your user name? ")
    score = int(gt.getUserScore(userName))

    if score == -1:
        newUser = True
        score = 0
    else:
        newUser = False

    print(f'Welcome {userName}. Your score is {score}.')

    userChoice = 0

    while userChoice != "-1":
        game = input("\nSelect a game: Math Game (1) or Binary Game (2) ")
        while game != "1" and game != "2":
            print("\nPlease try again: ")
            game = input("\nSelect a game: Math Game (1) or Binary Game (2) ")

        numPrompt = input(
            "\nHow many questions do you want per game(1 to 10)? ")

        while True:
            try:
                num = int(numPrompt)
                break
            except:
                print("\nYou did not enter a valid number. Please try again. ")
                numPrompt = input(
                    "\nHow many questions do you want per game(1 to 10)? ")

        if game == "1":
            mg.noOfQuestions = num
            gt.printInstructions(mathInstructions)
            score = score + mg.generateQuestions()
        else:
            bg.noOfQuestions = num
            gt.printInstructions(binaryInstructions)
            score = score + bg.generateQuestions()

        print("\nYour current score is: %d." % (score))
        userChoice = input("\nPress enter to continue or -1 to end the game. ")

    gt.updateUserScore(newUser, userName, str(score))


except Exception as e:
    print("An unknown error has occurred")
    print("Error", e)
