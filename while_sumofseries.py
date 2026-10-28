n=int(input("Read the Number: "))
sum=0
i=0
if(n > 0):
    while i <= n:
        sum+=i
        i+=1
    print(f"{"Sum of series of n: "}{sum}")
else:        
    print("Invalid Number")
