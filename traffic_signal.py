# 17. Accept a color from the user:
#  If the color is "Red", print "Stop".
#  If "Yellow", print "Slow Down".
#  If "Green", print "Go".
#  Otherwise, print "Invalid Signal".
choice=input("Enter a color (red/yellow/green) : ").lower()
if choice=="red":
    print("Stop")
elif choice=="yellow":
    print("Slow Down")
elif choice =="green":
    print("Go")
else:
    print("Invalid signal!")