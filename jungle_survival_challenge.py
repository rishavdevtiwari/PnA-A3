# 8. Write a program starting with "Welcome to the Jungle Survival Challenge".
#  Ask the user to "search for food" or "build a shelter".
#  If "search for food", ask to choose between "hunt" or "gather".
#  If "hunt", print "You were attacked by a wild animal. Game Over."
#  If "gather", print "You found enough food. You Win!"
#  If "build a shelter", print "Your shelter collapsed in the rain. Game Over."
print("Welcome to the Jungle Survival Challenge")
choice=input("Do you want to 'search for food' or 'build a shelter' : ").lower()
if choice=="search for food":
    choice=input("Do you want to 'hunt' or 'gather' : ").lower()
    if choice=="hunt":
        print("You were attacked by a wild animal. Game Over.")
    elif choice=="gather":
        print("You found enough food. You Win!")
    else:
        print("Invalid choice. Game Over.")
elif choice=="build a shelter":
    print("Your shelter collapsed in the rain. Game Over.")
else:
    print("Invalid choice. Game Over.")
        