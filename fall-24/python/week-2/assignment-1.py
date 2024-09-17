# Question - 1
radius = float(input("Please inform the radius: "))
if (radius <= 0 ):
  print("Area can not be calculated")
else:
  area = (radius ** 2) * 3.14159 
  perimeter = 2 * 3.14159

print("The area is:", area)
print("The perimeter is:", perimeter)

# Question - 2
age = int(input("Enter your age: "))

if (age >= 0 and age <= 12):
  userIs = "Junior"
elif (age > 12 and age <= 19):
  userIs = "Teenager"
else:
  userIs = "Senior"

print("The user is",userIs )

# # Question - 3

grade = int(input("Input your grade: "))

if(grade < 70):
  letterGrade = "F"
elif(grade >= 70 and grade < 80):
  letterGrade = "C"
elif(grade >= 80 and grade < 90):
  letterGrade = "B"
else:
  letterGrade = "A"

print("The letter grade for this student is: ", letterGrade)