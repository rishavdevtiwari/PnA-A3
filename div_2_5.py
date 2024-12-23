# 4. Take a number as input. Check if it is divisible by 2. If yes, further check if it is
# divisible by 5. Print appropriate messages for each condition.
num=int(input("Enter a number : "))
if num%2==0:
    if num%5==0:
        print("The number is divisible by both 2 and 5")    
    else:
        print("The number is divisible by 2, but not 5")
elif num%5==0:
    print("The number is divisible by 5, but not 2")
else:
    print("The number is not divisible by 2 or 5")