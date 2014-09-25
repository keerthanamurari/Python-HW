import os, random

guesses = 0
big = 100
small = 1

##number = random.randint(1, 100)

print('Hi ! What is your name ?')
myName = input()

print("Hello " + myName + "! Lets play a game!")
print("Think of random number from 1 to 100, and I'll try to guess it!")

while True:
    guess = int((big + small) / 2)
    print("Is your number ",guess," ?(yes/no):")

    YesNo = input()
    
    if(YesNo == "yes"):
        print("\n\nYeey! I got it in",guesses, " tries!")
        print("Do you want to play more..??")
        YesNo = input()
        
        if(YesNo == "no"):
            print("Bye-Bye")
            break
        elif(YesNo == "yes"):
            guesses = 0
            big = 100
            small = 1
    
    elif(YesNo == "no"):
        guesses += 1
        
        print("Is your number larger than" ,guess)
        YesNo = input()

        if(YesNo == "no"):
            big = guess - 1

        elif (YesNo == "yes"):
            small = guess + 1
