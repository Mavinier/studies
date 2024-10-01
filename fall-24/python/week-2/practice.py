# QUESTION - 1

# Input user name, password and confirm password in three strings,
# check if the two password matches (same).

# name = input("Input your name: ")
# password = input("Input your password: ")
# confirmPassword = input("Confirm your password: ")

# if(password == confirmPassword):
#   print("Login successful")
# else:
#   print("Wrong Credentials")

# QUESTION - 2

# Write a Python program that reads a the body temperature (in degree celsius) from the user.
# Normal body temperature ranges from 36.4°C to 37.2°C. If the temperature is below 36.4°C then
# it should print “Too low!”, if the input number is above 37.2°C it should print “Too high!”.
# Otherwise, it should print “You are doing great!”


# userBodyTemperature = float(input("Input your body temperature in Celsius: "))

# if(userBodyTemperature < 36.4):
#   print("Too low!")
# elif(userBodyTemperature > 37.2):
#   print("Too high!")
# else:
#   print("You are doing great!")


# QUESTION - 3

grade = int(input("Input your grade: "))

match grade:
  case grade if 10  < grade < 20:
    print("Better stay at home")
  case grade if 20 <= grade < 50:
    print("Pass grade")
  case grade if 50 <= grade < 70:
    print("C Grade")
  case grade if 70 <= grade < 80:
    print("B Grade")
  case _:
    print("A Grade")
