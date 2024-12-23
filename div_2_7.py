# 15. Accept input from the user:
#  If the number is divisible by 2 and 7, print "Double Seven".
#  If divisible by 2 but not 7, print "Even".
#  If divisible by 7 but not 2, print "Lucky Seven".
#  Otherwise, print the number as is.
num=int(input("Enter a number : "))
if num%2==0 and num%7==0:
    print("Double Seven")
elif num%2==0 and num%7!=0:
    print("Even")
elif num%7==0 and num%2!=0:
    print("Lucky Seven")
else:
    print(f"{num}")
    