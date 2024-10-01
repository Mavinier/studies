# Print Numbers from 1 to 10
# for n in range(1,11):
#   print(n)

# Sum of First N Numbers
# number = int(input("Please inform a number: "))
# listnNumber = []
# for n in range(1, number):
#   listnNumber.append(n)
#   result = sum(listnNumber)
#   print(listnNumber)
# 20

# Print Even Numbers
for n in range(1,20):
  if n % 2 == 0:  
    print(n)

# Print reverse string
string_to_reverse = "Let's reverse this string!"
reversed_s = ''
for i in range(len(string_to_reverse) -1, -1, -1):
  reversed_s += string_to_reverse[i]
print(reversed_s)


