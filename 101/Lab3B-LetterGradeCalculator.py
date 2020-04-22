    #   Austin Copley
    #   ​CSCI 101 – Section F
    #   Python Lab 3B
first_name = input("FIRSTNAME> ")
scholars = input("SCHOLARS> ")
weight1 = float(input("WEIGHT1> "))
weight2 = float(input("WEIGHT2> "))
grade1 = float(input("GRADE1> "))
grade2 = float(input("GRADE2> "))
total_grade = weight1 * grade1 + weight2 * grade2

if first_name in scholars and total_grade >= 80:
    status = "Current"
elif first_name in scholars and 80 > total_grade >= 70:
    status = "Probation"
elif first_name in scholars and 70 > total_grade:
    status = "Terminated"
elif first_name not in scholars and total_grade >= 90:
    status = "New"
else:
    status = "None"

if total_grade >= 90:
    letter_grade = 'A'
elif 90 > total_grade >= 80:
    letter_grade = 'B'
elif 80 > total_grade >= 70:
    letter_grade = 'C'
elif 70 > total_grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
print("Current Grade Percentage of", first_name,"is:")
print("OUTPUT", str(round(total_grade, 2)) + "%")
print("Current Letter Grade of", first_name, "is:")
print("OUTPUT", letter_grade)
print("Updated Scholar Status:")
print("OUTPUT", status)
print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
