# 19. Accept a BMI value from the user:
#  If BMI < 18.5, print "Underweight".
#  If 18.5 ≤ BMI < 24.9, print "Normal weight".
#  If 25 ≤ BMI < 29.9, print "Overweight".
#  If BMI ≥ 30, print "Obesity"
bmi=int(input("Enter your BMI value : "))
if bmi<18.5:
    print("Underweight")
elif 18.5<=bmi<24.9:
    print("Normal weight")
elif 25<=bmi<29.9:
    print("Overweight")
else:
    print("Obesity")