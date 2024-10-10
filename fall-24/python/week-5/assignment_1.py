# Q1
NUMBER_TO_REVERSE = 76542
reversed_num = 0
while NUMBER_TO_REVERSE != 0:
    digit = NUMBER_TO_REVERSE % 10
    reversed_num = reversed_num * 10 + digit
    NUMBER_TO_REVERSE //= 10

print(f"{reversed_num}")

# Q2
input_number = int(input("Inform a number: "))

for n in range(1, input_number + 1):
  if n % 2 == 0:
    square = n ** 2
    print(f"Current number is : {n} and the square is {square}")
  else:
    cube = n ** 3
    print(f"Current number is : {n} and the cube is {cube}")