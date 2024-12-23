# 21. Accept the price of an item from the user:
#  If the price is greater than 1000, apply a 20% discount and print the new price.
#  If between 500 and 1000, apply a 10% discount.
#  If less than 500, no discount.
price=int(input("Enter the price of an item : "))
if price>1000:
    print(r"The price after 20% discount is ",price-(price*0.2))
elif price>=500 and price<=1000:
    print(r"The price after 10% discount is",price-(price*0.1))
else:
    print("No discount")
    