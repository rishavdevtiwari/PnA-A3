# 24. Accept the age, gender ('M', 'F'), and experience (years) and assign a role:
#  Age >= 21 and <= 35:
# o Male:
#  Experience >= 5: "Senior Developer"
#  Experience < 5: "Junior Developer"
# o Female:
#  Experience >= 5: "Senior Analyst"
#  Experience < 5: "Junior Analyst"
#  Age > 35:
# o Male or Female: "Manager Role"
age=int(input("Enter your age : "))
gender=input("Enter your gender (M/F) : ").lower()
experience=int(input("Enter your experience in years : "))
if 21<=age<=35:
    if gender=='m':
        if experience>=5:
            print("Your role is Senior Developer")
        else:
            print("Your role is Junior Developer")
    elif gender=='f':
        if experience>=5:
            print("Your role is Senior Analyst")
        else:
            print("Your role is Junior Analyst")
elif age>35:
    if gender=='m' or gender=='f':
        print("Your role is Manager Role")
else:
    print("Invalid age")
            
