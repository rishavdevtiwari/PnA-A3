# 10. Start with "Welcome to the Haunted Castle".
#  Ask the user to choose "enter the castle" or "run away".
#  If "enter the castle", ask them to choose a door: "red", "green", or "black".
# o If "red", print "You entered a room full of flames. Game Over."
# o If "green", print "You found the treasure. You Win!"
# o If "black", print "You were captured by ghosts. Game Over."
#  If "run away", print "You escaped safely."
print("Welcome to the Haunted Castle!")
choice = input("Do you want to 'enter the castle' or 'run away' ? : ").lower()
if choice == "enter the castle":
    choice = input("Which door do you want to choose? 'red', 'green', 'black' : ").lower()
    if choice == "red":
        print("You entered a room full of flames. Game Over.")
    elif choice == "green":
        print("You found the treasure. You Win!")
    elif choice == "black":
        print("You were captured by ghosts. Game Over.")
    else:
        print("Invalid choice. Game Over.")
elif choice =="run away":
    print("You escaped safely.")
else:
    print("Invalid choice. Game Over.")