# 2. Ask the user if they want vegetarian or non-vegetarian. Based on the choice, give
# them options. If vegetarian, ask if they want "Salad" or "Pasta". If non-vegetarian, ask
# if they want "Chicken" or "Fish".
choice=input("Do you want vegetarian or non-vegetarian (veg/nonveg) : ").lower()
if choice=='veg':
    choice=input("Do you want 'salad' or 'pasta' : ").lower()
    if choice=='salad':
        print("You will be served with our salad!")
    elif choice=='pasta':
        print("You will be served with our pasta!")
    else:
        print("Invalid option!")
elif choice=='nonveg':
    choice=input("Do you want 'chicken' or 'fish' : ").lower()
    if choice=='chicken':
        print("You will be served with our chicken!")
    elif choice=='fish':
        print("You will be served with our fish!")
    else:
        print("Invalid option!")
else:
    print("Invalid option!")