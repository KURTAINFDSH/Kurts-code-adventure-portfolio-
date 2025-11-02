#Title
print("KURTS BASIC CALCULATOR")

#loop for continues solving
while True:
  
#NUMBER INPUT
  first_number = input("First-Number: ")

  second_number = input("Second-number: ")


#OPERATIONS
  print('[+]Plus')
  print('[*]multiply')
  print('[/]divide')
  print('[-]subtract')
  operation = input("Operation: ")

#functions
  if operation == '+':
      plus = int(first_number) + int(second_number)
      print(f"{first_number} + {second_number} = {plus}")
  
  elif operation == '*':
      multiply = int(first_number) * int(second_number)
      print(f"{first_number} * {second_number} = {multiply}")

  elif operation == '/':
      divide = float(first_number) / float(second_number)
      print(f"{first_number} / {second_number} = {divide}")
  
  elif operation == '-':
      subtract = int(first_number) - int(second_number)
      print(f"{first_number} - {second_number} = {subtract}")
      
#else statement if wrong operation inputed
  else:
    print("invalid Operation please try again using Operation below")
    print('[+]Plus')
    print('[*]multiply')
    print('[/]divide')
    print('[-]subtract')