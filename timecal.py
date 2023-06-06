from time import *
import random as r

#For Finding Error Between The Paragraph And UserInput 

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error

#For Checking Speed

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_r = round(time_delay,2)
    speed = len(userinput)/time_r
    return round(speed)

test = ["a quick dogs jump on the lazy fox",
        "my name is henil kheni"]
test1 = r.choice(test)
print("\t\tTyping Speed")
print(test1)
time1 = time()
testinput = input("Enter Here : ")
time2 = time()
print('Spedd : ', speed_time(time1, time2, testinput)," w/sec")
print("Error : ", mistake(test1,testinput))
