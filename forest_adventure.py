# 7. Write a program that starts with a greeting: "Welcome to the Forest Adventure".
#  Prompt the user to choose a path: "left" or "right".
#  If "left", ask them to pick between "explore" or "rest".
#  If "explore", print "You found treasure!".
#  If "rest", print "You were attacked by wild animals. Game Over."
#  If "right", print "You fell into a trap. Game Over."
print("Welcome to the Forest Adventure")
choice = input("Do you want to go left or right? ").lower()
if choice == "left":
    choice=input("Do you want to 'explore' or 'rest' : ").lower()
    if choice == "explore":
        print("You found treasure!")
    elif choice == "rest":
        print("You were attacked by wild animals!. Game over")
    else:
        print("Invalid choice!")
elif choice=="right":
    print("You fell into a trap!. Game over")
else:
    print("Invalid choice!")