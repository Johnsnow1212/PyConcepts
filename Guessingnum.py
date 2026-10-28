import random
Secret=random.randint(1,100)
attempts=0
while attempts < 7:
    Guess=int(input("Read the Gussing Number: "))
    attempts+=1
    if Guess == Secret:
        print("Congrats! You got it...")
        break
    elif Guess < Secret:
        print("Your Guess is too low...")
    else:
        print("Your Guess is too high...")
if Guess != Secret:
    print("Your Guess's are Wrong,you miss it")
    