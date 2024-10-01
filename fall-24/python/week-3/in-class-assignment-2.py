# QUESTION - 1

name = input("Input your name: ")
password = input("Input your password: ")
confirmPassword = input("Confirm your password: ")

if(password == confirmPassword):
  print("Login successful")
else:
  print("Wrong Credentials")

# QUESTION - 2

userBodyTemperature = float(input("Input your body temperature in Celsius: "))

if(userBodyTemperature < 36.4):
  print("Too low!")
elif(userBodyTemperature > 37.2):
  print("Too high!")
else:
  print("You are doing great!")