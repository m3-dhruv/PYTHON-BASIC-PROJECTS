import random

randNum = random.randint(1,100)

while True:
    userChoice = input("Guess the number or Quit:")
    if(userChoice == "Quit"):
        break

    userChoice = int(userChoice)
    if (userChoice == randNum):
        print("Success : Correct Guess!!!")
        break
    elif(userChoice < randNum):
        print("Your number was too small, try again...")
    else:
        print("Your number was too big, try again...")


print("----- GAME OVER -----")