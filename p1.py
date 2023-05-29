#Email Validation.

email= input("Enter Your Email : ") #g@g.com , kheniheni4767@gmail.com
k,j,d=0,0,0
if len(email)>=6: #error 1
    if email[0].isalpha(): #error 2
        if ("@" in email) and (email.count("@")==1): #error 3
            if (email[-4]==".") ^ (email[-3]=="."): #error 4
                for i in email: 
                    if i==i.isspace(): #error 5.0
                        k=1
                    elif i.isalpha(): #error 5.1
                        if i==i.upper():
                            j=1
                    elif i.isdigit(): #error 5.2
                        continue
                    elif i=="_" or i=="." or i=="@": #errpr 5.3
                        continue
                    else:
                        d=1

                if k==1 or j==1 or d==1:
                    print("Space can not be allowed or first character must be lower check also _ . @ in the email (Error no: 5)")
                else:
                    print("Your Email Is Correct Formation")
            else:
                print("Your have to focus on . opertor (Error no: 4)")
        else:
            print("Your @ is more than 1 (Error no: 3)")
    else:
        print("Your First Letter Is Must Be In charcter (Error no: 2) ")
else:
    print(" Wrong Email :- Your email length is too short (Error no: 1) ")




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
