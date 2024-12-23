# 5. Take a student's marks as input. If the marks are more than 50, check if they are
# greater than 90. If so, print "Excellent". If between 51 and 90, print "Good".
# Otherwise, print "Fail"
m=int(input("Enter your marks : "))
if m>50:
    if m>90:
        print("Excellent")
    elif m>51 and m<90:
        print("Good")
else:
    print("Fail")