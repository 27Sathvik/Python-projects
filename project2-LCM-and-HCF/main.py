num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

def lcm():
  greater_number = max([num1,num2])
  while greater_number % (num1 and num2) != 0:
    greater_number += 1
  return greater_number

def hcf():
  smaller_number = min([num1,num2])
  while smaller_number % (num1 and num2) != 0:
    smaller_number -= 1
  return smaller_number

print("LCM OF {} AND {} IS {}".format(num1,num2,lcm()))

print("HCF OF {} AND {} IS {}".format(num1,num2,hcf()))