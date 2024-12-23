# 25. Accept the age, gender ('M', 'F'), and show type ('Matinee', 'Evening'):
#  Age < 12:
# o Male or Female:
#  Matinee: Ticket = Rs500
#  Evening: Ticket = Rs700
#  Age >= 12 and < 60:
# o Male:
#  Matinee: Ticket = Rs800
#  Evening: Ticket = Rs100
# o Female:
#  Matinee: Ticket = Rs700
#  Evening: Ticket = Rs900
#  Age >= 60:
# o Male or Female: Ticket = Rs600
age=int(input("Enter your age : "))
gender=input("Enter your gender (M/F) : ").lower()
show_type=input("Enter show type (Matinee/Evening) : ").lower()
if age<12:
    if gender=='m' or gender=='f':
        if show_type=='matinee':
            print("Ticket price is Rs500")
        elif show_type=='evening':
            print("Ticket price is Rs700")
        else:
            pass
elif age>=12 and age<60:
    if gender=='m':
        if show_type=='matinee':
            print("Ticket price is Rs800")
        elif show_type=='evening':
            print("Ticket price is Rs100")
        else:
            pass
    if gender=='f':
        if show_type=='matinee':
            print("Ticket price is Rs700")
        elif show_type=='evening':
            print("Ticket price is Rs900")
        else:
            pass
else:
    if gender=='m' or gender=='f':  
        if show_type=='matinee' or show_type=='evening':
            print("Ticket price is Rs600")
        