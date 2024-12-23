# 11. Begin with "Welcome to the Underwater World".
#  Ask the user to choose "dive deeper" or "surface".
#  If "dive deeper", ask them to "search for pearls" or "chase the fish".
# o If "search for pearls", print "You found a rare pearl. You Win!"
# o If "chase the fish", print "You got lost underwater. Game Over."
#  If "surface", print "You returned safely."
print("Welcome to the Underwater World!")
choice=input("Do you want to 'dive deeper' or 'surface' : ").lower()
if choice=='dive deeper':
    choice=input("Do you want to 'search for pearls' or 'chase the fish' : ").lower()
    if choice=='search for pearls':
        print("You found a rare pearl. You Win!")
    elif choice=='chase the fish':
        print("You got lost underwater. Game Over.")
    else:
        print("Invalid choice. Game Over.")
elif choice=='surface':
    print("You returned safely.")
else:
    print("Invalid choice. Game Over.")
        