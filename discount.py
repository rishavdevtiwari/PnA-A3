# 1. Take the price of an item as input. If the price is more than 1000, apply a 10%
# discount. Otherwise, check if the price is more than 500 and apply a 5% discount.
# Print the final price.

price=int(input("Enter the price of a specific item : "))
if price > 1000:
    price-=(price*(10/100))
    print(f"The price after discount is : {price}")
elif price> 500:
    price-=(price*(5/100))
    print(f"The price after discount is : {price}")
else:
    print(f"No discount is applicable for {price}")