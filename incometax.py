# 22. Accept age, gender ('M', 'F'), and income and calculate the tax:
#  Age >= 18 and < 60:
# o Male:
#  Income > 10,00,000: Tax = 30%
#  Income between 5,00,000 and 10,00,000: Tax = 20%
#  Income <= 5,00,000: Tax = 10%
# o Female:
#  Income > 10,00,000: Tax = 25%
#  Income between 5,00,000 and 10,00,000: Tax = 15%
#  Income <= 5,00,000: Tax = 5%
#  Age >= 60:
# o Male or Female:
#  Income > 10,00,000: Tax = 20%
#  Income <= 10,00,000: Tax = 10%
age=int(input("Enter your age : "))
gender=input("Enter your gender (M/F) : ").lower()
income=int(input("Enter your income : "))
if age>=18 and age<60:
    if gender=='m':
        if income>1000000:
            tax=0.3
        elif income<1000000 and income>500000:
            tax=0.2
        else:
            tax=0.1
    elif gender=='f':
        if income>1000000:
            tax=0.25
        elif income<1000000 and income>500000:
            tax=0.15
        else:
            tax=0.5
    else:
        print("Invalid gender")
elif age>=60:
    if gender=='m' or gender=='f':
        if income>1000000:
            tax=0.2
        else:
            tax=0.1
    else:
        print("Invalid Gender!")
print(f"The income tax is {income*tax}")
print(f"The income after deducting income tax is {income-(income*tax)}")