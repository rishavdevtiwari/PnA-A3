# 20. Accept two numbers from the user:
#  If both numbers are even, print their sum.
#  If one is even and the other is odd, print their difference.
#  Otherwise, print their product.
a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
if a%2==0 and b%2==0:
    print("Sum of the numbers is : ",a+b)
elif (a%2==0 and b%2!=0) or (a%2!=0 and b%2==0):
    print("Difference of the numbers is",a-b)
else:
    print("The product of the numbers is", a*b)