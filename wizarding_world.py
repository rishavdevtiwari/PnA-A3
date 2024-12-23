# 13. Start the program with "Welcome to the Wizarding World".
#  Ask the user to choose a subject: "spells" or "potions".
#  If "spells", ask them to "practice magic" or "compete in duels".
#  If "practice magic", print "You mastered a powerful spell. You Win!"
#  If "compete in duels", print "You lost to a rival wizard. Game Over."
#  If "potions", ask whether to "brew an elixir" or "create poison".
#  If "brew an elixir", print "You healed a village. You Win!"
#  If "create poison", print "Your potion backfired. Game Over."
print("Welcome to the Wizarding World!")
choice = input("Choose a subject: 'spells' or 'potions': ").lower()
if choice == "spells":
    choice = input("Do you want to 'practice magic' or 'compete in duels' : ").lower()
    if choice == "practice magic":
        print("You mastered a powerful spell. You Win!")
    elif choice == "compete in duels":
        print("You lost to a rival wizard. Game Over.")
    else:
        print("Invalid choice. Game Over.")
elif choice == "potions":
    choice = input("Do you want to 'brew an elixir' or 'create poison' : ").lower()
    if choice == "brew an elixir":
        print("You healed a village. You Win!")
    elif choice == "create poison":
        print("Your potion backfired. Game Over.")
    else:
        print("Invalid choice. Game Over")
else:
    print("Invalid choice. Game Over")
    