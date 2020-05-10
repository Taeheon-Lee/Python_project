import random

goal = random.randint(1, 99)
cnt = 1
print("This is an interaction huessing game!")
print("You have to enter a number between 1 and 99", end=" ")
print("to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!\n")

while 1:
    answer = input("What's your guess between 1 and 99?\n")
    if answer == "exit":
        print("Goodbye!")
        exit()
    elif not answer.isdecimal():
        print("That's not a number.\n")
    elif int(answer) < goal:
        print("Too low!\n")
    elif int(answer) > goal:
        print("Too high!\n")
    elif int(answer) == goal:
        if cnt == 1:
            print("The answer to the ultimater question of life,", end=" ")
            print(f"the univers and everthing is {answer}.")
            print("Congratulations! You got it on your first try!")
        else:
            print("Congratulations, you've got it!")
            print("you won in", cnt, "attempts!")
        exit()
    cnt = cnt + 1
