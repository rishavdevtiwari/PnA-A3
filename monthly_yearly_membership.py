# 26. Accept the age, gender ('M', 'F'), and membership type ('Monthly', 'Yearly'):
#  Age >= 18 and < 30:
# o Male:
#  Monthly: Rs50
#  Yearly: Rs500
# o Female:
#  Monthly: Rs45
#  Yearly: Rs450
#  Age >= 30 and <= 50:
# o Male or Female:
#  Monthly: Rs60
#  Yearly: Rs600
#  Age > 50:
# o Male or Female:
#  Monthly: Rs40
#  Yearly: Rs400
age=int(input("Enter your age : "))
gender=input("Enter your gender (M/F) : ").lower()
membership=input("Enter your membership type (Monthly/Yearly) : ").lower()
if age>=18 and age<30:
    if gender=='m':
        if membership=='monthly':
            print("Membership fee is Rs50")
        elif membership=='yearly':
            print("Membership fee is Rs500")
        else:
            pass
    elif gender=='f':
         if membership=='monthly':
             print("Membership fee is Rs45")
         elif membership=='yearly':
             print("Membership fee is Rs450")
elif age>=30 and age<=50:
    if gender=='m' or gender=='f':
        if membership=='monthly':
            print("Membership fee is Rs60")
        elif membership=='yearly':
            print("Membership fee is Rs600")
elif age>50:
    if gender=='m' or gender=='f':
        if membership=='monthly':
            print("Membership fee is Rs40")
        elif membership=='yearly':
            print("Membership fee is Rs400")
else:
    print("Membership is not available for you")
            