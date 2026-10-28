n=int(input("Read the number: "))
sum=0
if n > 0:
    for i in range(0,n+1):
        sum += i
    print(f"{"Sum of series of n :"}{sum}")
else:
    print("Invalid Number")
