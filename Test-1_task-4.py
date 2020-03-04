
def calculate_grade(percentage):
    
    if percentage<=100 and percentage>=90:
        return "A"
    elif percentage<90 and percentage>=80:
        return "B"
    elif percentage<80 and percentage>=70:
        return "C"
    elif percentage<70 and percentage>=60:
        return "D"
    elif percentage<60 and percentage>=50:
        return "E"
    elif percentage<50 and percentage>=40:
         return "F"
m1,m2,m3,m4,m5=[float(x) for x in input("enter the number of 5 subjects ").split()]
marks=m1+m2+m3+m4+m5
percentage=(marks/5)
grade=calculate_grade(percentage)
print("percentage=",percentage, "Grade=",grade)
