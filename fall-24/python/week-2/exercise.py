# Get the name and age information from the user and
# display the output

yourName = input("Please input your name: ")
print("I think that ", yourName, " is a good name")
yourAge = input("Please input tour age: ")
print("You are ", yourAge, " yars old.")

# Read the name, birth Month and age information from
# the user. Print these values as well as the doubled age
# information

name = input("Input your name: ")
birthMonth = input("Imput your birth month: ")
age = int(input("Iput your age: "))

print(name, birthMonth, age * 2)


# Read a word from the user and a number N. Print that
# word N times

someWord = input("Input some word here: ")
N = int(input("Inform a number: "))
i = 0

while i < N:
  print(someWord, i)

  i += 1 

# Find the area and peremiter of a rectangle

lenght = float(input("Inform the lenght: "))
width = float(input("Inform the width: "))
area = lenght * width
perimeter = 2 * (lenght + width)

print(f"The area is: {area}, the peremiter is: {perimeter}")
