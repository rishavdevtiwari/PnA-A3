# 16. Accept a number from the user:
#  If the number is greater than 100, print "Big Number".
#  If the number is between 50 and 100, print "Medium Number".
#  If less than 50, print "Small Number".
num=int(input("Enter a number : "))
if num>100:
    print("Big Number")
elif 50<=num<=100:
    print("Medium Number")
else:
    print("Small Number")
    