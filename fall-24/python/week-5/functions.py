def square(n):
  return n ** 2


def convert_distance(kilometer):
  return kilometer * 0.621371

number_to_square = int(input("Inform a number to find its square: "))
squared_number = square(number_to_square)
print(f"The squared number is: {squared_number}")

km = float(input("Inform the distance in kilometer: "))
distance_converted = convert_distance(km)
print(f"The result of the conversion is: {distance_converted} miles")