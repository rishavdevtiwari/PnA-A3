# 18. Accept temperature in Celsius from the user:
#  If greater than 40, print "Hot".
#  If between 20 and 39, print "Warm".
#  If less than 20, print "Cold".
temp=int(input("Enter temperature in celsius : "))
if temp>40:
    print("Hot")
elif 20<=temp<=39:
    print("warm")
else:
    print("Cold")