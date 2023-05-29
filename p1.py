# Quiz game
'''
print("welcome to the Henil's Quiz games!!")

playing = input("Do you want to play ? ")
print(playing)

if playing != "yes":
    quit()

print("Okay!! Let's play....")
count = 0

print("What does CPU stands for ? ")
answer = "cpu"
a1 = input()
if a1 == answer:
    print("Correct!!")
    count += 1
else:
    print("Incorrect!!")

print("What does Gpu stands for ? ")
answer = "Gpu"
a1 = input()
if a1 == answer:
    print("Correct!!")
    count += 1
else:
    print("Incorrect!!")

print("What does RAM stands for ? ")
answer = "ram"
a1 = input()
if a1 == answer:
    print("Correct!!")
    count += 1
else:
    print("Incorrect!!")

print("What does Psu stands for ? ")
answer = "psu"
a1 = input()
if a1 == answer:
    print("Correct!!")
    count += 1
else:
    print("Incorrect!!")

print("Your total correct answer is "+str(count))
print("And you got " + str((count/4)*100) + "percentage")

'''
#rock paper scissor
'''
import random
userwins = 0
computerwins = 0


option = ["rock","paper","scissors"]

while True:

    userInput = input("chose rock / paper / scessior or q for quit : ")
    print("you choose : ",userInput)

    if userInput == "q":
        break

    if userInput not in option:
        continue
    
    randomnumber = random.randint(0,2)

    computerInput = option[randomnumber]
    print("computer choose : ",computerInput)

    if userInput == "rock" and computerInput == "scissors":
        print("you won!!")
        userwins +=1
    
    elif userInput == "paper" and computerInput == "rock":
        print("you won!!")
        userwins +=1

    elif userInput == "scissors" and computerInput == "paper":
        print("You won!!")
        userwins +=1
    
    else:
        print("you lost it!!")
        computerwins += 1

print("you are out of the game")
print("total user wins ",userwins)
print("total computer wins ", computerwins)
'''
