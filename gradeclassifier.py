grade=float(input("Read the grade: "))

if grade < 0 or grade > 20:
    print("Invalid Grade")
elif grade >= 16:
    print("Very Good")
elif grade >= 14:
    print("Good")
elif grade >= 12:
    print("Fairely Good")
elif grade >= 10:
    print("Pass")
else:
    print("Fail")
        

